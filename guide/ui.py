# -*- coding: utf-8 -*-
"""卷宗世界的共用零件：資料載入、公文用箋、印章、帳冊表、時間軸、圖版、行動版標籤列。"""
import html
import io
import json
import os

import streamlit as st

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
ASSETS = os.path.join(ROOT, "assets")

# 各卷：標題、網址、標籤色、篇幅權重（決定索引標籤高度）。app.py 依此建立頁面。
VOLUMES = [
    {"title": "卷宗封面", "path": "", "tab": "indigo", "weight": 6},
    {"title": "第一卷 歷史", "path": "history", "tab": "indigo", "weight": 6},
    {"title": "第二卷 諸國", "path": "nations", "tab": "seal", "weight": 11},
    {"title": "第三卷 薩恩", "path": "sharn", "tab": "seal", "weight": 5},
    {"title": "第四卷 龍紋家族", "path": "houses", "tab": "green", "weight": 5},
    {"title": "第五卷 種族", "path": "races", "tab": "green", "weight": 6},
    {"title": "第六卷 信仰與組織", "path": "faiths", "tab": "ochre", "weight": 11},
    {"title": "第七卷 位面", "path": "planes", "tab": "ochre", "weight": 5},
    {"title": "附錄", "path": "appendix", "tab": "violet", "weight": 7},
]
TAB_COLORS = {"indigo": "#16233f", "seal": "#b3261e", "green": "#2c6e49", "ochre": "#d7a021", "violet": "#5b3a8a"}
TAB_INK = {"ochre": "var(--ink)"}  # 淺色標籤選中時要用墨色字，白字在赭黃上對比不到 4.5:1

# 印泥效果：SVG 濾鏡讓印章邊緣不整、掉墨點、濃淡不一；ink-fine 是給小章的輕版。inject_css 注入一次。
INK_FILTERS = (
    '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">'
    '<filter id="ink-seal" x="-8%" y="-16%" width="116%" height="132%" color-interpolation-filters="sRGB">'
    '<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="11" result="grain"/>'
    '<feColorMatrix in="grain" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 14 -4.2" result="holes"/>'
    '<feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="4" result="wash"/>'
    '<feColorMatrix in="wash" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.6 0.66" result="density"/>'
    '<feComposite in="SourceGraphic" in2="holes" operator="in" result="a"/>'
    '<feComposite in="a" in2="density" operator="in" result="b"/>'
    '<feTurbulence type="turbulence" baseFrequency="0.05" numOctaves="2" seed="7" result="warp"/>'
    '<feDisplacementMap in="b" in2="warp" scale="3" xChannelSelector="R" yChannelSelector="G"/>'
    '</filter>'
    '<filter id="ink-fine" x="-8%" y="-16%" width="116%" height="132%" color-interpolation-filters="sRGB">'
    '<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5" result="grain"/>'
    '<feColorMatrix in="grain" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 14 -3.4" result="holes"/>'
    '<feComposite in="SourceGraphic" in2="holes" operator="in" result="a"/>'
    '<feTurbulence type="turbulence" baseFrequency="0.08" numOctaves="1" seed="9" result="warp"/>'
    '<feDisplacementMap in="a" in2="warp" scale="1.6" xChannelSelector="R" yChannelSelector="G"/>'
    '</filter>'
    '<linearGradient id="clip-metal" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#e9ebee"/><stop offset="0.45" stop-color="#8e96a3"/><stop offset="0.55" stop-color="#d7dbe0"/><stop offset="1" stop-color="#6c7480"/>'
    '</linearGradient>'
    '</svg>'
)

# 迴紋針：一條金屬絲的路徑，夾在照片頂邊
PAPERCLIP = (
    '<svg class="clip" viewBox="0 0 30 74" aria-hidden="true">'
    '<path d="M9 20 V56 a6 6 0 0 0 12 0 V14 a8 8 0 0 0 -16 0 V50 a10 10 0 0 0 20 0 V22"/>'
    '</svg>'
)


def tab_vars(tab):
    """一張標籤的 CSS 變數：底色，淺色標籤另給選中時的字色。"""
    s = "--tab:%s" % TAB_COLORS[tab]
    if tab in TAB_INK:
        s += ";--tab-ink:%s" % TAB_INK[tab]
    return s
PAGE_OBJS = []  # app.py 建立 st.Page 後填入


@st.cache_data(show_spinner=False)
def load(name):
    with io.open(os.path.join(DATA, name + ".json"), encoding="utf-8") as f:
        return json.load(f)


def _css_text():
    with io.open(os.path.join(ASSETS, "styles.css"), encoding="utf-8") as f:
        return f.read()


def inject_css():
    """注入世界樣式；索引標籤的顏色與高度依各卷篇幅比例產生。"""
    rules = []
    for i, v in enumerate(VOLUMES, start=1):
        height = 56 + v["weight"] * 8
        rules.append(
            'section[data-testid="stSidebar"] [data-testid="stSidebarNav"] li:nth-child(%d) a{%s;min-height:%dpx}'
            % (i, tab_vars(v["tab"]), height)
        )
    st.markdown("<style>%s\n%s</style>%s" % (_css_text(), "\n".join(rules), INK_FILTERS), unsafe_allow_html=True)


def esc(text):
    return html.escape(str(text), quote=False)


def en(term):
    """英文原名，以打字機字體當碳寫註記。"""
    return '<span class="en">%s</span>' % esc(term) if term else ""


def term(zh, term_en):
    return esc(zh) + en(term_en)


def paras(*texts):
    return "".join("<p>%s</p>" % esc(t) for t in texts if t)


def raw(html_text):
    st.markdown(html_text.replace("\n", " "), unsafe_allow_html=True)


def sheet(title, title_en=None, body="", ref=None, stamp=None, cls="", lead=None):
    """一張紅格公文用箋。body 是已組好的 HTML。"""
    parts = ['<section class="sheet %s">' % cls]
    if ref:
        parts.append('<div class="ref">%s</div>' % esc(ref))
    if stamp:
        parts.append('<div class="stamp">%s</div>' % esc(stamp))
    parts.append("<h2>%s%s</h2>" % (esc(title), en(title_en)))
    parts.append('<div class="body">')
    if lead:
        parts.append('<p class="lead">%s</p>' % esc(lead))
    parts.append(body)
    parts.append("</div></section>")
    raw("".join(parts))


def meta(rows):
    """dl 形式的欄位：[(標籤, 值HTML), ...]"""
    return '<dl class="meta">%s</dl>' % "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), v) for k, v in rows)


def tags(items):
    return '<div class="tags">%s</div>' % "".join("<span>%s</span>" % esc(t) for t in items)


def ledger(cols, rows):
    """帳冊表。cols: [(key, 標題, 是否數字欄)]；rows: dict 列表，值可為 HTML。"""
    head = "".join('<th class="%s">%s</th>' % ("num" if num else "", esc(label)) for key, label, num in cols)
    body = []
    for r in rows:
        body.append("<tr>%s</tr>" % "".join(
            '<td class="%s">%s</td>' % ("num" if num else "", r.get(key, "")) for key, label, num in cols))
    return '<table class="ledger"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (head, "".join(body))


def timeline(items):
    lis = []
    for it in items:
        lis.append('<li><span class="year">%s</span><div class="label">%s</div><p>%s</p></li>'
                   % (esc(it["year"]), esc(it["label"]), esc(it["body"])))
    return '<ol class="rule">%s</ol>' % "".join(lis)


def note(label, text):
    return '<div class="note"><strong>%s</strong>%s</div>' % (esc(label), esc(text))


def plate(number, caption, svg):
    return ('<figure class="plate"><div class="art">%s</div><figcaption><b>圖版%s</b>%s</figcaption></figure>'
            % (svg, esc(number), esc(caption)))


def photo(src, caption, alt, full=None, label="照片"):
    """一張用迴紋針夾在用箋上的照片。src 是 static 目錄下的檔名；full 給原尺寸檔，點開另開新頁。"""
    img = '<img src="/app/static/%s" alt="%s" loading="lazy">' % (esc(src), esc(alt))
    if full:
        img = '<a href="/app/static/%s" target="_blank" rel="noopener">%s</a>' % (esc(full), img)
    return ('<figure class="photo">%s%s<figcaption><b>%s</b>%s</figcaption></figure>'
            % (PAPERCLIP, img, esc(label), esc(caption)))


def stamp_inline(text, kind="ok"):
    return '<span class="stamp %s">%s</span>' % (kind, esc(text))
