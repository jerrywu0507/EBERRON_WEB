# -*- coding: utf-8 -*-
"""艾伯倫導覽：一疊給新任探員翻閱的卷宗。Streamlit 多頁入口。"""
import os

import streamlit as st

st.set_page_config(page_title="艾伯倫導覽", page_icon=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "favicon.png"), layout="wide", initial_sidebar_state="auto")

from guide import pages, ui  # noqa: E402  (set_page_config 必須是第一個 Streamlit 呼叫)

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
