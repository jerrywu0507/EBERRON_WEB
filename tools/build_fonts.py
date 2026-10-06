# -*- coding: utf-8 -*-
"""把思源宋體（Noto Serif CJK TC）子集化成只含本站用字的 woff2，放進 static/fonts/ 自帶。

用法：  .venv\Scripts\python.exe tools\build_fonts.py
- 原始 OTF 太大（每個 24 MB）不進版控；第一次執行會下載到 ~/.cache/eberron-fonts/。
- 正文字重 400 的字元集 = data/*.json + guide/*.py + app.py 的所有字元 + 常用標點與數字區段。
- 標題字重 600 / 900 與手寫體只收「頁面上真的以那個字重／字型顯示過的字」（tools/fontsets.json，
  由 tools/collect_chars.py 從跑著的站台收集；缺這個檔就退回全字集）。這讓首次載入的字型從約 3.9 MB 降到一半以下。
- 新增內容含新字後：先 collect_chars.py 再重跑本腳本；沒跑也不會壞：CSS 仍保留 Google Fonts 作後備，缺的字落回線上字型。
需要：pip install fonttools brotli
"""
import glob
import io
import json
import os
import sys
import urllib.request

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "fonts")
CACHE = os.path.join(os.path.expanduser("~"), ".cache", "eberron-fonts")
BASE = "https://raw.githubusercontent.com/notofonts/noto-cjk/main/Serif/OTF/TraditionalChinese/"
FACES = [("Regular", 400), ("SemiBold", 600), ("Black", 900)]
# 手寫註記用的霞鶩文楷 TC（同樣只進版控子集；原檔約 15 MB）
HAND = ("https://github.com/lxgw/LxgwWenkaiTC/releases/download/v1.522/LXGWWenKaiTC-Regular.ttf", "LXGWWenKaiTC-Regular.ttf", "LXGWWenKaiTC-400.woff2")
# 固定納入的區段：ASCII、Latin-1、一般標點、CJK 標點、全形字元、中文數字（清單序號）
RANGES = ["0020-007E", "00A0-00FF", "2010-2027", "2030-203B", "2190-2199", "3000-303F", "FF00-FFEF",
          "4E00", "4E8C", "4E09", "56DB", "4E94", "516D", "4E03", "516B", "4E5D", "5341", "3007"]


def site_chars():
    chars = set()
    files = glob.glob(os.path.join(ROOT, "data", "*.json")) + glob.glob(os.path.join(ROOT, "guide", "*.py"))
    files += [os.path.join(ROOT, "app.py"), os.path.join(ROOT, "assets", "styles.css")]
    for f in files:
        with io.open(f, encoding="utf-8") as fh:
            chars |= set(fh.read())
    return "".join(sorted(c for c in chars if ord(c) > 0x7F and not c.isspace()))


def display_sets():
    """tools/fontsets.json 裡各字重實際用到的字；沒有檔案時回傳 None（全部退回全字集）。"""
    path = os.path.join(ROOT, "tools", "fontsets.json")
    if not os.path.exists(path):
        print("tools/fontsets.json 不存在，600/900/手寫體使用全字集（先跑 tools/collect_chars.py 可瘦身）")
        return None
    with io.open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    # 700 / 800 沒有自己的字型檔，瀏覽器會拿 900 來用，所以併進 900
    return {
        600: data.get("serif600", ""),
        900: "".join(sorted(set(data.get("serif900", "")) | set(data.get("serif700", "")) | set(data.get("serif800", "")))),
        "hand": data.get("hand", ""),
    }


def fetch(name, url=None):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        print("downloading", name)
        urllib.request.urlretrieve(url or (BASE + name), path)
    return path


def subset_to(src, dst, text):
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.hinting = False
    opts.desubroutinize = True  # 子集後反而較小
    opts.layout_features = ["kern", "liga", "palt", "ccmp", "locl"]
    opts.name_IDs = [1, 2, 3, 4, 6]
    font = TTFont(src)
    s = subset.Subsetter(opts)
    s.populate(text=text, unicodes=subset.parse_unicodes(",".join(RANGES)))
    s.subset(font)
    font.flavor = "woff2"
    font.save(dst)
    print("wrote", os.path.relpath(dst, ROOT), "%d KB" % (os.path.getsize(dst) // 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    text = site_chars()
    print("site characters:", len(text))
    shown = display_sets()
    for face, weight in FACES:
        chars = text if (shown is None or weight == 400) else shown[weight]
        print("weight %d: %d characters" % (weight, len(chars)))
        subset_to(fetch("NotoSerifCJKtc-%s.otf" % face), os.path.join(OUT, "NotoSerifTC-%d.woff2" % weight), chars)
    url, name, out = HAND
    chars = text if shown is None else shown["hand"]
    print("hand: %d characters" % len(chars))
    subset_to(fetch(name, url), os.path.join(OUT, out), chars)

if __name__ == "__main__":
    sys.exit(main())
