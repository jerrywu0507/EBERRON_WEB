# -*- coding: utf-8 -*-
"""各卷的內容頁。每一頁是一個攤開的檔案夾，裡面夾著幾件不同格式的文件：先一句話說清是什麼，再展開。"""
import streamlit as st

from guide import ui
from guide.ui import (esc, en, term, paras, note, memos, meta, tags, ledger, plate, photo, polaroid, pinboard,
                      doc, form, card, attached, slip, bizcards, page, raw)

NUMS = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二", "十三"]


def tabstrip(current=""):
    links = "".join('<a href="./%s" style="%s"%s>%s</a>'
                    % (v["path"], ui.tab_vars(v["tab"]), ' aria-current="page"' if v["path"] == current else "", esc(v["title"]))
                    for v in ui.VOLUMES)
    raw('<nav class="tabstrip" aria-label="各卷">%s</nav>' % links)


def _bureau(vol, en_title):
    return ("王座堡卷宗 · %s" % vol, en_title)


# ---------------------------------------------------------------- 封面
def cover():
    tabstrip("")
    d = ui.load("overview")
    label = (
        '<div class="label">'
        '<p class="head">王座堡卷宗<span class="en">THRONEHOLD DOSSIER</span></p>'
        '<p class="div">戰役設定簡報 · 致新任探員</p>'
        '<h1 class="subject">艾伯倫<span class="en">%s</span></h1>'
        '<div class="meta"><span><b>檔號</b><i>998-YK-001</i></span><span><b>建檔</b><i>王國曆 998 年 1 月 1 日</i></span></div>'
        '</div>' % esc(d["site_title_en"]).upper()
    )
    raw(
        '<section class="cover" aria-label="卷宗封面">' + ui.BULLDOG
        + '<div class="foldertab" aria-hidden="true">EBERRON FILES · 艾伯倫檔案</div>' + label
        + '<p class="penned">%s</p>' % esc(d["tagline"])
        + '<div class="band"><span class="word">機密</span><span class="sub">探員限閱 · READ ONLY IF AUTHORIZED</span></div>'
        + '<a class="open" href="#docs">翻開卷宗 ▸</a>' + ui.paperclip("clip paper")
        + '</section><div id="docs"></div>'
    )
    things = [(NUMS[i], esc(t["title"]) + en(t["en"]), esc(t["body"])) for i, t in enumerate(d["seven_things"])]
    themes = "".join("<h3>%s%s</h3>%s" % (esc(t["title"]), en(t["en"]), paras(t["body"])) for t in d["themes"])
    months = ledger([("n", "月", True), ("name", "名稱", False)],
                    [{"n": str(i + 1), "name": esc(m)} for i, m in enumerate(d["calendar"]["months"])])
    coins = ledger([("coin", "硬幣", False), ("en", "原名", False), ("note", "說明", False)],
                   [{"coin": esc(c["coin"]), "en": en(c["en"]), "note": esc(c["note"])} for c in d["currency"]])
    page(
        form("致新任探員：該瞭解的七件事", "Seven Things to Know", lead=d["one_line"], log=things,
             no=("摘要單", "BRIEF-01"), ref="卷宗封面 · 第一頁"),
        doc("三大基調", "Three Themes", themes, ref="卷宗封面 · 第二頁", cls="cream punched", tilt=0.4),
        form("速記：時間與錢", "Time and Money", rows=[(f["k"], esc(f["v"])) for f in d["quick_facts"]],
             prose="<h3>曆法</h3>" + paras(d["calendar"]["note"]), table=months,
             foot="<p>一週七天依序為 %s。</p>" % esc("、".join(d["calendar"]["days"])) + coins,
             no=("速記單", "REF-02"), ref="卷宗封面 · 第三頁", tilt=-0.3),
    )


# ---------------------------------------------------------------- 第一卷 歷史
def history():
    tabstrip("history")
    d = ui.load("history")
    eras = "".join("<h3>%s%s</h3>%s" % (esc(e["era"]), en(e["en"]), paras(e["body"])) for e in d["eras"])
    timeline = [(it["year"], esc(it["label"]), esc(it["body"])) for it in d["timeline"]]
    scars = "".join("<h3>%s</h3>%s" % (esc(s["title"]), paras(s["body"])) for s in d["scars"])
    theories = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(t) for t in d["mourning_theories"])
    page(
        doc("第一卷　歷史", "History of Eberron", paras(d["creation_myth"]), ref="卷一 · 第一頁", cls="head punched",
            lead="一個由三條祖龍創造、被一場百年戰爭與一日浩劫定義的世界。", bureau=_bureau("第一卷", "HISTORY OF EBERRON")),
        doc("五個時代", "Five Ages", eras, ref="卷一 · 第二頁", cls="cream", tilt=0.5),
        form("年表", "Timeline", log=timeline, no=("事件記錄單", "LOG-01"), ref="卷一 · 第三頁", tilt=-0.4),
        doc("王座堡條約承認的十二國", "The Treaty of Thronehold",
            tags(d["treaty_nations"]["recognized"]) + "<p></p>" + paras(d["treaty_nations"]["note"]),
            ref="卷一 · 第四頁", tilt=0.3),
        doc("戰爭的傷痕", "The Scars of War", scars + note("備註", "設定書把哀傷的真相留給 DM 決定。只要它仍是謎，對它的恐懼就壓著下一場戰爭。", hand_written=True),
            ref="卷一 · 第五頁", cls="punched"),
        slip("哀傷的成因：三種猜測", "Theories of the Mourning", theories, stamp="待查"),
    )


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
    map_polaroid = polaroid(photo("map-khorvaire.jpg", "科瓦雷大陸地圖：五國、周邊各地區、海洋與主要城市", full="map-khorvaire-full.jpg"),
                            "科瓦雷全圖，尋路者基金會審度", typed="王國曆 998 年 · 點開看大圖", tilt=-1.4)
    plate_polaroid = polaroid(_khorvaire_plate(d), "科瓦雷示意，非比例；斜線是哀傷故地", typed="圖版一 · 粗框為五國、實線為條約承認", tilt=1.1)
    parts = [
        doc("第二卷　科瓦雷諸國", "Nations of Khorvaire", paras(d["intro"]), ref="卷二 · 第一頁", cls="head punched",
            lead="從同一個王國分裂出來的五國，加上戰爭中誕生的鄰居。", bureau=_bureau("第二卷", "NATIONS OF KHORVAIRE")),
        pinboard(map_polaroid, plate_polaroid),
    ]
    for i, n in enumerate(d["five_nations"], start=2):
        fields = [("首都", term(n["capital"], n["capital_en"])), ("統治者", esc(n["ruler"])),
                  ("信仰", esc(n["faith"])), ("特色", tags(n["traits"]))]
        sites = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(s) for s in n["sites"])
        body = (paras(n["body"]) + memos([("戰爭餘波", n["war_scar"]), ("紀事", n["hook"])])
                + "<h3>城市與地標</h3>" + sites)
        parts.append(card(n["name"], n["en"], fields, line=n["one_line"],
                          stamp="已消失" if n["en"].startswith("Cyre") else None, tilt=(-0.6, 0.5)[i % 2]))
        parts.append(attached(body, ref="卷二 · 第 %d 頁" % i))
    t = d["thronehold"]
    parts.append(doc(t["name"], t["en"], paras(t["body"]), ref="卷二 · 第七頁", cls="cream", tilt=0.4))
    regions = ledger([("name", "地區", False), ("treaty", "王座堡條約", False), ("line", "一句話", False)],
                     [{"name": term(r["name"], r["en"]) + _seat_line(r),
                       "treaty": "承認" if r.get("treaty") else "未承認",
                       "line": esc(r["line"])} for r in d["regions"]])
    parts.append(form("其他區域", "Beyond the Five Nations",
                      prose=paras("王座堡條約承認十二個國家：五國中尚存的四國，加上這裡的達貢、埃魯登原野、拉札爾聯邦、摩洛領、夸巴拉、塔蘭塔平原、維倫娜、吉拉哥。"
                                  "卓姆自立為國但未獲承認，陰影濕地與惡魔荒原沒有統一政府，哀傷故地則已無人主張。"),
                      table=regions, no=("地區清冊", "REG-01"), ref="卷二 · 第八頁"))
    parts.append(pinboard(polaroid(photo("map-world.jpg", "艾伯倫全球圖：科瓦雷、希恩德瑞克、艾倫諾、阿貢尼森、薩洛納與永冰極地"),
                                   "艾伯倫全球圖，西維斯家族刊行", typed="王國曆 998 年 · 科瓦雷以外的四塊大陸", tilt=-0.9)))
    far = [(None, term(r["name"], r["en"]), esc(r["line"])) for r in d["far_lands"]]
    parts.append(form("遠方諸地", "Distant Lands", log=far, plain_log=True, no=("地區清冊", "REG-02"), ref="卷二 · 第九頁", tilt=-0.3))
    page(*parts)


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
    quarters = ledger([("name", "大區", False), ("character", "性格", False)],
                      [{"name": term(q["name"], q["en"]), "character": esc(q["character"])} for q in d["quarters"]])
    above = bizcards([{"mark": None, "name": a["name"], "en": a["en"], "lines": [("說明", esc(a["line"]))]} for a in d["above_below"]], index=True)
    moves = memos(['<div class="memo tape hand">%s</div>' % esc(g) for g in d["getting_around"]])
    faces = bizcards([{"mark": None, "name": f["name"], "en": f["en"], "lines": [("一句話", esc(f["line"]))]} for f in d["faces"]])
    page(
        doc("第三卷　眾塔之城薩恩", "Sharn, the City of Towers",
            polaroid(photo("morgrave.jpg", "莫格雷夫大學的塔群，塔與塔之間以橋相連"), "莫格雷夫大學，孟西斯高地", typed="Morgrave University")
            + paras(d["body"]), ref="卷三 · 第一頁", cls="head punched",
            lead=d["one_line"], bureau=_bureau("第三卷", "SHARN, CITY OF TOWERS")),
        doc("垂直的城市", "Wards of Sharn", paras(d["vertical"]), ref="卷三 · 第二頁", tilt=0.4),
        pinboard(polaroid(photo("sharn-cross-section.jpg", "薩恩城剖面圖：天城區、上中下三個層區、齒輪區與熔池", full="sharn-cross-section-full.jpg"),
                          "薩恩剖面：從天城區到齒輪區", typed="西維斯家族刊行 · 點開看大圖", tilt=-1.0, tall=True),
                 polaroid(_sharn_plate(), "同一座城的示意，非比例", typed="圖版二", tilt=1.3)),
        form("五個大區", "Quarters of Sharn", table=quarters, no=("區域清冊", "SHN-01"), ref="卷三 · 第三頁"),
        pinboard(polaroid(photo("sharn-upper.jpg", "薩恩上層區地圖", full="sharn-upper.jpg"), "上層區：富人與掌權者", typed="Upper Wards · 點開看大圖", tilt=-1.4, small=True),
                 polaroid(photo("sharn-middle.jpg", "薩恩中層區地圖", full="sharn-middle.jpg"), "中層區：市場與酒館", typed="Middle Wards · 點開看大圖", tilt=0.8, small=True),
                 polaroid(photo("sharn-lower.jpg", "薩恩下層區地圖", full="sharn-lower.jpg"), "下層區：勞工、赤貧者與難民", typed="Lower Wards · 點開看大圖", tilt=-0.6, small=True), tilt=-0.4),
        doc("城市上空與地底", "Above and Below", above, ref="卷三 · 第四頁", cls="cream wide", tilt=-0.5),
        doc("怎麼在薩恩移動", "Getting Around",
            polaroid(photo("sharn-sky-battle.jpg", "空中飛艇上的追逐戰，滑翔者在塔間穿梭"), "塔與塔之間的空中追逐", typed="skycoach · 每層兩枚銀君幣")
            + moves, ref="卷三 · 第五頁", tilt=0.3),
        doc("薩恩的面孔", "Faces of Sharn", faces + note("戰爭的痕跡", d["war_marks"]), ref="卷三 · 第六頁", cls="wide punched"),
    )


# ---------------------------------------------------------------- 第四卷 龍紋家族
def houses():
    tabstrip("houses")
    d = ui.load("houses")
    marks = bizcards([{"mark": m["mark_en"].upper(), "name": m["house"], "en": m["house_en"],
                       "lines": [("龍紋", esc(m["mark"])), ("血脈", esc(m["race"])), ("專擅", esc(m["business"]))]} for m in d["marks"]])
    a = d["aberrant"]
    page(
        doc("第四卷　龍紋家族", "Dragonmarked Houses", paras(d["intro"]), ref="卷四 · 第一頁", cls="head punched",
            lead="十二個靠皮膚上的印記壟斷大陸經濟的家族。", bureau=_bureau("第四卷", "DRAGONMARKED HOUSES")),
        doc("十二龍紋與其家族", "Dragonmarks and Their Houses", marks, ref="卷四 · 第二頁", cls="wide cream"),
        slip(a["name"], a["en"], paras(a["body"]), stamp="警戒"),
        form("家族常識", "All about the Houses", rows=[(f["k"], esc(f["v"])) for f in d["facts"]],
             no=("備忘單", "HSE-01"), ref="卷四 · 第四頁", tilt=0.4),
        doc("戰爭與家族", "The Houses in the War", paras(d["war"]) + note("摩擦", d["tension"], hand_written=True),
            ref="卷四 · 第五頁", cls="punched", tilt=-0.3),
    )


# ---------------------------------------------------------------- 第五卷 種族
def races():
    tabstrip("races")
    d = ui.load("races")
    parts = [doc("第五卷　種族", "Races of Eberron", paras(d["intro"]), ref="卷五 · 第一頁", cls="head punched",
                 lead="四個只有艾伯倫才有的種族，以及熟悉種族的新位置。", bureau=_bureau("第五卷", "RACES OF EBERRON"))]
    portraits = {
        "Shifter": ("race-shifter.jpg", "甲板上的化獸者水手", "Shifter"),
        "Changeling": ("race-changeling.jpg", "鏡前的幻身靈：一張臉換過一張", "Changeling"),
        "Kalashtar": ("race-kalashtar.jpg", "離夢人，與身後的夢靈", "Kalashtar"),
    }
    for i, r in enumerate(d["races"], start=2):
        parts.append(card(r["name"], r["en"], [("常見名字", tags(r["names"]))], line=r["tagline"], tilt=(-0.5, 0.6)[i % 2]))
        pic = ""
        if r["en"] in portraits:
            src, cap, typed = portraits[r["en"]]
            pic = polaroid(photo(src, r["name"] + "的畫像"), cap, typed=typed)
        parts.append(attached(pic + paras(r["body"]) + note("扮演提示", r["play"], hand_written=True), ref="卷五 · 第 %d 頁" % i))
    others = [(None, esc(o["name"]), esc(o["line"])) for o in d["others"]]
    parts.append(form("熟悉的種族，不同的位置", "Familiar Races", log=others, plain_log=True, no=("種族清冊", "RCE-01"), ref="卷五 · 第六頁"))
    a = d["artificer"]
    parts.append(doc(a["name"], a["en"], paras(a["body"]), ref="卷五 · 第七頁", cls="cream", tilt=0.4))
    page(*parts)


# ---------------------------------------------------------------- 第六卷 信仰與組織
def faiths():
    tabstrip("faiths")
    f = ui.load("faiths")
    o = ui.load("orgs")
    god_cols = [("name", "神祇", False), ("portfolio", "神職", False), ("symbol", "常見聖徽", False)]
    sh, ds = f["sovereign_host"], f["dark_six"]
    gods = ledger(god_cols, [{"name": term(g["name"], g["en"]), "portfolio": esc(g["portfolio"]), "symbol": esc(g["symbol"])} for g in sh["gods"]])
    six = ledger(god_cols, [{"name": term(g["name"], g["en"]), "portfolio": esc(g["portfolio"]), "symbol": esc(g["symbol"])} for g in ds["gods"]])
    others = "".join("<h3>%s%s</h3>%s%s" % (esc(x["name"]), en(x["en"]),
                                            meta([("神職", esc(x["portfolio"])), ("聖徽", esc(x["symbol"]))]),
                                            paras(x["body"])) for x in f["other_faiths"])
    parts = [
        doc("第六卷　信仰與組織", "Faiths and Factions", paras(f["intro"]), ref="卷六 · 第一頁", cls="head punched",
            lead="諸神不顯聖，所以信仰靠人撐；真正下棋的是暗處的組織。", bureau=_bureau("第六卷", "FAITHS AND FACTIONS")),
        form(sh["name"], sh["en"], prose=paras(sh["body"]), table=gods, no=("名冊", "FTH-01"), ref="卷六 · 第二頁"),
        form(ds["name"], ds["en"], prose=paras(ds["body"]), table=six, no=("名冊", "FTH-02"), ref="卷六 · 第三頁", tilt=0.4),
        doc("其他信仰", "Other Faiths", others, ref="卷六 · 第四頁", cls="cream punched"),
        doc("組織", "Factions", paras(o["intro"]), ref="卷六 · 第五頁", cls="head", bureau=_bureau("第六卷 · 組織", "FACTIONS")),
    ]
    stamps = {"The Lords of Dust": "機密", "The Dreaming Dark": "機密", "The Order of the Emerald Claw": "通緝",
              "The Aurum": "機密", "The Boromar Clan": "備查", "The Tyrants": "機密", "The King's Citadel": "機密"}
    for i, org in enumerate(o["orgs"], start=6):
        parts.append(card(org["name"], org["en"], [("性質", esc(org["kind"])), ("對手", esc(org["rival"]))],
                          stamp=stamps.get(org["en"]), tilt=(-0.5, 0.4)[i % 2]))
        parts.append(attached(paras(org["summary"]) + memos([("為什麼難纏", org["why"]), ("冒險引子", org["hook"])]),
                              ref="卷六 · 第 %d 頁" % i))
    p = o["patrons"]
    parts.append(doc(p["title"], p["en"], paras(p["body"]), ref="卷六 · 第十三頁", tilt=0.3))
    page(*parts)


# ---------------------------------------------------------------- 第七卷 位面
def planes():
    tabstrip("planes")
    d = ui.load("planes")
    cards = bizcards([{"mark": p["epithet"], "name": p["name"], "en": p["en"], "lines": [("一句話", esc(p["summary"]))]} for p in d["planes"]], index=True)
    page(
        doc("第七卷　存在位面", "Planes of Existence", paras(d["intro"]), ref="卷七 · 第一頁", cls="head punched",
            lead="十三個環繞艾伯倫、時近時遠的位面，以及它們滲進世界的地方。", bureau=_bureau("第七卷", "PLANES OF EXISTENCE")),
        pinboard(polaroid(photo("planes-map.jpg", "諸位面地圖：十三個位面環繞著物質位面艾伯倫", full="planes-map-full.jpg"),
                          "諸位面地圖：十三個位面環著物質位面", typed="Exploring Eberron · 社群譯製 · 點開看大圖", tilt=-0.8, tall=True)),
        doc("十三位面", "Tour of the Planes", cards, ref="卷七 · 第二頁", cls="wide cream"),
        doc("宇宙觀備註", None, paras(d["cosmology_note"]) + "<h3>月亮</h3>" + paras(d["moons"]), ref="卷七 · 第三頁", cls="punched", tilt=-0.4),
    )


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
    tips = [(NUMS[i], esc(x["title"]), esc(x["body"])) for i, x in enumerate(t["tips"])]
    b = d["books"]
    rows = []
    for x in b["items"]:
        zh = esc(x["zh"]) if x["zh"] else ""
        rows.append({"title": "<strong>%s</strong>%s" % (esc(x["title"]), ("<br>" + zh) if zh else ""),
                     "year": esc(x["year"]), "edition": esc(x["edition"]), "zh": _zh_stamp(x), "note": esc(x["note"])})
    books = ledger([("title", "書名", False), ("year", "年份", True), ("edition", "版本", False), ("zh", "中文", False), ("note", "說明", False)], rows)
    links = "<ul>%s</ul>" % "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a>：%s</li>'
                                    % (esc(l["url"]), esc(l["label"]), esc(l["note"])) for l in b["links"])
    page(
        doc("附錄", "Appendix", paras(t["intro"]), ref="附錄 · 第一頁", cls="head punched", lead="建角提示、官方書目、術語表。",
            bureau=_bureau("附錄", "APPENDIX")),
        form("給玩家的建角提示", "Character Tips", log=tips, no=("建角單", "APP-01"), ref="附錄 · 第二頁"),
        doc("官方書目與延伸閱讀", "Bibliography", paras(b["intro"]) + books + "<h3>延伸連結</h3>" + links, ref="附錄 · 第三頁", cls="wide cream", tilt=0.3),
        part="top",
    )
    query = st.text_input("查術語", placeholder="輸入中文或英文，例如：龍紋、Sharn", label_visibility="visible")
    q = (query or "").strip().lower()
    terms = [x for x in g["terms"] if not q or q in x["zh"].lower() or q in x["en"].lower()]
    items = "".join('<div>%s<span class="en">%s</span></div>' % (esc(x["zh"]), esc(x["en"])) for x in terms)
    page(
        doc("術語表", "Glossary", "<p>%s 共 %d 個詞。</p>" % (esc(g["intro"]), len(terms)) + '<div class="glossary">%s</div>' % items,
            ref="附錄 · 第四頁", cls="wide"),
        doc("關於本站", None, paras(d["about"]), ref="附錄 · 第五頁", cls="cream", tilt=0.4),
        part="bottom",
    )
