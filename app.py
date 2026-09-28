# -*- coding: utf-8 -*-
"""艾伯倫導覽：一疊給新任探員翻閱的卷宗。Streamlit 多頁入口。"""
import importlib
import os
import threading

import streamlit as st

st.set_page_config(page_title="艾伯倫導覽", page_icon=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "favicon.png"), layout="wide", initial_sidebar_state="auto")

from guide import pages, ui  # noqa: E402  (set_page_config 必須是第一個 Streamlit 呼叫)

_GUIDE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guide")
_RELOAD_LOCK = threading.Lock()


def _fresh_modules():
    """雲端主機（Community Cloud）把新提交拉進執行中的程序時，主程式與 styles.css 每次執行都會重讀，
    但已載入的 guide 模組會留在舊版，畫面就變成「舊標記配新樣式」。這裡比對兩個模組檔的修改時間，
    變了就重新載入（先 ui 再 pages，因為 pages 從 ui 匯入名稱）。"""
    stamp = tuple(os.path.getmtime(os.path.join(_GUIDE, f)) for f in ("ui.py", "pages.py"))
    if getattr(ui, "_STAMP", None) != stamp:
        with _RELOAD_LOCK:
            if getattr(ui, "_STAMP", None) != stamp:
                importlib.reload(ui)
                importlib.reload(pages)
                ui._STAMP = stamp


_fresh_modules()

FUNCS = {
    "": pages.cover, "history": pages.history, "nations": pages.nations, "sharn": pages.sharn,
    "houses": pages.houses, "races": pages.races, "faiths": pages.faiths, "planes": pages.planes,
    "appendix": pages.appendix,
}

page_objs = []
for i, v in enumerate(ui.VOLUMES):
    kwargs = {"title": v["title"], "default": i == 0}
    if v["path"]:
        kwargs["url_path"] = v["path"]
    page_objs.append(st.Page(FUNCS[v["path"]], **kwargs))
ui.PAGE_OBJS = page_objs

current = st.navigation(page_objs, position="sidebar")
ui.inject_css()
current.run()
