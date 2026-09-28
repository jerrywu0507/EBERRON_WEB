# -*- coding: utf-8 -*-
"""各卷的內容頁。每一頁先一句話說清是什麼，再展開。"""
import streamlit as st

from guide import ui
from guide.ui import esc, en, term, paras, note, meta, tags, ledger, timeline, plate, photo, sheet, raw


def tabstrip(current=""):
    links = "".join('<a href="./%s" style="%s"%s>%s</a>'
                    % (v["path"], ui.tab_vars(v["tab"]), ' aria-current="page"' if v["path"] == current else "", esc(v["title"]))
                    for v in ui.VOLUMES)
    raw('<nav class="tabstrip" aria-label="各卷">%s</nav>' % links)


# ---------------------------------------------------------------- 封面
def cover():
    tabstrip("")
    d = ui.load("overview")
    heads = "".join('<a href="./%s" style="%s">%s</a>' % (v["path"], ui.tab_vars(v["tab"]), esc(v["title"]))
                    for v in ui.VOLUMES[1:])
    raw(
        '<section class="cover" aria-label="卷宗封面">'
        '<div class="spine"></div>'
        '<div class="cover-grid">'
        '<h1 class="vtitle">艾伯倫</h1>'
        '<div class="cover-meta">'
        '<p class="dossier">王座堡卷宗</p>'
        '<p class="sub">致新任探員的簡報 <span class="en">%s</span></p>'
        '<dl class="filenum"><dt>檔號</dt><dd>998-YK-001</dd><dt>日期</dt><dd>王國曆 998 年 1 月 1 日</dd>'
        '<dt>主題</dt><dd>Eberron / D&amp;D 戰役設定</dd><dt>密等</dt><dd>機密　探員限閱</dd></dl>'
        '<p class="lede">%s</p>'
        '<a class="open" href="#seven">翻開卷宗</a>'
        '</div>'
        '<div class="emboss" aria-hidden="true">王座堡</div>'
        '<div class="stamp big" aria-hidden="true">機密</div>'
        '</div>'
        '<nav class="tabheads" aria-label="各卷索引">%s</nav>'
        '</section>' % (esc(d["site_title_en"]), esc(d["tagline"]), heads)
    )
    raw('<div id="seven"></div>')
    things = "".join("<li><h3>%s%s</h3><p>%s</p></li>" % (esc(t["title"]), en(t["en"]), esc(t["body"]))
                     for t in d["seven_things"])
    sheet("致新任探員：該瞭解的七件事", "Seven Things to Know", '<ol class="seven">%s</ol>' % things,
          ref="卷宗封面 · 第一頁", lead=d["one_line"])
    themes = "".join("<h3>%s%s</h3>%s" % (esc(t["title"]), en(t["en"]), paras(t["body"])) for t in d["themes"])
    sheet("三大基調", None, themes, ref="卷宗封面 · 第二頁")
    facts = meta([(f["k"], esc(f["v"])) for f in d["quick_facts"]])
    months = ledger([("n", "月", True), ("name", "名稱", False)],
                    [{"n": str(i + 1), "name": esc(m)} for i, m in enumerate(d["calendar"]["months"])])
    coins = ledger([("coin", "硬幣", False), ("en", "原名", False), ("note", "說明", False)],
                   [{"coin": esc(c["coin"]), "en": en(c["en"]), "note": esc(c["note"])} for c in d["currency"]])
    sheet("速記：時間與錢", None,
          facts + "<h3>曆法</h3>" + paras(d["calendar"]["note"]) + months
          + "<p>一週七天依序為 %s。</p>" % esc("、".join(d["calendar"]["days"]))
          + "<h3>貨幣</h3>" + coins,
          ref="卷宗封面 · 第三頁", cls="wide")


# ---------------------------------------------------------------- 第一卷 歷史
def history():
    tabstrip("history")
    d = ui.load("history")
    sheet("第一卷　歷史", "History of Eberron", paras(d["creation_myth"]), ref="卷一 · 第一頁", cls="head",
          lead="一個由三條祖龍創造、被一場百年戰爭與一日浩劫定義的世界。")
    eras = "".join("<h3>%s%s</h3>%s" % (esc(e["era"]), en(e["en"]), paras(e["body"])) for e in d["eras"])
    sheet("五個時代", None, eras, ref="卷一 · 第二頁")
    sheet("年表", "Timeline", timeline(d["timeline"]), ref="卷一 · 第三頁", cls="wide")
    sheet("王座堡條約承認的十二國", "The Treaty of Thronehold",
          tags(d["treaty_nations"]["recognized"]) + "<p></p>" + paras(d["treaty_nations"]["note"]),
          ref="卷一 · 第四頁")
    scars = "".join("<h3>%s</h3>%s" % (esc(s["title"]), paras(s["body"])) for s in d["scars"])
    theories = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(t) for t in d["mourning_theories"])
    sheet("戰爭的傷痕", "The Scars of War", scars + "<h3>哀傷的成因：三種猜測</h3>" + theories
          + note("備註", "設定書把哀傷的真相留給 DM 決定。只要它仍是謎，對它的恐懼就壓著下一場戰爭。"),
          ref="卷一 · 第五頁", stamp="待查")


# ---------------------------------------------------------------- 第二卷 諸國
# 圖版一：科瓦雷全境示意。位置只表相對關係，非比例；名稱一律取自資料檔。
_PLATE_BOXES = {
    # en: (x, y, w, h)
    "Aundair": (140, 30, 116, 100), "Thrane": (266, 40, 104, 96), "Karrnath": (404, 16, 122, 120),
    "Breland": (140, 146, 180, 150), "Cyre (The Mournland)": (330, 150, 140, 110),
    "Demon Wastes": (16, 16, 110, 70), "Eldeen Reaches": (16, 96, 110, 100), "Droaam": (16, 206, 110, 90),
    "Shadow Marches": (16, 306, 110, 74), "Zilargo": (226, 306, 96, 74), "Darguun": (330, 270, 116, 80),
    "Valenar": (456, 290, 82, 90), "Q'barra": (548, 290, 76, 90), "Talenta Plains": (480, 220, 110, 60),
    "Mror Holds": (534, 146, 90, 64), "Lhazaar Principalities": (534, 16, 90, 120),
}
_PLATE_FONT = 'font-family="Noto Serif TC, serif"'
_PLATE_MONO = 'font-family="Courier Prime, monospace"'


def _plate_box(name, name_en, box, kind):
    """一個地區：kind 是 five（粗框）、treaty（實線）、free（虛線，未受承認）或 mourn（斜線）。"""
    x, y, w, h = box
    cx, cy = x + w / 2, y + h / 2
    if kind == "mourn":
        rect = ('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#hatch)" stroke="#b3261e" stroke-width="2.2"/>'
                '<rect x="%d" y="%d" width="%d" height="%d" fill="#fff" fill-opacity="0.72" stroke="none"/>'
                % (x, y, w, h, x, y, w, h))
        color = "#b3261e"
    else:
        stroke = {"five": 'stroke-width="2.2"', "treaty": 'stroke-width="1.2"', "free": 'stroke-width="1.2" stroke-dasharray="4 3"'}[kind]
        rect = '<rect x="%d" y="%d" width="%d" height="%d" fill="#fff" stroke="#16233f" %s/>' % (x, y, w, h, stroke)
        color = "#1d2b24"
    size = 15 if kind in ("five", "mourn") else 13.5
    en_color = "#b3261e" if kind == "mourn" else "#4b5a52"
    lines = [name_en]
    if len(name_en) * 6 > w - 8 and " " in name_en:  # 原名放不下就在最靠中間的空格折成兩行
        i = min((abs(j - len(name_en) / 2), j) for j, ch in enumerate(name_en) if ch == " ")[1]
        lines = [name_en[:i], name_en[i + 1:]]
    zh_y = cy - 1 if len(lines) == 1 else cy - 7
    label = ['<text x="%.0f" y="%.0f" font-size="%s" font-weight="700" fill="%s" text-anchor="middle">%s</text>'
             % (cx, zh_y, size, color, esc(name))]
    for k, line in enumerate(lines):
        label.append('<text x="%.0f" y="%.0f" font-size="10" fill="%s" text-anchor="middle" %s>%s</text>'
                     % (cx, zh_y + 15 + k * 12, en_color, _PLATE_MONO, esc(line)))
    return rect + "".join(label)


def _khorvaire_plate(d):
    parts = [
        '<svg viewBox="0 0 640 432" role="img" aria-label="科瓦雷十六個地區的相對位置示意圖">',
        '<defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">',
        '<line x1="0" y1="0" x2="0" y2="8" stroke="#b3261e" stroke-width="2" opacity="0.5"/></pattern></defs>',
        '<rect x="0" y="0" width="640" height="432" fill="#f4f5f2"/>',
        '<g %s>' % _PLATE_FONT,
    ]
    for n in d["five_nations"]:
        kind = "mourn" if n["en"].startswith("Cyre") else "five"
        parts.append(_plate_box(n["name"], n["en"], _PLATE_BOXES[n["en"]], kind))
    for r in d["regions"]:
        parts.append(_plate_box(r["name"], r["en"], _PLATE_BOXES[r["en"]], "treaty" if r.get("treaty") else "free"))
    t = d["thronehold"]
    parts.append('<text x="312" y="286" font-size="12" fill="#1d2b24" text-anchor="end">薩恩 Sharn ◆</text>')
    parts.append('<circle cx="387" cy="44" r="5" fill="#16233f"/>')
    parts.append('<text x="16" y="402" font-size="11.5" fill="#1d2b24">● %s %s（傳承海峽中的島，條約簽署地）</text>' % (esc(t["name"]), esc(t["en"])))
    parts.append('<text x="16" y="420" font-size="11.5" fill="#4b5a52">粗框：五國　實線：王座堡條約承認　虛線：未受承認　斜線：哀傷故地</text>')
    parts.append('</g></svg>')
    return plate("一", "科瓦雷全境示意，非比例。中央粗框是五國，賽爾已成哀傷故地；周圍八個實線地區是王座堡條約承認的國家，"
                 "虛線的卓姆、陰影濕地、惡魔荒原沒有受承認的政府。", "".join(parts))


def _seat_line(r):
    """帳冊裡地區名下方的首府一行。"""
    if not r.get("seat") or r["seat"] == "無":
        return '<span class="seat">首府　無</span>'
    return '<span class="seat">首府　%s%s</span>' % (esc(r["seat"]), en(r.get("seat_en")))


def nations():
    tabstrip("nations")
    d = ui.load("nations")
    khorvaire_map = photo("map-khorvaire.jpg", "科瓦雷全圖，尋路者基金會審度，王國曆 998 年。點開看大圖。",
                          "科瓦雷大陸地圖：五國、周邊各地區、海洋與主要城市", full="map-khorvaire-full.jpg", label="附圖")
    sheet("第二卷　科瓦雷諸國", "Nations of Khorvaire", paras(d["intro"]) + khorvaire_map + _khorvaire_plate(d),
          ref="卷二 · 第一頁", cls="head", lead="從同一個王國分裂出來的五國，加上戰爭中誕生的鄰居。")
    for i, n in enumerate(d["five_nations"], start=2):
        m = meta([
            ("首都", term(n["capital"], n["capital_en"])),
            ("統治者", esc(n["ruler"])),
            ("信仰", esc(n["faith"])),
            ("特色", tags(n["traits"])),
        ])
        sites = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(s) for s in n["sites"])
        body = (m + paras(n["body"]) + note("戰爭餘波", n["war_scar"]) + note("紀事", n["hook"])
                + "<h3>城市與地標</h3>" + sites)
        sheet(n["name"], n["en"], body, ref="卷二 · 第 %d 頁" % i, lead=n["one_line"],
              stamp="已消失" if n["en"].startswith("Cyre") else None)
    t = d["thronehold"]
    sheet(t["name"], t["en"], paras(t["body"]), ref="卷二 · 第七頁")
    regions = ledger([("name", "地區", False), ("treaty", "王座堡條約", False), ("line", "一句話", False)],
                     [{"name": term(r["name"], r["en"]) + _seat_line(r),
                       "treaty": "承認" if r.get("treaty") else "未承認",
                       "line": esc(r["line"])} for r in d["regions"]])
    sheet("其他區域", "Beyond the Five Nations",
          paras("王座堡條約承認十二個國家：五國中尚存的四國，加上這裡的達貢、埃魯登原野、拉札爾聯邦、摩洛領、夸巴拉、塔蘭塔平原、維倫娜、吉拉哥。"
                "卓姆自立為國但未獲承認，陰影濕地與惡魔荒原沒有統一政府，哀傷故地則已無人主張。") + regions,
          ref="卷二 · 第八頁", cls="wide")
    far = ledger([("name", "遠方諸地", False), ("line", "一句話", False)],
                 [{"name": term(r["name"], r["en"]), "line": esc(r["line"])} for r in d["far_lands"]])
    sheet("遠方諸地", "Distant Lands", far, ref="卷二 · 第九頁", cls="wide")


# ---------------------------------------------------------------- 第三卷 薩恩
def _sharn_plate():
    """圖版二：薩恩剖面示意。天城區浮在雲上，塔身分上／中／下三個層區，齒輪區在地底，邊沿崖區沿匕首河的崖壁。"""
    ink, indigo, soft = "#1d2b24", "#16233f", "#4b5a52"
    parts = [
        '<svg viewBox="0 0 640 400" role="img" aria-label="薩恩城的垂直剖面示意圖：上中下三個層區、天城區、齒輪區與邊沿崖區">',
        '<defs><pattern id="cogs" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">',
        '<line x1="0" y1="0" x2="0" y2="8" stroke="#16233f" stroke-width="1.4" opacity="0.35"/></pattern></defs>',
        '<rect x="0" y="0" width="640" height="400" fill="#f4f5f2"/>',
        '<g %s>' % _PLATE_FONT,
        # 地底：齒輪區
        '<rect x="0" y="312" width="500" height="62" fill="url(#cogs)"/>',
        '<line x1="0" y1="310" x2="500" y2="310" stroke="%s" stroke-width="2"/>' % indigo,
        '<text x="250" y="343" font-size="13.5" font-weight="700" fill="%s" text-anchor="middle">齒輪區</text>' % ink,
        '<text x="250" y="357" font-size="10" fill="%s" text-anchor="middle" %s>The Cogs</text>' % (soft, _PLATE_MONO),
        # 崖壁與匕首河
        '<line x1="500" y1="310" x2="500" y2="352" stroke="%s" stroke-width="2"/>' % indigo,
        '<path d="M504 354 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="%s" stroke-width="1.4"/>' % indigo,
        '<path d="M504 366 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="%s" stroke-width="1.2" opacity="0.6"/>' % indigo,
        '<text x="572" y="388" font-size="12" font-weight="700" fill="%s" text-anchor="middle">匕首河</text>' % ink,
        '<text x="572" y="399" font-size="9.5" fill="%s" text-anchor="middle" %s>Dagger River</text>' % (soft, _PLATE_MONO),
        # 邊沿崖區：崖壁上的平台與升降索
        '<line x1="494" y1="240" x2="494" y2="346" stroke="%s" stroke-width="1" stroke-dasharray="2 3"/>' % indigo,
        '<rect x="482" y="262" width="20" height="6" fill="#fff" stroke="%s" stroke-width="1.2"/>' % indigo,
        '<rect x="482" y="296" width="20" height="6" fill="#fff" stroke="%s" stroke-width="1.2"/>' % indigo,
        '<rect x="482" y="330" width="20" height="6" fill="#fff" stroke="%s" stroke-width="1.2"/>' % indigo,
        '<text x="510" y="292" font-size="12" font-weight="700" fill="%s">邊沿崖區</text>' % ink,
        '<text x="510" y="305" font-size="9.5" fill="%s" %s>Cliffside</text>' % (soft, _PLATE_MONO),
        # 層區分界（虛線）與左側標籤
        '<line x1="60" y1="140" x2="500" y2="140" stroke="%s" stroke-width="1" stroke-dasharray="5 4"/>' % indigo,
        '<line x1="60" y1="225" x2="500" y2="225" stroke="%s" stroke-width="1" stroke-dasharray="5 4"/>' % indigo,
    ]
    for label, en_label, y in (("上層區", "Upper", 96), ("中層區", "Middle", 182), ("下層區", "Lower", 266)):
        parts.append('<text x="8" y="%d" font-size="13.5" font-weight="700" fill="%s">%s</text>' % (y, ink, label))
        parts.append('<text x="8" y="%d" font-size="9.5" fill="%s" %s>%s</text>' % (y + 13, soft, _PLATE_MONO, en_label))
    # 塔：底寬、頂窄的梯形，內有樓層線
    towers = [(80, 64, 150), (170, 92, 60), (290, 70, 110), (390, 84, 180)]
    for x, w, top in towers:
        parts.append('<polygon points="%d,310 %d,310 %d,%d %d,%d" fill="#fff" stroke="%s" stroke-width="1.6"/>'
                     % (x, x + w, x + w - 5, top, x + 5, top, indigo))
        y = top + 34
        while y < 300:
            parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8" opacity="0.35"/>'
                         % (x + 5, y, x + w - 5, y, indigo))
            y += 34
    # 塔間橋樑
    for x1, x2, y in ((144, 170, 200), (262, 290, 120), (262, 290, 250), (360, 390, 205), (474, 494, 262)):
        parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.4"/>' % (x1, y, x2, y, indigo))
    # 天城區：固化雲朵上的浮島
    parts.append('<ellipse cx="216" cy="34" rx="48" ry="11" fill="#fff" stroke="%s" stroke-width="1.2"/>' % indigo)
    parts.append('<rect x="200" y="18" width="14" height="10" fill="#fff" stroke="%s" stroke-width="1"/>' % indigo)
    parts.append('<rect x="220" y="14" width="10" height="14" fill="#fff" stroke="%s" stroke-width="1"/>' % indigo)
    parts.append('<ellipse cx="334" cy="52" rx="34" ry="9" fill="#fff" stroke="%s" stroke-width="1.2"/>' % indigo)
    parts.append('<rect x="326" y="38" width="12" height="9" fill="#fff" stroke="%s" stroke-width="1"/>' % indigo)
    parts.append('<text x="384" y="38" font-size="12" font-weight="700" fill="%s">天城區</text>' % ink)
    parts.append('<text x="384" y="51" font-size="9.5" fill="%s" %s>Skyway</text>' % (soft, _PLATE_MONO))
    parts.append('<text x="8" y="392" font-size="11.5" fill="%s">虛線：層區分界　斜線：地底的齒輪區　橫槓：塔間的橋樑</text>' % soft)
    parts.append('</g></svg>')
    return plate("二", "薩恩剖面示意，非比例。海拔就是階級：天城區浮在固化的雲上，每座塔分成上、中、下三個層區，"
                 "齒輪區在地底，邊沿崖區沿著匕首河的崖壁而建。", "".join(parts))


def sharn():
    tabstrip("sharn")
    d = ui.load("sharn")
    sheet("第三卷　眾塔之城薩恩", "Sharn, the City of Towers", paras(d["body"]), ref="卷三 · 第一頁", cls="head",
          lead=d["one_line"])
    sheet("垂直的城市", "Wards of Sharn", paras(d["vertical"]) + _sharn_plate(), ref="卷三 · 第二頁")
    quarters = ledger([("name", "大區", False), ("character", "性格", False)],
                      [{"name": term(q["name"], q["en"]), "character": esc(q["character"])} for q in d["quarters"]])
    above = ledger([("name", "區域", False), ("line", "說明", False)],
                   [{"name": term(a["name"], a["en"]), "line": esc(a["line"])} for a in d["above_below"]])
    sheet("五個大區，加上天上與地下", None, quarters + "<h3>城市上空與地底</h3>" + above,
          ref="卷三 · 第三頁", cls="wide")
    moves = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(g) for g in d["getting_around"])
    sheet("怎麼在薩恩移動", "Getting Around", moves, ref="卷三 · 第四頁")
    faces = ledger([("name", "勢力", False), ("line", "一句話", False)],
                   [{"name": term(f["name"], f["en"]), "line": esc(f["line"])} for f in d["faces"]])
    sheet("薩恩的面孔", None, faces + note("戰爭的痕跡", d["war_marks"]), ref="卷三 · 第五頁", cls="wide")


# ---------------------------------------------------------------- 第四卷 龍紋家族
def houses():
    tabstrip("houses")
    d = ui.load("houses")
    sheet("第四卷　龍紋家族", "Dragonmarked Houses", paras(d["intro"]), ref="卷四 · 第一頁", cls="head",
          lead="十二個靠皮膚上的印記壟斷大陸經濟的家族。")
    marks = ledger([("mark", "龍紋", False), ("house", "家族", False), ("race", "血脈", False), ("business", "專擅公會", False)],
                   [{"mark": term(m["mark"], m["mark_en"]), "house": term(m["house"], m["house_en"]),
                     "race": esc(m["race"]), "business": esc(m["business"])} for m in d["marks"]])
    sheet("十二龍紋與其家族", "Dragonmarks and Their Houses", marks, ref="卷四 · 第二頁", cls="wide")
    a = d["aberrant"]
    sheet(a["name"], a["en"], paras(a["body"]), ref="卷四 · 第三頁", stamp="警戒")
    facts = meta([(f["k"], esc(f["v"])) for f in d["facts"]])
    sheet("家族常識", "All about the Houses", facts, ref="卷四 · 第四頁")
    sheet("戰爭與家族", "The Houses in the War", paras(d["war"]) + note("摩擦", d["tension"]), ref="卷四 · 第五頁")


# ---------------------------------------------------------------- 第五卷 種族
def races():
    tabstrip("races")
    d = ui.load("races")
    sheet("第五卷　種族", "Races of Eberron", paras(d["intro"]), ref="卷五 · 第一頁", cls="head",
          lead="四個只有艾伯倫才有的種族，以及熟悉種族的新位置。")
    for i, r in enumerate(d["races"], start=2):
        body = paras(r["body"]) + note("扮演提示", r["play"]) + "<h3>常見名字</h3>" + tags(r["names"])
        sheet(r["name"], r["en"], body, ref="卷五 · 第 %d 頁" % i, lead=r["tagline"])
    others = ledger([("name", "種族", False), ("line", "在艾伯倫的位置", False)],
                    [{"name": esc(o["name"]), "line": esc(o["line"])} for o in d["others"]])
    sheet("熟悉的種族，不同的位置", None, others, ref="卷五 · 第六頁", cls="wide")
    a = d["artificer"]
    sheet(a["name"], a["en"], paras(a["body"]), ref="卷五 · 第七頁")


# ---------------------------------------------------------------- 第六卷 信仰與組織
def faiths():
    tabstrip("faiths")
    f = ui.load("faiths")
    o = ui.load("orgs")
    sheet("第六卷　信仰與組織", "Faiths and Factions", paras(f["intro"]), ref="卷六 · 第一頁", cls="head",
          lead="諸神不顯聖，所以信仰靠人撐；真正下棋的是暗處的組織。")
    god_cols = [("name", "神祇", False), ("portfolio", "神職", False), ("symbol", "常見聖徽", False)]
    sh = f["sovereign_host"]
    gods = ledger(god_cols, [{"name": term(g["name"], g["en"]), "portfolio": esc(g["portfolio"]),
                              "symbol": esc(g["symbol"])} for g in sh["gods"]])
    sheet(sh["name"], sh["en"], paras(sh["body"]) + gods, ref="卷六 · 第二頁", cls="wide")
    ds = f["dark_six"]
    six = ledger(god_cols, [{"name": term(g["name"], g["en"]), "portfolio": esc(g["portfolio"]),
                             "symbol": esc(g["symbol"])} for g in ds["gods"]])
    sheet(ds["name"], ds["en"], paras(ds["body"]) + six, ref="卷六 · 第三頁", cls="wide")
    others = "".join("<h3>%s%s</h3>%s%s" % (esc(x["name"]), en(x["en"]),
                                            meta([("神職", esc(x["portfolio"])), ("聖徽", esc(x["symbol"]))]),
                                            paras(x["body"])) for x in f["other_faiths"])
    sheet("其他信仰", "Other Faiths", others, ref="卷六 · 第四頁")
    sheet("組織", "Factions", paras(o["intro"]), ref="卷六 · 第五頁", cls="head")
    stamps = {"The Lords of Dust": "機密", "The Dreaming Dark": "機密", "The Order of the Emerald Claw": "通緝",
              "The Aurum": "機密", "The Boromar Clan": "備查", "The Tyrants": "機密", "The King's Citadel": "機密"}
    for i, org in enumerate(o["orgs"], start=6):
        body = (meta([("性質", esc(org["kind"])), ("對手", esc(org["rival"]))]) + paras(org["summary"])
                + note("為什麼難纏", org["why"]) + note("冒險引子", org["hook"]))
        sheet(org["name"], org["en"], body, ref="卷六 · 第 %d 頁" % i, stamp=stamps.get(org["en"]))
    p = o["patrons"]
    sheet(p["title"], p["en"], paras(p["body"]), ref="卷六 · 第十三頁")


# ---------------------------------------------------------------- 第七卷 位面
def planes():
    tabstrip("planes")
    d = ui.load("planes")
    sheet("第七卷　存在位面", "Planes of Existence", paras(d["intro"]), ref="卷七 · 第一頁", cls="head",
          lead="十三個環繞艾伯倫、時近時遠的位面，以及它們滲進世界的地方。")
    rows = [{"name": term(p["name"], p["en"]), "epithet": esc(p["epithet"]), "summary": esc(p["summary"])}
            for p in d["planes"]]
    sheet("十三位面", "Tour of the Planes",
          ledger([("name", "位面", False), ("epithet", "稱號", False), ("summary", "一句話", False)], rows),
          ref="卷七 · 第二頁", cls="wide")
    sheet("宇宙觀備註", None, paras(d["cosmology_note"]) + "<h3>月亮</h3>" + paras(d["moons"]), ref="卷七 · 第三頁")


# ---------------------------------------------------------------- 附錄
def _zh_stamp(x):
    """譯本狀態章：有譯本／無譯本／待查（社群譯本無法確認時不下斷言）。"""
    status = x.get("zh_status") or ("ok" if x["zh_available"] else "no")
    return ui.stamp_inline({"ok": "有譯本", "no": "無譯本", "tbd": "待查"}[status], status)


def appendix():
    tabstrip("appendix")
    d = ui.load("appendix")
    g = ui.load("glossary")
    t = d["player_tips"]
    sheet("附錄", "Appendix", paras(t["intro"]), ref="附錄 · 第一頁", cls="head", lead="建角提示、官方書目、術語表。")
    tips = "".join("<h3>%s</h3>%s" % (esc(x["title"]), paras(x["body"])) for x in t["tips"])
    sheet("給玩家的建角提示", "Character Tips", tips, ref="附錄 · 第二頁")
    b = d["books"]
    rows = []
    for x in b["items"]:
        zh = esc(x["zh"]) if x["zh"] else ""
        rows.append({"title": "<strong>%s</strong>%s" % (esc(x["title"]), ("<br>" + zh) if zh else ""),
                     "year": esc(x["year"]), "edition": esc(x["edition"]),
                     "zh": _zh_stamp(x),
                     "note": esc(x["note"])})
    books = ledger([("title", "書名", False), ("year", "年份", True), ("edition", "版本", False), ("zh", "中文", False), ("note", "說明", False)], rows)
    links = "<ul>%s</ul>" % "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a>：%s</li>'
                                    % (esc(l["url"]), esc(l["label"]), esc(l["note"])) for l in b["links"])
    sheet("官方書目與延伸閱讀", "Bibliography", paras(b["intro"]) + books + "<h3>延伸連結</h3>" + links,
          ref="附錄 · 第三頁", cls="wide")
    query = st.text_input("查術語", placeholder="輸入中文或英文，例如：龍紋、Sharn", label_visibility="visible")
    q = (query or "").strip().lower()
    terms = [x for x in g["terms"] if not q or q in x["zh"].lower() or q in x["en"].lower()]
    items = "".join('<div>%s<span class="en">%s</span></div>' % (esc(x["zh"]), esc(x["en"])) for x in terms)
    sheet("術語表", "Glossary", "<p>%s 共 %d 個詞。</p>" % (esc(g["intro"]), len(terms)) + '<div class="glossary">%s</div>' % items,
          ref="附錄 · 第四頁", cls="wide")
    sheet("關於本站", None, paras(d["about"]), ref="附錄 · 第五頁")
