# -*- coding: utf-8 -*-
"""從跑著的本機站台收集「每個字型／字重實際用到哪些字」，寫到 tools/fontsets.json，供 build_fonts.py 瘦身子集。

用法：  先 .\start_streamlit.ps1（或 restart），再  .venv\Scripts\python.exe tools\collect_chars.py [http://127.0.0.1:8509]
- 以 Chrome DevTools 協定開每一頁（桌面 1440 與手機 390 各一遍），走訪所有可見文字節點，
  依 computed font-family / font-weight 分類：serif400 / serif600 / serif700 / serif900 / hand / mono。
- 正文（serif400）不靠這份清單（build_fonts.py 仍掃全部資料檔）；清單只用來縮小 600 / 900 與手寫體。
- 缺字不會壞：styles.css 仍 @import Google Fonts 作後備，不在子集裡的字會落回線上字型。
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import snap  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "fontsets.json")
PAGES = ["", "history", "nations", "sharn", "houses", "races", "faiths", "planes", "appendix"]

COLLECT = r"""(function(){
  var out = {};
  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
  var node;
  while ((node = walker.nextNode())) {
    var text = node.nodeValue; if (!text || !text.trim()) continue;
    var el = node.parentElement; if (!el) continue;
    var cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    var fam = cs.fontFamily.toLowerCase(); var key;
    if (fam.indexOf('wenkai') >= 0) key = 'hand';
    else if (fam.indexOf('courier') >= 0) key = 'mono';
    else if (fam.indexOf('noto serif') >= 0) key = 'serif' + cs.fontWeight;
    else continue;
    out[key] = out[key] || {};
    for (var i = 0; i < text.length; i++) { var ch = text[i]; if (ch.charCodeAt(0) > 127 && ch.trim()) out[key][ch] = 1; }
  }
  var res = {}; for (var k in out) res[k] = Object.keys(out[k]).join('');
  return JSON.stringify(res);
})()"""


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8509"
    sets = {}
    chrome = snap.Chrome()
    try:
        chrome.send("Page.enable")
        for width in (1440, 390):
            chrome.send("Emulation.setDeviceMetricsOverride", width=width, height=900, deviceScaleFactor=1, mobile=width < 500)
            for page in PAGES:
                chrome.send("Page.navigate", url="%s/%s" % (base, page))
                for _ in range(80):
                    time.sleep(0.5)
                    try:
                        if chrome.eval("!!document.querySelector('.folder,.cover')"):
                            break
                    except Exception:
                        pass
                time.sleep(2)
                found = json.loads(chrome.eval(COLLECT))
                for key, chars in found.items():
                    sets.setdefault(key, set()).update(chars)
                print("%4d /%-9s" % (width, page or "cover"), {k: len(v) for k, v in found.items()})
    finally:
        chrome.close()
    data = {k: "".join(sorted(v)) for k, v in sorted(sets.items())}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    print("wrote", os.path.relpath(OUT, ROOT), {k: len(v) for k, v in data.items()})


if __name__ == "__main__":
    sys.exit(main())
