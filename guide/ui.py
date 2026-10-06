# -*- coding: utf-8 -*-
"""案卷世界的共用零件：資料載入、文件（白紙、記錄單、紅色檔案卡、警示紙、便條、拍立得、名片）、
印章、固定物（長尾夾、鐵夾、迴紋針、膠帶）、行動版標籤列。每個零件回傳 HTML，page() 把一頁的文件裝進同一個攤開的檔案夾。"""
import base64
import html
import io
import json
import mimetypes
import os
import re

import streamlit as st

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
ASSETS = os.path.join(ROOT, "assets")
STATIC = os.path.join(ROOT, "static")

# 各卷：標題、網址、標籤色、篇幅權重（決定索引標籤高度份額）。app.py 依此建立頁面。
VOLUMES = [
    {"title": "卷宗封面", "path": "", "tab": "indigo", "weight": 6},
    {"title": "第一卷 歷史", "path": "history", "tab": "indigo", "weight": 8},
    {"title": "第二卷 諸國", "path": "nations", "tab": "seal", "weight": 11},
    {"title": "第三卷 薩恩", "path": "sharn", "tab": "seal", "weight": 11},
    {"title": "第四卷 龍紋家族", "path": "houses", "tab": "green", "weight": 5},
    {"title": "第五卷 種族", "path": "races", "tab": "green", "weight": 6},
    {"title": "第六卷 信仰與組織", "path": "faiths", "tab": "ochre", "weight": 11},
    {"title": "第七卷 位面", "path": "planes", "tab": "ochre", "weight": 10},
    {"title": "附錄", "path": "appendix", "tab": "violet", "weight": 7},
]
TAB_COLORS = {"indigo": "#2f3f6e", "seal": "#c2321f", "green": "#5f8f6c", "ochre": "#d9a23a", "violet": "#6c5a91"}
TAB_INK = {"ochre": "var(--kraft-ink)"}  # 淺色標籤選中時要用深色字

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

# 固定物
BULLDOG = ('<div class="bulldog" aria-hidden="true"><div class="ring"></div><div class="arm l"></div>'
           '<div class="arm r"></div><div class="jaw"></div></div>')
BINDER = '<div class="binder" aria-hidden="true"></div>'


def paperclip(cls="clip"):
    """迴紋針：一條金屬絲的路徑。"""
    return ('<svg class="%s" viewBox="0 0 30 74" aria-hidden="true">'
            '<path d="M9 20 V56 a6 6 0 0 0 12 0 V14 a8 8 0 0 0 -16 0 V50 a10 10 0 0 0 20 0 V22"/></svg>' % cls)


def tab_vars(tab):
    """一張標籤的 CSS 變數：底色，淺色標籤另給選中時的字色。"""
    s = "--tab:%s" % TAB_COLORS[tab]
    if tab in TAB_INK:
        s += ";--tab-ink:%s" % TAB_INK[tab]
    return s
PAGE_OBJS = []  # app.py 建立 st.Page 後填入


@st.cache_data(show_spinner=False)
def _load(path, mtime):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def load(name):
    """讀一卷的資料。快取鍵含檔案修改時間：雲端把新資料拉進執行中的程序時，舊快取不會再被端出來。"""
    path = os.path.join(DATA, name + ".json")
    return _load(path, os.path.getmtime(path))


def static_enabled():
    """執行中的程序有沒有 /app/static 路由。它在啟動時依 server.enableStaticServing 註冊；
    雲端主機拉進新的 config.toml 不會重啟程序，所以要問執行中的設定值，不能假設檔案裡寫了就有。"""
    try:
        return bool(st.config.get_option("server.enableStaticServing"))
    except Exception:
        return True


@st.cache_data(show_spinner=False)
def _data_uri(path, mtime):
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


def static_url(name):
    """static/ 裡一個檔案的網址：正常走相對路徑 app/static/；沒有那條路由時改成 data URI 內嵌，圖片與紙紋才不會破。"""
    path = os.path.join(STATIC, name)
    if static_enabled():
        # 版本參數：檔案一換網址就換，瀏覽器或雲端快取裡的舊回應（例如路由還沒開時拿到的 HTML）不會再被端出來
        # 相對路徑（沒有開頭的斜線）：Community Cloud 把 app 放在 /~/+/ 基底路徑底下，絕對路徑 /app/static 會打到代理層拿回 HTML
        return "app/static/%s?v=%d" % (name, int(os.path.getmtime(path)))
    return _data_uri(path, os.path.getmtime(path))


def _css_text():
    with io.open(os.path.join(ASSETS, "styles.css"), encoding="utf-8") as f:
        return f.read()


def _css_for_runtime():
    css = _css_text()
    if static_enabled():
        return css
    # 沒有 /app/static 路由：紙紋內嵌；自帶字型那幾行拿掉，讓 @import 的 Google Fonts 接手（手寫字退回宋體）
    for tile in ("paper-grain.png", "kraft-grain.png"):
        css = css.replace("url(app/static/%s)" % tile, "url(%s)" % static_url(tile))
    return chr(10).join(line for line in css.splitlines() if not line.startswith("@font-face {"))


def inject_css():
    """注入世界樣式；索引標籤的顏色與高度份額（--w）依各卷篇幅權重產生，標籤軌永遠剛好一個視窗高。"""
    rules = []
    for i, v in enumerate(VOLUMES, start=1):
        rules.append(
            'section[data-testid="stSidebar"] [data-testid="stSidebarNav"] li:nth-child(%d){--w:%d}'
            'section[data-testid="stSidebar"] [data-testid="stSidebarNav"] li:nth-child(%d) a{%s}'
            '.st-key-tabstrip [data-testid="stElementContainer"]:nth-child(%d){%s}'
            % (i, v["weight"], i, tab_vars(v["tab"]), i, tab_vars(v["tab"]))
        )
    st.markdown("<style>%s\n%s</style>%s" % (_css_for_runtime(), "\n".join(rules), INK_FILTERS), unsafe_allow_html=True)


# ---------------------------------------------------------------- 文字
def esc(text):
    return html.escape(str(text), quote=False)


def en(term):
    """英文原名，以打字機字體當碳寫註記。"""
    return '<span class="en">%s</span>' % esc(term) if term else ""


def term(zh, term_en):
    return esc(zh) + en(term_en)


def hand(text):
    """手寫字（鋼筆藍）。"""
    return '<span class="hand">%s</span>' % esc(text)


def paras(*texts):
    return "".join("<p>%s</p>" % esc(t) for t in texts if t)


def raw(html_text):
    st.markdown(html_text.replace("\n", " "), unsafe_allow_html=True)


def _tilt(t):
    return ' style="--tilt:%sdeg"' % t if t is not None else ""


def _toc(title):
    """文件的目錄標題屬性；folder() 讀它來排卷內目錄並配 id。"""
    return ' data-toc="%s"' % html.escape(str(title), quote=True) if title else ""


_TOC_RE = re.compile(r'^<section class="(?:doc|form|card|slip)[^"]*"[^>]*?data-toc="([^"]*)"')


# ---------------------------------------------------------------- 文件
def doc(title, title_en=None, body="", ref=None, stamp=None, cls="", lead=None, bureau=None, tilt=None):
    """一張白色公文紙。title 為 None 時是接在檔案卡後面的續頁（cls 加 attached）。"""
    parts = ['<section class="doc %s"%s%s>' % (cls, _tilt(tilt), _toc(title))]
    if bureau:
        parts.append('<div class="bureau"><span>%s</span><span>%s</span></div>' % (esc(bureau[0]), esc(bureau[1])))
    if stamp:
        parts.append('<div class="stamp">%s</div>' % esc(stamp))
    if title:
        parts.append("<h2>%s%s</h2>" % (esc(title), en(title_en)))
    parts.append('<div class="body">')
    if lead:
        parts.append('<p class="lead">%s</p>' % esc(lead))
    parts.append(body)
    parts.append("</div>")
    if ref:
        parts.append('<div class="ref">%s</div>' % esc(ref))
    parts.append("</section>")
    return "".join(parts)


def _is_short(value_html):
    plain = re.sub(r"<[^>]+>", "", value_html)
    return len(plain) <= 30 and "<" not in value_html


def form(title, title_en=None, rows=None, ref=None, no=None, lead=None, log=None, table=None, foot=None,
         prose=None, stamp=None, tilt=None, plain_log=False, extra=""):
    """一張印好格式的記錄單。rows 是 (欄名, 值HTML) 的欄位列，短的值用手寫；log 是 (鍵, 事項HTML, 內文HTML) 的條目；
    table 是 ledger HTML；prose 是段落 HTML；foot 是腳註 HTML。"""
    parts = ['<section class="form"%s%s>' % (_tilt(tilt), _toc(title))]
    if stamp:
        parts.append('<div class="stamp">%s</div>' % esc(stamp))
    no_html = ""
    if no:
        no_html = '<div class="no">%s<b>%s</b></div>' % (esc(no[0]), esc(no[1]))
    parts.append('<div class="formhead"><h2>%s%s</h2>%s</div>' % (esc(title), en(title_en), no_html))
    if lead:
        parts.append('<p class="lead">%s</p>' % esc(lead))
    if prose:
        parts.append('<div class="prose">%s</div>' % prose)
    if rows:
        cells = []
        for k, v in rows:
            cls = "v hand" if _is_short(v) else "v"
            cells.append('<div class="row"><div class="k">%s</div><div class="%s">%s</div></div>' % (esc(k), cls, v))
        parts.append('<div class="rows">%s</div>' % "".join(cells))
    if log:
        entries = []
        for key, what, body in log:
            if plain_log or key is None:
                entries.append('<div class="entry"><div><div class="what">%s</div><p>%s</p></div></div>' % (what, body))
            else:
                entries.append('<div class="entry"><div class="key">%s</div><div><div class="what">%s</div><p>%s</p></div></div>'
                               % (esc(key), what, body))
        parts.append('<div class="log %s">%s</div>' % ("plain" if plain_log else "", "".join(entries)))
    if table:
        parts.append(table)
    if extra:
        parts.append(extra)
    if foot:
        parts.append('<div class="foot">%s</div>' % foot)
    if ref:
        parts.append('<div class="ref">%s</div>' % esc(ref))
    parts.append("</section>")
    return "".join(parts)


def card(name, name_en, fields, line=None, stamp=None, tilt=None, emblem=None):
    """紅色檔案卡：名稱、原名、一句話、欄位。左緣一枚鐵夾。長文放在後面 attached 的白紙上。
    emblem 是貼在卡片右上角的一張小相片（國旗、徽章），像檔案卡上的證件照。"""
    parts = ['<section class="card%s"%s%s>%s' % (" has-emblem" if emblem else "", _tilt(tilt), _toc(name), BINDER)]
    if emblem:
        parts.append('<div class="emblem tape">%s</div>' % emblem)
    if stamp:
        parts.append('<div class="stamp">%s</div>' % esc(stamp))
    parts.append("<h2>%s%s</h2>" % (esc(name), en(name_en)))
    if line:
        parts.append('<p class="line">%s</p>' % esc(line))
    if fields:
        parts.append('<dl class="fields">%s</dl>' % "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (esc(k), v) for k, v in fields))
    parts.append("</section>")
    return "".join(parts)


def attached(body, ref=None, cls="", tilt=None):
    """接在檔案卡下面、從卡片底下露出來的白紙。"""
    return doc(None, body=body, ref=ref, cls="attached " + cls, tilt=tilt)


def slip(title, title_en, body, stamp=None, tilt=None):
    """黃色警示紙。"""
    parts = ['<section class="slip"%s%s>' % (_tilt(tilt), _toc(title))]
    if stamp:
        parts.append('<div class="stamp">%s</div>' % esc(stamp))
    parts.append("<h2>%s%s</h2>" % (esc(title), en(title_en)))
    parts.append('<div class="body">%s</div></section>' % body)
    return "".join(parts)


def note(label, text, hand_written=False):
    """便條：一張貼在文件上的小紙，標籤朱色並自帶全形冒號。"""
    cls = "memo tape hand" if hand_written else "memo tape"
    return '<div class="%s"><strong>%s</strong>%s</div>' % (cls, esc(label), esc(text))


def memos(items):
    """幾張便條並排。items 是 (標籤, 文字) 或已組好的便條 HTML。"""
    inner = "".join(x if isinstance(x, str) else note(*x) for x in items)
    return '<div class="memos">%s</div>' % inner


def meta(rows):
    """dl 形式的欄位：[(標籤, 值HTML), ...]"""
    return '<dl class="meta">%s</dl>' % "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), v) for k, v in rows)


def tags(items):
    return '<div class="tags">%s</div>' % "".join("<span>%s</span>" % esc(t) for t in items)


def ledger(cols, rows):
    """打字機表格。cols: [(key, 標題, 是否數字欄)]；rows: dict 列表，值可為 HTML。
    三欄以上的表在手機上改成一列一張（.stack）：欄名寫進 data-label 由 CSS 印在值前面，短值（.short）並排成一行。"""
    head = "".join('<th class="%s">%s</th>' % ("num" if num else "", esc(label)) for key, label, num in cols)
    body = []
    for r in rows:
        cells = []
        for key, label, num in cols:
            v = r.get(key, "")
            cls = ["num"] if num else []
            if not num and len(re.sub(r"<[^>]+>", "", str(v))) <= 14:
                cls.append("short")
            cells.append('<td class="%s" data-label="%s">%s</td>' % (" ".join(cls), esc(label), v))
        body.append("<tr>%s</tr>" % "".join(cells))
    stack = " stack" if len(cols) >= 3 else ""
    return '<table class="ledger%s" data-cols="%d"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (
        stack, len(cols), head, "".join(body))


def bizcards(items, index=False):
    """一疊名片（牛皮紙）或索引卡（白紙）。items: dict(mark, name, en, lines=[(標籤, 文字)])。"""
    cards = []
    for it in items:
        lines = "".join("<p><b>%s</b>%s</p>" % (esc(k), v) for k, v in it.get("lines", []))
        mark = '<div class="mark">%s</div>' % esc(it["mark"]) if it.get("mark") else ""
        cards.append('<div class="bizcard %s">%s<h3>%s%s</h3>%s</div>' % ("index" if index else "", mark, esc(it["name"]), en(it.get("en")), lines))
    return '<div class="bizcards">%s</div>' % "".join(cards)


def plate(number, caption, svg):
    return ('<figure class="plate"><div class="art">%s</div><figcaption><b>圖版%s</b>%s</figcaption></figure>'
            % (svg, esc(number), esc(caption)))


def polaroid(inner, caption, typed=None, tilt=None, tall=False, small=False):
    """拍立得：白框相紙，下方手寫一行，打字機小字補一行。inner 是 img 或圖版 HTML；tall 給直幅的剖面圖與海報，small 讓幾張相片在同一張方格紙上並排。"""
    t = '<span class="typed">%s</span>' % esc(typed) if typed else ""
    cls = (" tall" if tall else "") + (" small" if small else "")
    return ('<figure class="polaroid tape%s"%s><div class="print">%s</div><figcaption>%s%s</figcaption></figure>'
            % (cls, _tilt(tilt), inner, esc(caption), t))


def photo(src, alt, full=None):
    """static 目錄裡的一張照片；full 給原尺寸檔，點開另開新頁（內嵌模式下省略，免得頁面塞進整張大圖）。"""
    img = '<img src="%s" alt="%s" loading="lazy">' % (static_url(src), esc(alt))
    if full and static_enabled():
        img = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (static_url(full), img)
    return img


def pinboard(*items, tilt=None):
    """一張方格紙，上面貼著幾張拍立得。"""
    return '<div class="pinboard"%s>%s</div>' % (_tilt(tilt), "".join(items))


def stamp_inline(text, kind="ok"):
    return '<span class="stamp %s">%s</span>' % (kind, esc(text))


def folder(*parts, part=None, toc=True):
    """攤開的檔案夾；part 是 top / bottom 時，兩半之間可以放 Streamlit 元件。
    toc=True 且有三件以上有標題的文件時，夾子最上面放一張「卷內目錄」索引卡（頁內錨點），右下角給一枚回頂端的小籤。"""
    cls = "folder" + (" " + part if part else "")
    parts = list(parts)
    entries = []
    if toc and part != "bottom":
        for i, p in enumerate(parts):
            m = _TOC_RE.match(p)
            if m:
                n = len(entries) + 1
                parts[i] = p.replace("<section ", '<section id="sec-%d" ' % n, 1)
                entries.append((n, m.group(1)))
    head = tail = ""
    if len(entries) >= 3:
        head = ('<div id="top"></div><nav class="toc" aria-label="卷內目錄"><span class="head">卷內目錄</span>'
                + "".join('<a href="#sec-%d"><i>%02d</i>%s</a>' % (n, n, t) for n, t in entries) + "</nav>")
        tail = '<a class="totop" href="#top" aria-label="回到頂端" title="回到頂端">▲</a>'
    return '<div class="%s">%s%s%s</div>' % (cls, head, "".join(parts), tail)


def page(*parts, part=None, toc=True):
    raw(folder(*parts, part=part, toc=toc))
