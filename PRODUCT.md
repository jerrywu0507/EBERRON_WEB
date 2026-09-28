# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Streamlit（Python），使用者指定。單一 Streamlit 應用、多頁式導覽、自訂 CSS 與網路字型；不引入前端框架。部署位置未定：使用者明確表示這是獨立網站，與實驗室網站無關，先在本機預覽。

## Users

公開的華語 D&D 社群讀者：對 D&D 5e 有基本認識、多半完全不認識艾伯倫（Eberron）的玩家與 DM。情境：開團前預習、評估這個設定值不值得跑、跑團中快速查一個名詞。手機與桌機都會用；不需登入，靠單一連結分享。

## Product Purpose

用繁體中文把艾伯倫這個「魔法即科技、通俗冒險、黑色陰謀」的 D&D 設定介紹給華語讀者，讓第一次接觸的人在十分鐘內抓到這個世界的形狀，並能循著附上的英文原名去找官方書。成功的樣子：讀者能說出艾伯倫和一般奇幻世界差在哪、知道五國與龍紋家族是什麼、知道自己能扮演什麼。

## Positioning

華語圈幾乎沒有系統性的艾伯倫繁中入門。本站沿用中文社群譯本（DND5eChm《艾伯倫：從終末戰爭中崛起》）已通行的譯名，每個專有名詞附英文原名，讀者能無縫接到官方英文資料，也和同一套譯名的怪物圖鑑對得上。這是導覽而不是百科：篇幅精簡、取捨明確、不是逐條翻譯。

## Operating Context

- 讀者常在手機上讀，也會在桌邊用桌機查名詞。
- 內容全部原創撰寫，以官方設定為事實依據；不轉載譯本全文，不使用官方地圖與插圖。
- 固定附錄：玩家建角提示與官方書目（英文原書名，並註明有無中文譯本）。

## Capabilities and Constraints

- 涵蓋主題（使用者確認「都要」）：世界觀與歷史年表；科瓦雷諸國與眾塔之城薩恩；龍紋家族與四個特有種族；信仰、組織與存在位面；附錄（建角提示、書目）。
- Streamlit 的版面限制：元件為區塊式直向流；自訂樣式靠注入 CSS；無法完全掌控 DOM，動態效果以 CSS 為主。
- 本次沒有影像生成工具：不會有生成插圖，視覺靠排版、色彩、幾何與文字。
- 譯名以譯本為準，例：科瓦雷 Khorvaire、薩恩 Sharn、安黛爾 Aundair、布蕾蘭 Breland、卡納斯 Karrnath、瑟雷恩 Thrane、賽爾 Cyre、哀傷故地 Mournland、王座堡 Thronehold、戰俑 Warforged、幻身靈 Changeling、化獸者 Shifter、離夢人 Kalashtar、天命諸神 Sovereign Host、黑暗六神 Dark Six、銀焰教會 Church of the Silver Flame、沃爾之血 Blood of Vol、不朽議庭 Undying Court、塵主 Lords of Dust、黑暗夢境 Dreaming Dark、翡翠利爪教團 Order of the Emerald Claw、金權會 Aurum。
- 推斷、待確認：語言採「繁體中文，專有名詞附英文原名」（使用者回答放置位置時未指定語言，依讀者是華語社群且需查官方書而推斷）。

## Brand Commitments

沒有既有品牌或標誌。站名暫定「艾伯倫導覽」，待定。艾伯倫本身的文化印記是設定事實而非視覺指令：閃電列車、飛空艇、眾塔之城、戰俑、龍紋、終末戰爭與哀傷日。

## Evidence on Hand

- 事實依據：中文譯本《艾伯倫：從終末戰爭中崛起》35 個章節頁的純文字（只作用語與事實對照，存於工作階段暫存區 `scratchpad/eberron_src_tw/`），以及抽出的術語對照表 `scratchpad/eberron_terms.tsv`（498 詞）。
- 沒有：官方插圖、地圖、任何可公開使用的圖像；沒有讀者數據、推薦語或使用量，不可捏造。

## Product Principles

1. 先給形狀再給細節：每一頁開頭一句話說清這是什麼，再展開。
2. 譯名可追溯：專有名詞第一次出現附英文原名。
3. 導覽不是百科：寧可少而清楚，不逐條堆砌。
4. 手機上也要好讀：內容在窄螢幕上不靠橫向表格存活。
5. 事實不捏造：不確定的設定事實寧可不寫。

## Accessibility & Inclusion

繁體中文讀者；文字對比至少達 WCAG AA；互動元件維持 Streamlit 原生鍵盤操作。
