# -*- coding: utf-8 -*-
"""重建 data/glossary.json：只收各卷資料裡明確成對的「中文名／英文原名」欄位，再加上一份手寫的補充名詞。
時代標題（era）與卷名、篇名不是名詞，不收。用法：python tools/build_glossary.py"""
import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
FIELD_PAIRS = [("name", "en"), ("mark", "mark_en"), ("house", "house_en"), ("capital", "capital_en"), ("title", "en")]
SKIP_FILES = {"glossary", "appendix", "overview"}  # overview 的 title 對是卷名，不是名詞
SKIP_EN = {"Seven Things to Know"}
EXTRA = [
    ("科瓦雷", "Khorvaire"), ("伽利法王國", "Kingdom of Galifar"), ("王座堡條約", "Treaty of Thronehold"), ("終末戰爭", "The Last War"),
    ("哀傷日", "Day of Mourning"), ("哀傷故地", "The Mournland"), ("死灰迷霧", "Dead-gray mist"), ("五國", "Five Nations"),
    ("閃電列車", "Lightning rail"), ("飛艇", "Airship"), ("元素航船", "Elemental galleon"), ("魔匠師", "Magewright"), ("奇械師", "Artificer"),
    ("龍晶", "Dragonshard"), ("幻紡", "Glamerweave"), ("永明提燈", "Everbright lantern"), ("顯能區", "Manifest zone"), ("西伯瑞斯之環", "Ring of Siberys"),
    ("巨龍預言", "Draconic Prophecy"), ("密閣", "The Chamber"), ("影閣", "Shadow Cabinet"), ("蒙啟者", "Inspired"), ("夢靈", "Quori"),
    ("國王堡壘", "King's Citadel"), ("國王暗燈", "Dark Lanterns"), ("十二學會", "The Twelve"), ("寇斯敕令", "Korth Edicts"), ("西伯瑞斯測驗", "Test of Siberys"),
    ("剝皮者", "Excoriate"), ("棄兒", "Foundling"), ("六十豪門", "The Sixty"), ("薩恩警衛", "Sharn Watch"), ("空中客車", "Skycoach"),
    ("齒輪區", "The Cogs"), ("天城區", "Skyway"), ("莫格雷夫大學", "Morgrave University"), ("薩恩探事報", "Sharn Inquisitive"), ("柯蘭堡紀事報", "Korranberg Chronicle"),
    ("魔君", "Overlord"), ("羽蛇", "Couatl"), ("羅剎", "Rakshasa"), ("刀鋒領主", "Lord of Blades"), ("罪髓女士", "Lady Illmarrow"),
    ("護門者", "Gatekeepers"), ("達坎帝國", "Dhakaani Empire"), ("創生鍛爐", "Creation forge"), ("戰俑泰坦", "Warforged titan"), ("王國曆", "Year of the Kingdom (YK)"),
    ("阿卡尼克斯", "Arcanix"), ("雷肯馬克學院", "Rekkenmark Academy"), ("新賽爾", "New Cyre"), ("梅綽", "Metrol"), ("銀焰堡", "Flamekeep"),
    ("尋者", "Seeker (Blood of Vol)"), ("光明之道", "Path of Light"), ("異變魔", "Daelkyr"), ("異種龍紋", "Aberrant dragonmark"), ("龍紋戰爭", "War of the Mark"),
    ("哈拉斯·塔卡南", "Halas Tarkanan"), ("瘟疫女士", "Lady of the Plague"), ("索剌卡特剌", "Sora Katra"), ("龍血（毒品）", "Dragon's Blood"),
    ("夢百合", "Dreamlily"), ("赫拉賈克", "Hrazhak"), ("刃紋傭兵", "Blademarks"), ("亞貢斯", "Argonth"), ("薩利奧斯特", "Thaliost"),
    ("沙杜卡", "Shadukar"), ("蘿恩女王", "Queen Wroann"), ("伊爾泰恩家族", "ir'Tain family"),
    ("蒂拉·邁倫", "Tira Miron"), ("貝·舍盧", "Bel Shalor"), ("羅·睹契室", "Rak Tulkhesh"), ("蘇·珂帝室", "Sul Khatesh"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pairs = {}
    by_field = {}

    def add(zh, en, src, field):
        if isinstance(zh, str) and isinstance(en, str) and zh.strip() and en.strip() and en.strip() not in SKIP_EN:
            key = en.strip().lower()  # 同一個原名只收一次，大小寫不同視為同一個詞
            if key not in pairs:
                pairs[key] = (zh.strip(), en.strip(), src)
                by_field.setdefault(field, []).append((zh.strip(), en.strip(), src))

    def walk(x, src):
        if isinstance(x, dict):
            for a, b in FIELD_PAIRS:
                if a in x and b in x:
                    add(x[a], x[b], src, a)
            for v in x.values():
                walk(v, src)
        elif isinstance(x, list):
            for v in x:
                walk(v, src)

    for f in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        name = os.path.basename(f)[:-5]
        if name in SKIP_FILES:
            continue
        with io.open(f, encoding="utf-8") as fh:
            walk(json.load(fh), name)
    for zh, en in EXTRA:
        add(zh, en, "extra", "extra")
    rows = sorted(({"zh": zh, "en": en, "src": src} for zh, en, src in pairs.values()), key=lambda r: r["en"].lower())
    out = os.path.join(DATA, "glossary.json")
    with io.open(out, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"intro": "全站專有名詞對照，依英文原名排序。", "terms": rows}, ensure_ascii=False, indent=1))
    print("術語數:", len(rows))
    for field, items in by_field.items():
        print("[%s] %d 條" % (field, len(items)))
        if field == "title":
            for zh, en, src in items:
                print("   ", src, zh, "|", en)


if __name__ == "__main__":
    main()
