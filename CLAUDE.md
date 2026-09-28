# 艾伯倫導覽（Eberron Guide）— 交接說明

給接手這個專案的 Claude Code（或任何人）。這份文件記錄專案是什麼、做到哪裡、怎麼跑、改東西的規則，以及還沒決定的事。內容以 2026-09-28 的狀態為準。

## 這是什麼

- 用 Streamlit 1.64 做的**獨立網站**，以繁體中文向華語 D&D 社群介紹《龍與地下城》的艾伯倫（Eberron）戰役設定。九個頁面：卷宗封面、第一卷歷史、第二卷諸國、第三卷薩恩、第四卷龍紋家族、第五卷種族、第六卷信仰與組織、第七卷位面、附錄（建角提示、書目、171 條中英術語表）。
- 它**與使用者的實驗室網站無關**（不要接進 Caddy 或實驗室首頁），目前只在本機 http://127.0.0.1:8509/ 預覽，站名、網域與主機都還沒決定。
- 使用者的固定要求：**回覆一律用繁體中文**；譯名沿用中文社群譯本（DND5eChm《艾伯倫：從終末戰爭中崛起》）；每個專有名詞附英文原名。
- 產品定義在 [PRODUCT.md](PRODUCT.md)，設計系統在 [DESIGN.md](DESIGN.md)（及 `.impeccable/design.json`）。改視覺前先讀 DESIGN.md，它是建好之後從程式碼反推記錄的，是權威。

## 怎麼在新電腦跑起來

需要 Python 3.12 與 Google Chrome（截圖工具用；不截圖可不裝）。`.venv` 內含絕對路徑，**不要搬舊的 .venv，重建即可**：

```powershell
cd <專案資料夾>
.\setup_env.ps1          # 建 .venv 並安裝 requirements.txt（streamlit、opencc、websocket-client、pillow）
.\start_streamlit.ps1    # 前景啟動，http://127.0.0.1:8509/
.\restart_streamlit.ps1  # 關掉 8509 上的舊程序後以隱藏視窗重啟
```

健康檢查：`http://127.0.0.1:8509/_stcore/health` 回 `ok`。主題在 [.streamlit/config.toml](.streamlit/config.toml)；連接埠與位址寫在 `start_streamlit.ps1` 的啟動參數（config.toml 不放 server.address/port，雲端部署時由平台決定）。開機不會自動啟動。

注意：Windows PowerShell 5.1 讀含中文的 `.ps1` 需要 UTF-8 BOM；現有三個腳本都是純 ASCII，可直接跑。

## 檔案結構

| 路徑 | 內容 |
|---|---|
| `app.py` | 入口：`st.set_page_config`、依 `ui.VOLUMES` 建 `st.Page`、`st.navigation`、注入 CSS |
| `guide/ui.py` | 共用零件：`VOLUMES`（各卷標題／網址／標籤色／篇幅權重）、`load()`（快取 JSON）、`inject_css()`（樣式＋標籤軌逐卷規則＋印泥 SVG 濾鏡 `INK_FILTERS`）、`sheet/meta/tags/ledger/timeline/note/plate/stamp_inline/term/en/paras` |
| `guide/pages.py` | 九個頁面函式、行動版標籤列 `tabstrip(current)`、圖版一 `_khorvaire_plate()`（手繪 SVG 科瓦雷全境示意，16 地區＋王座堡） |
| `assets/styles.css` | 整站樣式（色票 token、封面、印章、用箋、標籤軌、帳冊、年表、圖版、手機斷點 900px、減少動態） |
| `static/fonts/`、`static/paper-grain.png` | 自帶字型子集（思源宋體 400/600/900、Courier Prime）與紙紋貼圖；`config.toml` 開了 `enableStaticServing`，網址是 `/app/static/...` |
| `tools/build_fonts.py` | 重建字型子集（需 `pip install fonttools brotli`；原始 OTF 會下載到 `~/.cache/eberron-fonts/`） |
| `assets/favicon.png` | 自製網站圖示（靛藍卷宗＋朱印） |
| `data/*.json` | 全部文字內容：overview、history、nations、sharn、houses、races、faiths、orgs、planes、appendix、glossary |
| `tools/build_glossary.py` | 從各卷資料的中英成對欄位＋內建補充清單重建 `data/glossary.json`（**不要手改 glossary.json**） |
| `tools/snap.py` | 用 Chrome DevTools 協定截整頁／查 DOM：`snap.py shot <url> <out.png> <width> [mobile]`、`snap.py dom <url> "<js>"`。檔頭的 `CHROME` 路徑依機器調整 |
| `.impeccable/` | 設計流程證據：`surfaces/app-py.md`（方向契約＋ADAPTATIONS）、`brief-app.md`、`decision/direction-3cbdd602.json`、`review/*.png` 與 `detect.json`、`design.json` |
| `requirements.txt`、`setup_env.ps1` | 環境重建 |

## 改東西的規則

- `data/*.json` 與 `guide/*.py` 有快取／已載入模組，**改完要重啟**（`restart_streamlit.ps1`）；只改 `assets/styles.css` 立即生效（每次重跑都重讀）。
- 新增專有名詞時，資料裡用成對欄位（`name`/`en`、`capital`/`capital_en`、`mark`/`mark_en`、`house`/`house_en`、`seat`/`seat_en`），再跑 `tools/build_glossary.py` 讓術語表跟上；純句子裡的名詞請加進腳本的 `EXTRA` 清單。
- 頁面組版用 `sheet(title, title_en, body_html, ref="卷X · 第N頁", cls="head|wide", stamp=None, lead=None)`：`head` 是各卷首頁（靛藍框、下方露一張紙），`wide` 釋放 36em 行寬給帳冊／術語表／年表；`ref` 是頁碼，CSS 放在用箋**腳**，不要放回標題上方（審查禁止眉批式小標）。
- 新增內容含新字後跑 `tools/build_fonts.py`（沒跑也不會壞：缺的字會落回 Google Fonts，只是那幾個字會慢一點出現）。
- 新增一卷：`ui.VOLUMES` 加一項（`path`、`tab` 色、`weight`），`app.py` 的 `FUNCS` 對應頁面函式，頁面函式第一行呼叫 `tabstrip("<path>")`。
- 設計底線（來自 DESIGN.md 與 Impeccable craft floor）：顏色只用 `:root` 的 token；朱紅只當印與格線；封面上的印用 `#e34b3f`；赭黃標籤選中時用墨色字（白字對比不足）；註記做成疊在紙上的紙條（`note()`），不做框中框；全站只有一個入場動作（朱印落下）；文字對比 ≥ 4.5:1；英文原名用 Courier Prime（`en()`）；封面只加工藝細節不加圖；圖像只以編號圖版出現（圖版一科瓦雷、圖版二薩恩剖面）。
- 事實不確定就蓋「待查」章（`stamp="待查"` 或帳冊裡 `stamp_inline("待查", "tbd")`），不要下斷言。目前待查：《奇械鍛爐》《尋路者指南》是否有中文譯本；薩恩人口寫成「各版設定書估計約二十萬至五十萬」。
- 不轉載譯本全文、不使用官方地圖與插圖（圖版一是自己畫的示意圖）。
- CSS 依賴 Streamlit 的 DOM 結構（`section[data-testid="stSidebar"]`、`[data-testid="stSidebarNav"]`、`[data-testid="stAppViewContainer"]` 用 `row-reverse` 把側欄放到右緣）；升級 Streamlit 後先檢查標籤軌。

## 做過什麼（時序）

1. 訪談確認：讀者＝公開華語 D&D 社群、內容＝全部主題、獨立網站 → 寫 PRODUCT.md。
2. 用 Impeccable 技能擲籤選方向（seed `3cbdd602`），使用者選「王座堡卷宗」：靛藍封面、直排「艾伯倫」、斜落的朱印「機密」、紅格公文用箋、右緣五色索引標籤軌（依篇幅分高）、手機改頂端標籤列。契約在 `.impeccable/surfaces/app-py.md`。
3. 以程式碼直接建站（無設計稿），兩輪檢視（`tools/snap.py` 截圖）、跑過一次設計偵測器（`review/detect.json`，剩餘項目為 Streamlit 自身的 transition 與靜態對比誤判）。
4. 完工審查第一輪判「fix」：印章改成 SVG 濾鏡印泥（破邊、掉墨、濃淡）、頁碼移到用箋腳、手機英文原名可折行、赭黃標籤選中改墨字、寬用箋釋放行寬；次要：註記改紙條、封面內縮與印色寫進契約 ADAPTATIONS、書目「待查」章、圖例出界、favicon、封面標籤頭改真連結。第二輪判「**ship**」，五項全部 resolved；補修灰色「無譯本」章太淡。
5. 文件代理寫出 DESIGN.md 與 `.impeccable/design.json`。
6. 完工後追加：圖版一擴成科瓦雷全境（16 地區＋王座堡，含圖例），「其他區域」帳冊加首府與王座堡條約承認狀態，手機上圖版可橫向拖動。
7. 質感升級（2026-09-28，依 frontend-design 與 taste-skill 的改版流程）：紅格線改為跟著段落走、手機段落靠左、用箋不隨滑鼠抬起；自帶字型子集、紙紋、桌面受光；封面加檔案標籤紙、暗紋圓章、書脊凸帶、磨損暗角；卷首用箋與章的入場動作；圖版二薩恩剖面；DESIGN.md 同步。

說明：這台機器的 Claude Code 沒有註冊 Impeccable 內建的審查／文件代理，審查與文件是由一般代理照 `~/.claude/skills/impeccable/reference/degraded/*.md` 代跑的；Impeccable 技能本身裝在 `~/.claude/skills/impeccable`（原始碼 https://github.com/pbakaus/impeccable ，當時官方安裝器 404，是手動下載檔案安裝的），新電腦要另外裝。

## 還沒決定／可做的下一步

- 站名、網域與主機（例如 Streamlit Community Cloud 需要 git 倉庫＋`requirements.txt`，已備好）。目前不是 git 倉庫。
- 11 個「其他區域」首府的中文名是音譯的（盧坎·德拉爾 Rhukaan Draal、大峭壁 The Great Crag、泰爾·瓦萊斯塔斯 Taer Valaestas、綠心 Greenheart、特羅蘭港 Trolanport、克羅納峰 Krona Peak、瑞加爾港 Regalport、新王座 Newthrone、集會堡 Gatherhold、扎拉沙克 Zarash'ak），若 DND5eChm 有既定譯名請改 `data/nations.json` 的 `seat`。
- 待查項目（見上）。
- 手機上多欄帳冊（書目五欄）偏擠，可考慮手機改直式排列。
