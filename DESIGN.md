---
name: "艾伯倫導覽"
description: "一疊攤在冷白桌面上的靛藍卷宗：紅格公文用箋、斜落的朱印、依篇幅分高的五色索引標籤。"
colors:
  seal: "#b3261e"
  seal-on-indigo: "#e34b3f"
  rule: "rgba(179, 38, 30, 0.55)"
  rule-faint: "rgba(179, 38, 30, 0.14)"
  indigo: "#16233f"
  indigo-deep: "#0f182c"
  indigo-ink: "#b9c4dc"
  tab-green: "#2c6e49"
  tab-ochre: "#d7a021"
  tab-violet: "#5b3a8a"
  paper: "#f4f5f2"
  paper-shade: "#e6e9ec"
  sheet-white: "#ffffff"
  ink: "#1d2b24"
  ink-soft: "#4b5a52"
typography:
  display:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "clamp(64px, 9vw, 124px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0.08em"
  headline:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "34px"
    fontWeight: 900
    lineHeight: 1.3
  title:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "28px"
    fontWeight: 900
    lineHeight: 1.3
  subtitle:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "20px"
    fontWeight: 900
    lineHeight: 1.3
  lead:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.85
  body:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.85
  body-sm:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "15.5px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "14px"
    fontWeight: 600
    letterSpacing: "0.06em"
  nav-tab:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "15px"
    fontWeight: 600
    letterSpacing: "0.12em"
  annotation:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "0.78em"
    fontWeight: 400
    letterSpacing: "0.01em"
  folio:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "12px"
    fontWeight: 400
    letterSpacing: "0.12em"
  numeral:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "14px"
    fontWeight: 700
    fontFeature: "tabular-nums"
  stamp:
    fontFamily: "Noto Serif TC, Songti TC, PMingLiU, serif"
    fontSize: "15px"
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: "0.28em"
rounded:
  none: "0"
  stamp: "4px"
  tab: "6px 0 0 6px"
  dot: "50%"
spacing:
  xs: "6px"
  sm: "14px"
  md: "22px"
  lg: "34px"
  xl: "40px"
  xxl: "56px"
  ruling: "31px"
components:
  cover:
    backgroundColor: "{colors.indigo}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "48px 56px 0 84px"
    height: "min(88vh, 760px)"
  button-open:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.indigo}"
    rounded: "{rounded.none}"
    padding: "12px 22px"
    size: "17px"
  nav-tab:
    backgroundColor: "color-mix(in srgb, var(--tab) 26%, #f4f5f2)"
    textColor: "{colors.ink}"
    typography: "{typography.nav-tab}"
    rounded: "{rounded.tab}"
    padding: "14px 8px"
    width: "120px"
    height: "56px + 8px × 篇幅權重（96px–144px）"
  nav-tab-active:
    backgroundColor: "var(--tab)"
    textColor: "{colors.paper}"
    typography: "{typography.nav-tab}"
    rounded: "{rounded.tab}"
    padding: "14px 8px"
  nav-tab-active-ochre:
    backgroundColor: "{colors.tab-ochre}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-tab}"
    rounded: "{rounded.tab}"
    padding: "14px 8px"
  tabstrip-tab:
    backgroundColor: "color-mix(in srgb, var(--tab) 12%, #ffffff)"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "5px 12px"
    size: "14px"
  tabstrip-tab-active:
    backgroundColor: "var(--tab)"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "5px 12px"
    size: "14px"
  sheet:
    backgroundColor: "{colors.sheet-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: "34px 40px 36px"
    width: "820px"
  sheet-head:
    backgroundColor: "{colors.sheet-white}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: "34px 40px 36px"
    width: "820px"
  sheet-wide:
    backgroundColor: "{colors.sheet-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: "34px 40px 36px"
    width: "100%"
  stamp:
    textColor: "{colors.seal}"
    typography: "{typography.stamp}"
    rounded: "{rounded.stamp}"
    padding: "4px 12px"
  stamp-cover:
    textColor: "{colors.seal-on-indigo}"
    typography: "{typography.stamp}"
    rounded: "{rounded.stamp}"
    padding: "8px 20px"
    size: "44px"
  stamp-inline:
    textColor: "{colors.seal}"
    typography: "{typography.stamp}"
    rounded: "{rounded.stamp}"
    padding: "1px 8px"
    size: "12px"
  tag:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1px 8px"
    size: "13px"
  note:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    width: "36em"
  ledger-head:
    textColor: "{colors.seal}"
    typography: "{typography.label}"
    padding: "8px 10px"
  ledger-cell:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "9px 10px"
  timeline-year:
    textColor: "{colors.seal}"
    typography: "{typography.numeral}"
    width: "116px"
  plate:
    backgroundColor: "{colors.sheet-white}"
    rounded: "{rounded.none}"
    padding: "16px"
  input-text:
    backgroundColor: "{colors.sheet-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
---

# Design System: 艾伯倫導覽

## Overview

**Creative North Star: "王座堡卷宗"**

整個艾伯倫被整理成一疊給新任探員翻閱的機密卷宗，攤在一張冷白的桌面上。桌面（`--paper` #f4f5f2）是最底層；靛藍封面是桌上的一件物件，不出血、三側留桌面；每一卷的內容寫在白色紅格公文用箋上，一張接一張往下疊；狀態與強調用斜落的朱印蓋上去；卷宗前緣（右側）是五色索引標籤軌，標籤高度依各卷篇幅比例。把所有內容拿掉，靛藍封面、紅格紙、朱印與彩色標籤軌仍然認得出是它。

密度與聲音是文件式的、克制的。全站只有一種內文（17px／1.85、行寬 36em），階層靠字重 900 與尺寸分級、靠「哪張紙在上面」；沒有眉批式小標，沒有框中框。中文一律思源宋體（Noto Serif TC），英文原名一律以打字機字體 Courier Prime 作碳寫註記。入場動作只有兩個節拍：封面「機密」印落下；翻開一卷時卷首用箋落到桌上、它的章接著落下。其餘互動只有標籤與按鈕輕輕抬起，用箋本身靜止。

已確認的拒絕：深色羊皮紙底、燙金襯線大標、同尺寸主題卡片格、卡片套卡片；封面是純色靛藍，不做仿布紋；沒有官方地圖與插圖，圖像只有自繪的 SVG 圖版，編號並附說明。

**Key Characteristics:**
- 桌面／封面／用箋三層材質：冷白桌面 #f4f5f2、靛藍封面 #16233f、白紙 #fff 配朱色格線。
- 所有紙面（用箋、紙條、標籤、封面標籤紙、按鈕、圖版）鋪一層極淡的纖維噪點（`static/paper-grain.png`，`--grain`），桌面自上而下微微受光；封面是壓有同色暗紋圓章、貼著檔案標籤紙的硬板，書脊有兩道凸帶，外緣有磨損暗角。
- 朱 #b3261e 只當「印」與「格」，落在靛藍上時換 #e34b3f。
- 單一內文字級 17px／1.85、36em；標題以 900 字重分級；英文原名 Courier Prime 碳寫註記。
- 階層靠疊紙、位移與軟陰影（`--lift`），沒有硬偏移陰影、沒有框中框。
- 方角紙、斜落印：圓角只在標籤前緣（6px）與印章（4px）；印章 -12°／-6°，紙條 ±0.5°。
- 五色索引標籤軌在前緣，高度依篇幅（56px + 8px × 權重）；手機改成頂端橫向標籤列。
- 一個入場動作（印落下 520ms），其餘 320ms 指數緩出；尊重 prefers-reduced-motion。

## Colors

一張冷白桌面上的靛藍卷宗與白紙朱印：三種材質色（桌面、封面、紙）、一種印色、五色標籤紙；`.streamlit/config.toml` 的主題鏡射同一組值（primaryColor 朱、backgroundColor 桌面、secondaryBackgroundColor 靛、textColor 墨），讓 Streamlit 原生元件落回同一個世界。

### Primary
- **朱印 Seal** (#b3261e)：印章、用箋的 2px 標題底線、帳冊欄頭、`.meta` 的欄名、折頁碼、年表的年份與圓點、清單的斜方點、`::selection` 反白、全站焦點環（`outline: 2px solid`，外距 3px）、輸入框焦點。它是紙上的印與格，不是底色；白紙上 6.5:1，桌面上 6.0:1。
- **靛上朱 Seal on Indigo** (#e34b3f)：只用於落在靛藍封面上的「機密」大印。#b3261e 在 #16233f 上只有約 2.4:1，#e34b3f 約 4.0:1，以 44px／900 的大字達到大字 AA。這是完工時記錄的調整，取代直向契約的 #b3261e。
- **朱框線 Rule** (rgba(179, 38, 30, 0.55))：用箋外框 1px、標題底線 2px、帳冊欄頭底線、時間軸的直線、圖版外框、輸入框邊。白紙上約等於 #d58883。
- **淡朱格線 Rule Faint** (rgba(179, 38, 30, 0.14))：用箋的 31px 紅格、內框第二道線、帳冊列線、七件事與術語表的分隔線、下層紙的邊。白紙上約等於 #f4e1e0。

### Secondary
- **靛藍封面 Indigo** (#16233f)：封面底、卷首用箋的框與標題底線、靛藍標籤紙（封面、第一卷）、捲軸滑塊、側邊欄收合鈕；也是所有陰影與細線的色相（rgba(22, 35, 63, α)）。
- **書脊靛 Indigo Deep** (#0f182c)：封面左側 34px 書脊，右側一道 rgba(255,255,255,0.08) 的線、內側一道虛線。
- **靛上淡墨 Indigo Ink** (#b9c4dc)：封面上的次要文字：副題。靛藍上 8.9:1。（檔號改寫在白色標籤紙上：欄名朱色、值墨色。）

### Tertiary
- **檔案綠 Archive Green** (#2c6e49)：第四、五卷（龍紋家族、種族）的標籤紙；「有譯本」章。白紙上 6.1:1。
- **赭黃 Ochre** (#d7a021)：第六、七卷（信仰與組織、位面）的標籤紙。唯一的淺色標籤：選中時字改墨色（`--tab-ink`）。
- **紫 Violet** (#5b3a8a)：附錄的標籤紙。
- 靛 #16233f 與朱 #b3261e 同時也是標籤色（封面／第一卷靛、第二／三卷朱）。每一卷的標籤色由 `tab_vars()` 以行內變數 `--tab` 帶進索引標籤、手機標籤與封面標籤頭；未選中的標籤以 `color-mix(in srgb, var(--tab) 26%, #f4f5f2)` 調成淡紙色（靛約 #babec3、朱 #e3bfbb、綠 #c0d2c6、赭 #ecdfbc、紫 #ccc4d7），墨字在其上皆 ≥ 7.9:1。

### Neutral
- **冷白桌面 Paper** (#f4f5f2)：頁面底色；也是紙條、標籤片、封面按鈕的底，以及靛藍與深色標籤上的字色。
- **桌面陰面 Paper Shade** (#e6e9ec)：右側標籤軌的底、捲軸軌道。
- **白紙 Sheet White** (#ffffff)：用箋、圖版、輸入框、時間軸圓點的紙面。用箋用純白而非桌面的冷白，換取紙疊與桌面的分離（完工時記錄的調整）。
- **墨 Ink** (#1d2b24)：全站文字、標籤片與淡色標籤上的字。白紙上 14.8:1、桌面上 13.5:1。
- **淡墨 Ink Soft** (#4b5a52)：英文原名註記、圖版說明、「無譯本」章。白紙上 7.3:1。
- **靛藍細線**（rgba(22, 35, 63, α)）：不是獨立色票，是靛藍的透明度家族：標籤軌左邊 0.18、紙條邊 0.12、卷首用箋內框 0.14、標籤片邊 0.35、帳冊列懸停底 0.035。

### Named Rules
**The Seal Rule.** 朱 #b3261e 在紙上只以「印」與「格」出現：印章、框線與格線、欄頭、折頁碼、年份、清單方點、焦點環、選取反白。唯一可填滿的朱色面是選中的朱色索引標籤。它從不當紙面或桌面的底色。

**The Cover Seal Rule.** 落在靛藍上的印一律用 #e34b3f，並且只以大字（封面 44px、手機 30px，900）出現；紙上的印維持 #b3261e，並套 `#ink-seal`／`#ink-fine` 印泥濾鏡。

**The Ochre Ink Rule.** 赭黃 #d7a021 選中時字用墨 #1d2b24（6.3:1），不用紙白（2.2:1）；其餘四色選中時字為紙白 #f4f5f2（靛 14.3:1、朱 6.0:1、綠 5.6:1、紫 7.9:1）。

## Typography

**Display Font:** Noto Serif TC（後備 Songti TC、PMingLiU、serif）
**Body Font:** Noto Serif TC（同上；`.stApp *` 一律套用，Streamlit 原生元件也是）
**Label/Mono Font:** Courier Prime（後備 Courier New、monospace）：英文原名、折頁碼、年份與數字欄、`code`

**字型自帶。** `tools/build_fonts.py` 把思源宋體三個字重子集化成只含本站用字的 woff2（各約 770 KB）放在 `static/fonts/`，CSS 在 Google Fonts 的 `@import` 之後宣告同名 `@font-face`，所以本機子集優先、子集外的字落回 Google；新增內容含新字後重跑一次。標題套 `text-wrap: balance` 與 0.02em 字距（封面卷名 0.04em）；全站 `text-spacing-trim: space-first`、`hanging-punctuation: allow-end`，支援的瀏覽器才生效。

**Character:** 一種宋體撐起整本卷宗，從封面 124px 的直排大字到 12px 的折頁碼都是同一張臉，只靠字重（900／600／400）與尺寸分級；打字機字體只給「後來補上的」東西：英文原名、頁碼、數字。宋體是公文，Courier 是碳寫的註記。

### Hierarchy
- **Display**（900，clamp(64px, 9vw, 124px)，1，字距 0.08em）：封面直排大字「艾伯倫」，`writing-mode: vertical-rl`、`text-orientation: upright`；手機改橫排 64px、0.04em。
- **Headline**（900，34px，1.3）：各卷卷首用箋的標題（`.sheet.head h2`），靛藍 2px 底線。封面卷名 `.dossier` 用 clamp(30px, 3.6vw, 46px)／1.2。
- **Title**（900，28px，1.3）：一般用箋的 h2，朱 2px 底線，下距 14px。
- **Subtitle**（900，20px，1.3，上距 26px）：用箋內的 h3。七件事條目的 h3 19px、時間軸事件名 18px 屬同一級。
- **Lead**（600，19px，1.85）：每張用箋開頭的一句話 `.lead`，下距 18px；封面導言 `.lede` 22px／1.7／600。
- **Body**（400，17px，1.85，量 36em）：全站唯一內文字級；段落下距 14px、兩端對齊，手機靠左。
- **Body small**（400，15.5px，1.6）：帳冊表；紙條 15.5px／1.8；`.meta`、術語表、封面檔號 15px。
- **Label**（600，14px，字距 0.06em）：帳冊欄頭，朱色、不換行；`.meta dt` 朱 600 15px。
- **Nav tab**（600，15px，字距 0.12em，直排 mixed）：索引標籤軌；封面標籤頭 12px／0.08em；手機標籤列 14px／600。
- **Annotation**（Courier Prime，400，0.78em，字距 0.01em，`--ink-soft`）：英文原名 `.en`，緊跟中文之後、左距 0.5em、不換行；h2 內 14px 並以 `vertical-align: 0.35em` 提到上緣；帳冊格內另起一行 12.5px；手機的標題內另起一行。
- **Folio**（Courier Prime，12px，字距 0.12em，`--seal`）：用箋腳的頁碼 `.ref`（如「卷二 · 第三頁」），右下角、白底墊 4px 蓋住格線。
- **Numeral**（Courier Prime，`tabular-nums`；年份 14px／700／朱）：年表的年份、月份序號、帳冊的 `.num` 欄。
- **Stamp**（900，字距 0.28em，1.3）：印章文字；封面 44px、用箋 15px、行內章 12px／0.16em；`text-indent` 抵消字距讓字置中。

### Named Rules
**The One Body Size Rule.** 內文只有 17px／1.85 一種字級、行寬 36em；階層靠字重 900 與 34／28／20px 的尺寸，沒有眉批式小標，也沒有全大寫的小字標籤。用箋的頁碼在腳、章在角落，標題上方永遠是空的。

**The Carbon Copy Rule.** 每個專有名詞第一次出現時，英文原名以 Courier Prime 0.78em 淡墨緊跟在中文之後，像碳寫的註記；它永遠是附註，不當標題、不當裝飾字。

**The Tabular Figures Rule.** 年份、頁碼、序號、金額一律 Courier Prime 加 `font-variant-numeric: tabular-nums`；數字在欄位裡對齊，在年表上靠右釘在事件旁。

## Layout

**桌面與卷宗。** 頁面是一張冷白桌面：`.block-container` 最寬 1060px、內距 0 2.5rem 4rem，Streamlit 頁首壓成 2.5rem 透明、工具列與頁尾隱藏。`[data-testid="stAppViewContainer"]` 以 `flex-direction: row-reverse` 把側邊欄搬到右側，成為卷宗前緣的索引標籤軌。所有物件（封面、用箋、標籤軌）都攤在同一張桌面上；封面不出血，1440 寬時約 980×760、三側留桌面（完工時記錄的調整，取代直向契約的滿版封面）。

**索引標籤軌。** 132px 寬、`--paper-shade` 底、左邊 1px rgba(22,35,63,0.18)。標籤列 `gap: 6px`、右留 12px，標籤 120px 寬、內距 14px 8px、文字直排。高度由 `inject_css()` 依各卷篇幅權重注入 nth-child 規則：56px + 8px × 權重（權重 5→96px、6→104px、7→112px、11→144px）。九張標籤：封面、第一卷歷史（靛）、第二卷諸國、第三卷薩恩（朱）、第四卷龍紋家族、第五卷種族（綠）、第六卷信仰與組織、第七卷位面（赭）、附錄（紫）。

**封面。** `min-height: min(88vh, 760px)`、內距 48px 56px 0 84px、上距 0.5rem 下距 1.5rem；左側 34px 書脊；內容以 `grid-template-columns: auto 1fr`、欄距 56px 排成直排大字 + 卷宗資料（最寬 560px）；封面底邊一列八張 22px 高的標籤頭（`.tabheads`，七卷加附錄，左移 20px）。「機密」大印絕對定位在右 64px、下 96px。檔號區是一張貼在封面上的紙標籤（`dl.filenum`：#fbfbf8 底、紙紋、1px 靛藍 25% 邊、上緣 4px 朱色橫條、-0.6°、`width: max-content`）；封面下方的空場壓一枚同色的暗紋圓章「王座堡」（`.emboss`，156px，左 244px 下 34px，只靠內陰影與 11% 白字讀出，手機隱藏）；封面外緣 70px 內陰影做磨損暗角，書脊上下各一道 8px 凸帶與內側虛線縫線，直排大字帶 2px 印壓陰影。

**用箋。** 最寬 820px、下距 22px、內距 34px 40px 36px；`.sheet.wide` 放寬到 100%，但其中的段落、開頭句、清單、`.meta`、紙條與年表文字仍鎖 36em。紅格跟著字走：每個內文段落與清單項目自己以 `background-size: 100% 1lh` 在每個行框底上 3px 處畫一條 1px 淡朱線，所以格線永遠貼在該段文字的每一行之下，不會穿過標題、帳冊、紙條或年表；開頭句、標題與卷首用箋不畫格。

**節奏。** 6px（標籤與標籤片間距、`.meta` 列距）、14px（段落與標題下距）、22px（用箋之間、年表事件之間、圖版上距）、26px（h3 上距）、34／36／40px（用箋內距）、56px（封面欄距）。

**年表。** `padding-left: 150px`，直線在 136px，年份寬 116px 靠右釘在左側；事件下距 22px。**術語表**兩欄、欄距 32px。

**行動版（單一斷點 `max-width: 900px`）。** 側邊標籤軌與 Streamlit 的收合鈕、抽屜一律隱藏，改由每頁頂端的橫向標籤列（`.tabstrip`，`gap: 6px`、可橫向捲動、隱藏捲軸）接手；桌面內距改 0 16px 3rem；封面內距 28px 22px 26px 46px、單欄、大字改橫排 64px、大印改為靜態流入（上距 24px、下距 26px、30px）、標籤頭隱藏；用箋內距 26px 18px、折頁碼右 18px 下 7px、章右 12px 上 10px 13px、內文靠左、英文註記可換行且在標題內另起一行；年表左距 74px、直線 60px、年份 52px／12px；術語表單欄；帳冊 14px、格內距 7px 6px。

### Named Rules
**The Fore Edge Rule.** 索引標籤軌永遠在卷宗前緣（右側），標籤突向用箋；手機上它變成頂端一列橫向標籤，絕不變成抽屜蓋在用箋上。

**The Proportional Tab Rule.** 標籤高度不是等高的：56px + 8px × 該卷篇幅權重，長的卷標籤就高。新增一卷時給它權重與標籤色，不手調高度。

**The Desk Rule.** 一切物件攤在 #f4f5f2 桌面上；封面是桌上的物件而非滿版背景，用箋最寬 820px 而非撐滿容器。

## Elevation & Depth

混合式：深度靠「哪張紙在上面」（疊紙、位移、露出下層紙）加上一種有位移、負擴散的靛藍軟影；沒有硬偏移陰影，沒有以描邊或底色差表達層級的框中框。靜止時用箋已有 `--lift`（它本來就是一張放在桌上的紙），閱讀時不因懸停而動，用箋是讀的不是按的；卷首用箋底下露出第二張略斜（0.6°）的白紙；索引標籤懸停滑出 4px、選中滑出 6px 並帶 `--lift`；紙條是「放在用箋上的一張紙」，自帶 `--lift` 與 ±0.5° 的歪斜。動態全部走 `--ease`（cubic-bezier(0.16, 1, 0.3, 1)）、320ms，只作用於 transform、box-shadow、background；入場動畫只有兩個節拍：封面大印 `seal-land`（520ms、延遲 240ms，`rotate(-12deg) scale(1.35)` 落到 `scale(1)`、透明度 0 → 0.92）；翻到任一卷時，卷首用箋 `sheet-lay` 從下方 16px、-0.35° 落到桌上（520ms），它右上角的章接著以 `seal-land` 落下（延遲 460ms）。之後靜止。`prefers-reduced-motion: reduce` 時關掉該動畫，並取消封面按鈕與標籤的過渡與位移。

### Shadow Vocabulary
- **Lift**（`box-shadow: 0 10px 24px -14px rgba(22, 35, 63, 0.45), 0 1px 0 rgba(22, 35, 63, 0.06)`，即 `--lift`）：用箋靜止、紙條、索引標籤懸停與選中。唯一的通用陰影。
- **Sheet inset**（`inset 0 0 0 4px #fff, inset 0 0 0 5px var(--rule-faint)`）：用箋內縮 4px 的第二道淡朱框線；卷首用箋改 rgba(22, 35, 63, 0.14)。
- **Cover**（`0 24px 48px -28px rgba(15, 24, 44, 0.7), inset 0 0 0 1px rgba(255, 255, 255, 0.06)`）：封面壓在桌面上的一道深影與一圈極淡的邊光。
- **Open button**（`0 8px 18px -10px rgba(0, 0, 0, 0.6)`；懸停 `0 14px 24px -12px rgba(0, 0, 0, 0.7)` + `translateY(-2px)`）：封面「翻開卷宗」。
- **Focus**（`0 0 0 2px rgba(179, 38, 30, 0.25)` + 邊改朱）：輸入框焦點；其他元件用全站 `outline: 2px solid var(--seal)`、外距 3px。

### Named Rules
**The Top Sheet Rule.** 階層靠哪張紙在上面：要分層就疊一張紙、移一點位、露一角下層紙，不在紙上再畫一個框。用箋裡唯一允許的框是裱圖版的那一道 1px 朱線。

**The Soft Shadow Only Rule.** 陰影只有 `--lift` 與它在標籤、按鈕上的懸停版：有位移、負擴散、靛藍色相；沒有硬偏移陰影、沒有黑色純影、沒有發光。

## Shapes

紙是方角的，印是斜的。所有紙面（用箋、圖版、紙條、標籤片、輸入框、封面按鈕、捲軸滑塊）都是 0 圓角；圓角只出現在兩個地方：索引標籤突向用箋的那一邊（`6px 0 0 6px`，貼軌的一邊方角）與印章的框（4px）。時間軸的節點是 10px 白底、2px 朱邊的圓點；清單的項目符號是 0.42em、旋轉 45° 的空心小方點。

邊線：用箋與圖版 1px `--rule`，內縮 4px 再一道淡朱線；標題底線 2px；卷首用箋改靛藍；印章 3px 雙線（封面 4px）；標籤片 1px 靛藍 35%；紙條 1px 靛藍 12%；手機標籤與封面標籤頭以 4px 的標籤色上邊條標示所屬卷。

歪斜是這個世界的幾何：印章 -12°（行內章 -6°），紙條 -0.5°、第二張 +0.4°，卷首用箋底下的紙 +0.6°；封面書脊 34px 寬、內側一道 1px 虛線。印章另有 SVG 印泥濾鏡（`#ink-seal`、小章 `#ink-fine`，由 `ui.inject_css()` 注入一次）：碎邊、掉墨點、濃淡不一。

### Named Rules
**The Square Paper, Tilted Seal Rule.** 紙方角、印斜落。新元件若是紙就 0 圓角、直放；若是印就 4px 圓角、雙線、負角度、套印泥濾鏡；沒有第三種。

## Components

### Buttons
全站只有一個自製按鈕：封面的「翻開卷宗」（`.cover .open`）。它是一張貼在靛藍封面上的紙片。
- **Shape:** 方角（0），1px `--paper` 邊。
- **Primary:** 紙白底 #f4f5f2、靛藍字 #16233f、17px／600、內距 12px 22px、`inline-block`。
- **Hover / Focus:** 抬起 2px、影子從 `0 8px 18px -10px rgba(0,0,0,0.6)` 拉到 `0 14px 24px -12px rgba(0,0,0,0.7)`，320ms `--ease`；焦點用全站朱色 outline。
- **Secondary / Ghost:** 沒有。其他導航都是標籤或連結。

### Chips
- **Style:** 標籤片 `.tags span`：桌面色底 #f4f5f2、墨字 13px、1px rgba(22,35,63,0.35) 邊、內距 1px 8px、方角；`flex-wrap`、間距 6px。
- **State:** 純標示，沒有選取態。狀態要用章不用片：行內章 `.stamp.ok`（檔案綠「有譯本」）、`.stamp.no`（淡墨「無譯本」）、`.stamp.tbd`（朱「待查」），12px／-6°／`#ink-fine`。

### Cards / Containers
用箋（`.sheet`）是唯一的容器：一張紅格公文用箋，不是卡片。
- **Corner Style:** 方角（0）。
- **Background:** 白紙 #fff；紅格由內文段落與清單項目自己畫（每個行框一條 `--rule-faint`，貼在文字之下）。
- **Shadow Strategy:** 靜止 `--lift`；用箋不做懸停位移（見 Elevation & Depth）。
- **Border:** 1px `--rule`，內縮 4px 再一道 `--rule-faint`；卷首用箋（`.sheet.head`）改靛藍邊與 rgba(22,35,63,0.14) 內框、不畫格、標題 34px 靛藍底線、底下露出一張 +0.6° 的白紙（`::before`，`inset: 10px -8px -10px 8px`）。
- **Internal Padding:** 34px 40px 36px；手機 26px 18px。
- **Anatomy:** 右上角至多一枚章（`.sheet > .stamp`，15px，右 22px 上 18px）；h2 附英文原名；`.body` 內先一句 `.lead` 再展開；腳的右下角是 Courier Prime 折頁碼 `.ref`。`.sheet.wide` 放寬到 100% 給帳冊、術語表與年表，文字仍鎖 36em。
- **紙條（`.note`）：** 放在用箋上的一張紙：`--paper` 底、1px rgba(22,35,63,0.12) 邊、`--lift`、-0.5°（第二張 +0.4°、上距 16px）、內距 12px 16px、15.5px／1.8、最寬 36em；標籤 `strong` 朱色 600 並自帶全形冒號。
- **圖版（`.plate`）：** `figure`，1px `--rule` 邊、內距 16px、白底、上距 22px；SVG 撐滿寬；`figcaption` 13.5px 淡墨，「圖版一」以朱色 600 起頭。圖版 SVG 自己用同一組色：底 #f4f5f2、框 #16233f 2px、字 #1d2b24、警示區 #b3261e 45° 斜線紋。圖版二（薩恩剖面，`_sharn_plate()`）沿用：塔身白底靛線的梯形、層區分界虛線、齒輪區 45° 靛線斜紋、匕首河波線、天城區浮島。

### Inputs / Fields
- **Style:** Streamlit `st.text_input` 重新上色：白底、1px `--rule` 邊、方角、宋體。
- **Focus:** 邊改朱、`box-shadow: 0 0 0 2px rgba(179,38,30,0.25)`。
- **Error / Disabled:** 未定義（站內只有術語查詢一個輸入框）。

### Navigation
- **索引標籤軌（桌機）：** 右側 132px 軌、`--paper-shade` 底。標籤直排 15px／600／0.12em、墨字、`color-mix(in srgb, var(--tab) 26%, #f4f5f2)` 淡底、1px `color-mix(... 70%)` 邊、左圓角 6px、高度 56px + 8px × 權重。懸停滑出 4px 帶 `--lift`；選中（`aria-current="page"`）填滿標籤色、紙白字（赭黃改墨字）、滑出 6px。
- **手機標籤列（≤ 900px）：** 頁頂一列 `.tabstrip a`：`color-mix(in srgb, var(--tab) 12%, #fff)` 底、1px `color-mix(... 55%)` 邊、4px 標籤色上邊條、內距 5px 12px、14px／600、不換行、可橫向捲動；選中填滿標籤色。
- **封面標籤頭：** 封面底邊八張 22px 高的紙白標籤頭，12px／0.08em 墨字、4px 標籤色上邊條、內距 0 12px、間距 8px，懸停抬 3px；手機隱藏。
- **頁內連結：** 封面「翻開卷宗」以錨點 `#seven` 捲到第一張用箋。

### Seal（印章）
全站的狀態與強調語彙。`.stamp`：`inline-block`、3px 雙線朱框、4px 圓角、朱字 900、字距 0.28em（`text-indent` 抵消）、-12°、`mix-blend-mode: multiply`、透明度 0.9、`filter: url(#ink-seal)`。三個尺寸：封面大印 44px（#e34b3f、4px 框、`mix-blend-mode: normal`、透明度 0.92、`seal-land` 落下動畫，手機 30px 靜態）；用箋章 15px（右上角，如「待查」「警戒」「機密」「通緝」「備查」「已消失」）；行內章 12px（-6°、字距 0.16em、內距 1px 8px、`#ink-fine`）。印文只用兩個字，字越少章越像章。

### Ledger（帳冊表）
`table.ledger`：滿寬、`border-collapse`、15.5px／1.6。欄頭朱色 600 14px／0.06em、靠左、2px `--rule` 底線；格 9px 10px、1px `--rule-faint` 列線、頂對齊；數字欄 `.num` 用 Courier Prime `tabular-nums` 不換行；格內英文原名另起一行 12.5px；列懸停底 rgba(22,35,63,0.035)。手機 14px、格 7px 6px。

### Timeline（尺規年表）
`ol.rule`：一條 1px `--rule` 的連續直線，事件是 10px 白底朱邊的圓點；年份 Courier Prime 14px／700／朱、靠右釘在直線左側 116px 欄；事件名 18px／900、正文 16px；事件間距 22px。手機左距 74px、年份 52px／12px。

### Seven（七件事）
`ol.seven`：序號是內容，以 `counter(things, cjk-ideographic)` 排成 44px 的 1px 朱框方格、朱字 900 18px 放在左側；條目內距 14px 0 14px 64px、`--rule-faint` 分隔；標題 19px。

### Meta（欄位列）
`dl.meta`：`grid-template-columns: max-content 1fr`、間距 6px 16px、15px；欄名 `dt` 朱色 600 不換行，值 `dd` 墨字，可放標籤片。

### Glossary（術語表）
兩欄（欄距 32px）、`break-inside: avoid`；每條 15px、內距 6px 0、`--rule-faint` 底線，中文後接 `.en`（左距 0.6em）；手機單欄。

## Do's and Don'ts

### Do:
- **Do** 把每個新內容區塊放在一張用箋（`.sheet`）上：白紙 #fff、1px `--rule` 邊、內縮 4px 白 + 5px `--rule-faint` 的內框、`--lift` 軟影、內距 34px 40px 36px、最寬 820px；表格、術語表、年表才用 `.sheet.wide`。
- **Do** 每張用箋在腳放一個 Courier Prime 12px 朱色折頁碼（`.ref`，如「卷二 · 第三頁」）；狀態章最多一枚，落在右上角。
- **Do** 每個專有名詞第一次出現時，用 `.en` 把英文原名以 Courier Prime 0.78em 淡墨緊跟在中文之後。
- **Do** 內文維持 17px／1.85、36em；標題只用 900 字重與 34／28／20px 分級。
- **Do** 用該卷的標籤色 `--tab` 貫穿它的索引標籤、手機標籤與封面標籤頭；赭黃選中時字改墨色（`--tab-ink`）。
- **Do** 落在靛藍上的朱印用 #e34b3f；紙上的印維持 #b3261e，並套 `#ink-seal`／`#ink-fine` 印泥濾鏡。
- **Do** 要在用箋上附註，就放一張略歪的紙條（`.note`，`--paper` 底、`--lift`、±0.5°），標籤朱色 600 並自帶全形冒號。
- **Do** 數字用 Courier Prime + `tabular-nums`：年份靠右釘在年表直線左側，帳冊數字欄用 `.num`。
- **Do** 尊重 `prefers-reduced-motion`：關掉印落下、用箋落下動畫與所有位移過渡。
- **Do** 新增含新字的內容後跑 `tools/build_fonts.py` 重建字型子集。

### Don't:
- **Don't** 用眉批式小標、全大寫小字標籤或任何放在標題上方的短標；用箋的識別在腳（折頁碼）與角落（章）。
- **Don't** 用深色羊皮紙、米色紙、燙金襯線大標，或在封面加仿布紋、紋理：封面是純色 #16233f。
- **Don't** 排同尺寸的主題卡片格，或在用箋裡再畫一個框；要分層就疊一張紙。
- **Don't** 用硬偏移陰影或描邊做深度；唯一的陰影語彙是 `--lift` 與它的懸停版。
- **Don't** 把朱 #b3261e 當底色填滿一個面（選中的朱色索引標籤與選取反白除外）。
- **Don't** 在赭黃 #d7a021 上放白字（2.2:1）；也不要把 #b3261e 直接印在靛藍上（約 2.4:1）。
- **Don't** 加圓角超過標籤前緣的 6px 與印章的 4px：沒有藥丸按鈕、沒有圓角卡片、沒有圓角輸入框。
- **Don't** 在 900px 以下顯示側邊標籤軌或 Streamlit 抽屜；行動版只用頂端橫向標籤列。
- **Don't** 用圖示字型或字符圖示補畫面；圖像只以編號圖版（`.plate`，「圖版一」+ 說明）出現。
