# -*- coding: utf-8 -*-
"""用 Chrome DevTools 協定擷取 Streamlit 頁面：等內容渲染完成後截整頁，或查 DOM。

用法：
  snap.py shot <url> <out.png> <width> [mobile]     整頁截圖（mobile 會模擬觸控裝置）
  snap.py dom  <url> <js-expression>                 等渲染完成後回傳 JS 運算式結果（字串）
"""
import base64
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

import websocket  # websocket-client

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9333
READY_JS = "document.querySelectorAll('.sheet, .cover').length > 0 && document.fonts.status === 'loaded'"


class Chrome:
    def __init__(self):
        self.profile = tempfile.mkdtemp(prefix="snapchrome-")
        self.proc = subprocess.Popen([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
            "--remote-debugging-port=%d" % PORT, "--user-data-dir=%s" % self.profile, "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(60):
            try:
                urllib.request.urlopen("http://127.0.0.1:%d/json/version" % PORT, timeout=1).read()
                break
            except Exception:
                time.sleep(0.25)
        req = urllib.request.Request("http://127.0.0.1:%d/json/new?about:blank" % PORT, method="PUT")
        info = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        self.ws = websocket.create_connection(info["webSocketDebuggerUrl"], suppress_origin=True)
        self.ws.settimeout(60)
        self.seq = 0

    def send(self, method, **params):
        self.seq += 1
        self.ws.send(json.dumps({"id": self.seq, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.seq:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg.get("result", {})

    def eval(self, expr):
        r = self.send("Runtime.evaluate", expression=expr, returnByValue=True)
        return r.get("result", {}).get("value")

    def open(self, url, width, mobile):
        # 一開始就給一個很高的視窗：Streamlit 只排版一次，之後截圖只裁切，不再改視窗大小觸發重排。
        self.send("Emulation.setDeviceMetricsOverride", width=width, height=9000, deviceScaleFactor=1, mobile=mobile)
        if mobile:
            self.send("Emulation.setTouchEmulationEnabled", enabled=True)
        self.send("Page.enable")
        self.send("Page.navigate", url=url)
        for _ in range(120):
            time.sleep(0.5)
            try:
                if self.eval(READY_JS):
                    break
            except Exception:
                pass
        time.sleep(1.5)  # 讓字型與入場動作落定

    def shot(self, out):
        # Streamlit 的主內容在內層容器裡捲動，documentElement 的 scrollHeight 只等於視窗高度；
        # 改量所有用箋與封面的最低邊界，把視窗拉到那麼高再截，內層容器就不需要捲動。
        h = int(self.eval(
            "Math.ceil(Math.max(600, "
            "...Array.from(document.querySelectorAll('.sheet, .cover, .block-container'))"
            ".map(e => e.getBoundingClientRect().bottom + window.scrollY)) + 72)"))
        w = int(self.eval("document.documentElement.clientWidth"))
        h = min(h, 9000)
        data = self.send("Page.captureScreenshot", format="png", captureBeyondViewport=False,
                         clip={"x": 0, "y": 0, "width": w, "height": h, "scale": 1})["data"]
        with open(out, "wb") as f:
            f.write(base64.b64decode(data))
        return w, h

    def close(self):
        try:
            self.ws.close()
        finally:
            self.proc.kill()


def main():
    cmd = sys.argv[1]
    c = Chrome()
    try:
        if cmd == "shot":
            url, out, width = sys.argv[2], sys.argv[3], int(sys.argv[4])
            mobile = len(sys.argv) > 5 and sys.argv[5] == "mobile"
            c.open(url, width, mobile)
            w, h = c.shot(out)
            print("wrote %s (%dx%d)" % (out, w, h))
        elif cmd == "dom":
            url, expr = sys.argv[2], sys.argv[3]
            c.open(url, 1440, False)
            print(c.eval(expr))
    finally:
        c.close()


if __name__ == "__main__":
    main()
