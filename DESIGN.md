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

**Creative North Star: "牛皮紙案卷"**

整個艾伯倫是一疊放在深色桌面上的牛皮紙檔案夾。封面是合上的夾子：頂邊咬著一枚長尾夾，正面貼一張印刷的檔案標籤，下方一條黑底紅字的「機密」橫帶，底邊別著一枚紅色迴紋針，右緣是一張綠色檔案標籤紙。翻開之後，每一卷是同一個攤開的夾子，裡面夾著幾件不同格式的文件：白色公文紙（打孔）、印好格式的記錄單、紅色檔案卡（左緣一枚鐵夾）、黃色警示紙、貼著膠帶的便條、牛皮紙名片、方格紙上用膠帶貼著的拍立得。狀態與強調仍用紅色橡皮章。把所有文字拿掉，牛皮紙夾、白紙、紅卡、黃紙、鐵夾與迴紋針仍然認得出是它。

密度與聲音是檔案式的：每件文件有自己的格式，同一頁裡不會有兩件長得一樣的文件；文件之間靠露出一角、微微歪斜與各自的陰影表示「這是好幾張紙」，不靠框線。宋體是印刷的正文，Courier Prime 是打字機打上去的欄位與編號，霞鶩文楷（鋼筆藍）是探員自己補寫的字。入場動作只有兩個節拍：封面的「機密」橫帶落下；翻到一卷時，第一件文件落進夾子、它的章接著蓋下。

已確認的拒絕：靛藍布面封面、白底紅格用箋（舊版）、同尺寸卡片格、框中框、羊皮紙漸層、燙金襯線大標；沒有官方插圖，圖像只有使用者提供的照片與自繪的 SVG 圖版，兩者都以拍立得的形式貼在方格紙上。

**Key Characteristics:**
- 四層材質：深色桌面 #17150f、牛皮紙 #c9a36f（亮面 #dcc191、暗面 #a7804b）、白色公文紙 #f8f5ee、米色紙 #f3ead4；另有紅色檔案卡 #cb3628、黃色警示紙 #f2c437、方格紙 #eff3f0。
- 三種筆跡：宋體正文（Noto Serif TC）、打字機欄位（Courier Prime）、鋼筆手寫（LXGW WenKai TC，#24408c）。
- 四種固定物：長尾夾（封面頂邊）、鐵夾（檔案卡左緣）、迴紋針（封面底邊）、膠帶（便條與拍立得頂邊）。
- 每件文件有自己的傾角（`--tilt`，±0.3° 到 ±1.6°），陰影是 `--lift`（有位移、負擴散、近黑）加 1px 極淡邊；手機上全部歸零。
- 紅色 #c2321f 是印章、橫帶、欄名、折頁鍵；紅色檔案卡是唯一整片紅的物件。
- 索引標籤軌是牛皮紙夾的標籤：前緣一條 7px 卷色色帶，開啟的那卷微微染上卷色並抽出。

## Colors

### Desk & Kraft
- **桌面 Desk** (#17150f)：頁面底色；上方以 `radial-gradient` 亮到 #2b2720，像桌燈從上方打下。標籤軌底 #100f0b。
- **牛皮紙 Kraft** (#c9a36f)：封面與攤開的夾子；以 `linear-gradient(160deg)` 從亮面 #dcc191 到暗面 #a7804b，鋪一層纖維貼圖 `static/kraft-grain.png`（`--fibre`）。名片用更亮的 #e6d1a6 → #d5bc87。
- **牛皮紙上的墨 Kraft Ink** (#3a2c15)：標籤軌與名片上的字。

### Papers
- **公文紙 Bond** (#f8f5ee)：白色文件、記錄單、拍立得相紙（#fdfcf8）；鋪 `static/paper-grain.png`（`--grain`）。
- **米色紙 Cream** (#f3ead4)：封面標籤、次要文件（`.doc.cream`）、標籤片；便條 #f7f0da。
- **方格紙 Grid** (#eff3f0，格線 rgba(120,150,175,0.35)，22px)：拍立得貼在上面的紙。
- **檔案卡 Card** (#cb3628，暗面 #a32b1f，字 #f8ecd6)：國家、種族、組織的側寫卡；卡上兩道 1px 米色細框（45%／25%）。
- **警示紙 Slip** (#f2c437，字 #1c1a12)：頂邊一條黑色虛線帶。

### Ink
- **墨 Ink** (#1b1a17)：全站正文；公文紙上 15:1。
- **淡墨 Ink Soft** (#57544c)：英文原名、折頁碼、欄名、腳註；公文紙上 6.5:1。
- **鋼筆藍 Pen** (#24408c)：手寫字；牛皮紙上 5.2:1、米色紙上 8.4:1。
- **朱 Seal** (#c2321f)：印章、橫帶底、欄名、折頁鍵、清單方點、焦點環、選取反白；紙上 5.3:1。
- **橫帶字**（#ff5238 on #151311）：只用於封面「機密」橫帶的字。

### Tabs
靛 #2f3f6e（封面、第一卷）、朱 #c2321f（第二、三卷）、綠 #5f8f6c（第四、五卷）、赭 #d9a23a（第六、七卷）、紫 #6c5a91（附錄）。每卷的色由 `tab_vars()` 以行內變數 `--tab` 帶進索引標籤與手機標籤；未選中只在標籤前緣 7px 色帶出現，選中時標籤底色染成 `color-mix(tab 28%, kraft-light)`，字維持牛皮紙墨色（900 字重）。

### Named Rules
**The One Red Object Rule.** 整片紅的物件只有紅色檔案卡與封面橫帶；其他地方的紅只當印、帶、欄名與點。

**The Three Hands Rule.** 印刷是宋體，打字機是 Courier Prime，手寫是霞鶩文楷。手寫只出現在探員會親手補的地方：記錄單裡短的欄位值、便條（`hand_written=True`）、拍立得圖說、封面的一句話。長段正文永遠不用手寫。

**The Kraft Shows Through Rule.** 夾子是所有文件的底；打孔的洞露出牛皮紙，文件之間的縫露出牛皮紙，方格紙與名片也放在牛皮紙上。沒有文件直接放在桌面上。

## Typography

**Display / Body:** Noto Serif TC（400／600／900；`static/fonts/NotoSerifTC-*.woff2` 子集）
**Typed:** Courier Prime（400／700／italic；欄名、編號、英文原名、折頁碼、橫帶副標、封面按鈕）
**Hand:** LXGW WenKai TC（400；`static/fonts/LXGWWenKaiTC-400.woff2` 子集，`--hand`）

字型自帶：`tools/build_fonts.py` 掃描 data、guide、app.py、styles.css 的全部字元，把四個字檔子集化成 woff2 放進 `static/fonts/`（各約 520 到 790 KB）；CSS 在 Google Fonts 的 `@import` 之後宣告同名 `@font-face`，子集外的字落回 Google。新增內容含新字後重跑一次。

### Hierarchy
- **封面主題**（900，54px，字距 0.2em）：標籤上的「艾伯倫」；英文副題 13px／0.34em 淡墨。
- **文件標題**（900，27px，字距 0.02em，`text-wrap: balance`，2px 墨色底線）：白紙文件 `.doc h2`；卷首 32px。
- **記錄單標題**（900，22px，字距 0.06em，3px 雙線底）：`.form .formhead h2`；右側打字機編號（`no`）。
- **檔案卡名稱**（900，30px，字距 0.06em，米色字）：`.card h2`；原名 Courier 12px／0.22em 另起一行。
- **警示紙標題**（900，21px，字距 0.1em）：`.slip h2`。
- **小標**（900，19px）：`.doc h3`、記錄單條目的事項 17.5px。
- **開頭句**（600，18.5px）：`.lead`；記錄單裡 17.5px。
- **正文**（400，17px，1.85，36em）：白紙文件；記錄單段落 16.5px／1.8／38em；便條 15.5px／1.75；名片 14px／1.6。
- **欄名**（600，12.5px，字距 0.14em，淡墨）：記錄單 `.k`；檔案卡欄名 Courier 10.5px／0.2em。
- **打字機小字**（Courier，11 到 12px，字距 0.1 到 0.16em）：局處線 `.bureau`、折頁碼 `.ref`、記錄單編號、拍立得的第二行。
- **手寫**（文楷，18 到 24px，鋼筆藍）：封面一句話 24px（加 0.35px 描邊），便條 18px，記錄單短值 19px，拍立得圖說 18px。
- **印章**（900，字距 0.28em）：文件章 15px、行內章 12px；封面橫帶字 30px／0.42em。

### Named Rules
**The Typed Field Rule.** 凡是表單上印好的東西（欄名、編號、局處線、頁碼）一律 Courier Prime 小字加字距；凡是填進去的東西是宋體或手寫。

**The Carbon Copy Rule.** 專有名詞第一次出現時，英文原名以 Courier Prime 0.78em 淡墨緊跟在中文之後；在檔案卡與名片上則另起一行。

## Layout

**桌面與夾子。** `.block-container` 最寬 1060px；攤開的夾子 `.folder` 最寬 940px、內距 34px 40px 60px、圓角 6px，左側 22px 處一道摺線；封面 `.cover` 最寬 760px、最低 620px、上距 52px 讓長尾夾露出。所有文件在夾子裡置中、最寬 800px；文件之間 30px，白紙接白紙時 -6px 讓它們疊起來。

**文件的排法。** 每一卷是一個夾子，裡面照內容選文件格式，同一頁不重複：
- 卷首永遠是一張打孔的白紙（`doc(cls="head punched", bureau=...)`），頂端一行打字機局處線。
- 一個實體（國家、種族、組織）＝一張紅色檔案卡（名稱、一句話、欄位）＋接在後面、從卡片底下露出來的白紙（正文、便條、清單）。
- 表格與有編號的清單＝記錄單（`form`）：雙線標題、右側編號、欄位列或條目列、腳註。
- 一組同類小項（家族、位面、勢力）＝名片格（`bizcards`，牛皮紙或白色索引卡）。
- 警告、猜測、風險＝黃色警示紙（`slip`）。
- 附註＝貼在文件上的便條（`note`／`memos`），手寫或印刷。
- 圖像＝方格紙（`pinboard`）上的拍立得（`polaroid`），圖說手寫、第二行打字機。

**索引標籤軌。** 132px 寬、桌面色底加左緣 16px 陰面。標籤列填滿軌高（扣上下 16px），`inject_css()` 依各卷篇幅權重注入 `li:nth-child(n){--w:權重}`，每張標籤以 `flex: var(--w) 1 0` 分得高度（下限 58px），軌永遠剛好一個視窗高；標籤是牛皮紙索引標：纖維、上亮下暗、1px 深邊、左圓角 7px、前緣 7px 卷色色帶；文字直排 600、`clamp(12.5px, 1.6vh, 15px)`，可在空格處折成第二列。手機（≤ 900px）改頂端橫向標籤列，牛皮紙底、4px 卷色上邊；標籤是 `st.page_link`（站內換頁），選中的那張由 `tabstrip()` 以 nth-child 規則填卷色。Streamlit 的透明頁首在手機上高 60px 且蓋在最上層，已設 `pointer-events: none`，否則會吃掉標籤列的點擊。

**節奏。** 6px（標籤片、欄位列距）、10 到 14px（段距、便條內距）、18 到 22px（便條間距、名片間距、拍立得間距）、26 到 30px（文件間距、方格紙內距）、34 到 44px（文件內距）。

### Named Rules
**The One Folder Per Volume Rule.** 一卷一個夾子，夾子裡的文件才是內容單位；Streamlit 元件要放進夾子時，把夾子切成上下兩半（`page(..., part="top")`／`part="bottom"`），元件夾在中間。

**The Different Paper Rule.** 同一頁裡相鄰的兩件文件不能同一種格式；至少要換紙色（白／米）、換格式（文件／記錄單／卡）或換物件（便條／名片／拍立得）。

## Elevation & Depth

深度靠「這是一張真的紙」：每件文件有自己的傾角（`--tilt`）、`--lift`（`0 12px 28px -16px rgba(0,0,0,0.75), 0 2px 4px -2px rgba(0,0,0,0.35)`）加一圈 1px 12% 黑邊當紙厚；檔案卡與名片的邊更深（35%／25%）；夾子本身是 `0 40px 60px -30px rgba(0,0,0,0.9)` 壓在桌面上。接在檔案卡後面的白紙上移 18px 藏進卡下（`z-index` 卡 2、紙 1）。固定物有自己的影子：長尾夾與鐵夾是金屬漸層加 `0 3px 6px -2px` 深影，迴紋針是 `drop-shadow(0 2px 2px)`，膠帶是半透明米白加 1px 白內框。文件不做懸停位移；只有標籤與封面按鈕會抬起。

### Named Rules
**The Real Paper Rule.** 每件文件有傾角、有影、有 1px 厚度；不用描邊做深度，不用同一個影子疊兩層紙。手機上傾角歸零，影子保留。

## Shapes

紙是方角的：文件、記錄單、檔案卡、警示紙、便條、拍立得、名片全部 0 圓角；只有夾子（6px）、封面（4px／右上 10px）、索引標籤前緣（7px）、封面標籤（6px）與印章（4px）有圓角，那些是紙以外的東西或印刷品。歪斜：文件 ±0.3 到 0.5°、卡 ±0.5 到 0.6°、便條 ±0.5 到 0.7°、警示紙 -1.1°、拍立得 -1.2 到 -1.6°、封面標籤 -0.4°、橫帶 0.6°、印章 -12°（行內 -6°）。打孔：卷首白紙左緣兩個 13px 的圓洞（牛皮紙暗面色、內陰影），上下對稱於紙的中線。

## Components

### Buttons
只有封面的「翻開卷宗 ▸」：白紙色、Courier 700 14px／0.12em、1px 深邊、-1°，懸停抬 2px。

### Cover（合上的夾子）
`.cover`：牛皮紙、頂邊長尾夾（`ui.BULLDOG`：圓環、兩臂、夾口）、右上角夾子本身的標籤耳（`::before`）、右緣綠色檔案標籤紙（`.foldertab`，Courier 直排「EBERRON FILES · 艾伯倫檔案」）、正面的印刷標籤（`.label`：局名、分部線、主題「艾伯倫」、檔號與建檔日）、一行手寫（`.penned`）、「機密」橫帶（`.band`：紅底、黑塊、紅字、打字機副標）、底邊紅色迴紋針（`ui.paperclip("clip paper")`）。手機：標籤耳與檔案標籤紙隱藏。

### Document（白紙）
`ui.doc(title, title_en, body, ref, stamp, cls, lead, bureau, tilt)`：公文紙；`cls` 可加 `head`（卷首，32px 標題）、`punched`（打孔，左內距 56px）、`cream`（米色紙）、`wide`（放寬正文）、`attached`（接在檔案卡後）。右上角至多一枚章；折頁碼在右下。

### Form（記錄單）
`ui.form(title, title_en, rows, ref, no, lead, log, table, foot, prose, stamp, tilt, plain_log)`：雙線標題列與右側編號；`rows` 是欄位列（值 ≤ 30 字且無標記時自動改手寫）；`log` 是條目列（鍵／事項／內文，鍵用 Courier 朱色）；`table` 放 `ledger`；`prose` 段落；`foot` 腳註。

### Card（紅色檔案卡）＋ Attached
`ui.card(name, name_en, fields, line, stamp, tilt)`：紅卡、左緣鐵夾（`ui.BINDER`）、名稱與原名、一句話、`fields` 欄位格（`repeat(auto-fit, minmax(210px, 1fr))`）；卡上的章用米色。`emblem=` 可貼一張小相片在卡的右上角（`.emblem`：122px 寬、白色相紙邊、2°、頂邊膠帶；卡文字區右側留 190px），像檔案卡上的證件照，五國的國旗就貼在這裡；章壓在相片上緣。正文放在 `ui.attached(body, ref)` 的白紙上，白紙上移藏進卡下。

### Slip（警示紙）
`ui.slip(title, title_en, body, stamp)`：黃紙、頂邊黑色虛線帶、-1.1°、最寬 560px。

### Memo（便條）
`ui.note(label, text, hand_written)`：米色小紙、頂邊膠帶、標籤朱色並自帶全形冒號；`ui.memos([...])` 並排成格（220px 起），奇偶張傾角相反。

### Business Cards（名片）
`ui.bizcards(items, index)`：牛皮紙名片（上緣打字機小標、名稱、原名、幾行「標籤 值」）或白色索引卡（`index=True`，第一條紅線、其餘淡橫線）。`auto-fill, minmax(230px, 1fr)`。

### Polaroid & Pinboard（拍立得與方格紙）
`ui.pinboard(*polaroids)`：方格紙，拍立得以 flex 並排、置中。`ui.polaroid(inner, caption, typed, tilt, tall)`：白框相紙、頂邊膠帶、圖說手寫（第二行 `typed` 打字機）；`inner` 是 `ui.photo()` 的 `<img>` 或 `plate()` 的 SVG。橫幅相片在方格紙上最寬 640px、最高 520px（超出裁切）；`tall=True` 的直幅相片（剖面圖、海報）保留全高、最寬 430px。拍立得也可以直接放進白紙文件的正文開頭：它會浮在正文右側（最寬 280px，1.2°），像夾在紙上的一張照片；手機上回到正文上方置中。`small=True` 的相片最寬 330px，讓兩張並排在同一張方格紙上。圖說永遠只有相片那麼寬，長句往下折行，不會把相紙撐寬。

### Seal（印章）
`.stamp`：3px 雙線朱框、4px 圓角、900、-12°、`multiply`、`#ink-seal` 印泥濾鏡；文件與記錄單右上角 15px；檔案卡上米色、`normal` 混合；行內章 `stamp_inline()` 12px／-6°／`#ink-fine`。

### Ledger（打字機表）
`ui.ledger(cols, rows)`：欄頭朱色 600 13px／0.1em、2px 墨底線；格 9px 10px、淡線分列；數字欄 Courier `tabular-nums`。在記錄單裡左右各留 30px。

### Navigation
索引標籤軌與手機標籤列，見 Layout。封面沒有各卷標籤頭；翻開卷宗的連結捲到第一件文件（`#docs`）。

## Do's and Don'ts

### Do:
- **Do** 每一卷用 `page(...)` 把文件裝進同一個夾子；卷首一張打孔白紙加局處線。
- **Do** 一個實體一張紅色檔案卡加一張接在後面的白紙；表格與編號清單用記錄單；同類小項用名片；警告用黃紙；附註用便條；圖用拍立得貼在方格紙上。
- **Do** 給每件文件一個小傾角（`tilt=`），相鄰文件方向相反；手機上會自動歸零。
- **Do** 手寫只用在短欄位、便條、圖說、封面一句話。
- **Do** 每個專有名詞第一次出現時，用 `en()` 把英文原名以打字機字體跟在中文後面；卡與名片上另起一行。
- **Do** 新增含新字的內容後跑 `tools/build_fonts.py`；四個字檔都會重建。
- **Do** 尊重 `prefers-reduced-motion`：關掉橫帶、首件文件與章的入場動畫，以及標籤與按鈕的位移。

### Don't:
- **Don't** 在同一頁放兩件相鄰且同格式的文件；也不要把長段正文放在檔案卡、名片或便條上。
- **Don't** 用整片紅做任何不是檔案卡或封面橫帶的東西；不要把黃色用在警示紙以外。
- **Don't** 在紙上畫框做層級；要分層就換一種紙、疊一張紙、貼一張便條。
- **Don't** 用手寫字型排正文，或用宋體排表單的欄名與編號。
- **Don't** 給紙圓角；圓角只屬於夾子、標籤、印章與封面標籤。
- **Don't** 在 900px 以下顯示側邊標籤軌；行動版只用頂端橫向標籤列。
- **Don't** 用圖示字型補畫面；固定物只有長尾夾、鐵夾、迴紋針、膠帶四種，全部是 CSS 或 SVG 路徑。

## 追加零件（2026-10-06）

- **卷內目錄索引卡 `.toc`**：夾子最上面一張牛皮紙小卡（`--kraft-light`、纖維紋、1px 黑邊加 `--lift`），Courier 的「卷內目錄」小標與 `01`、`02` 朱紅編號，標題用宋體、底下一條點線，hover 變實線。由 `ui.folder()` 自動產生，只在三件以上有標題的文件時出現；錨點 `#sec-N`，捲動用 `scroll-behavior: smooth`（減少動態時關掉），每件文件 `scroll-margin-top: 16px`。
- **回頂端小籤 `.totop`**：固定在右下角的 40px 牛皮紙方籤（桌面避開標籤軌，`right: 152px`；手機 `right: 14px`），只有一個「▲」，hover 上浮 2px。
- **手機堆疊表 `.ledger.stack`**：三欄以上的打字機表在 ≤ 900px 改成一列一張：表頭藏起來，每列底下一條 `--rule`，第一欄粗體當標題，其餘欄前面印 Courier 朱紅小字欄名（`data-label`），數字欄與短值（`.short`，去標籤後 ≤ 14 字）並排成一行。
- **術語表**：詞條右側 Courier 小字印出處卷（`.src`，手機改到詞條下一行）；搜尋命中處 `<mark>` 用警示紙黃 55% 標底；找不到時朱紅一行 `.nohit`。
- **字型預算**：正文 400 全字集約 790 KB；600／900 與手寫體只含實際顯示過的字（各約 200／200／170 KB），總量約 1.4 MB。缺字落回 Google Fonts 同名同字重的後備字型。
- **地標清單的位置小字 `.where`**：地名與英文後面接一段 Courier 灰字（層區 · 城區），桌面同一行不折、手機換到下一行。四大犯罪組織用紅色檔案卡＋白紙（欄位：性質、地盤、首領；白紙上兩張便條「他們要什麼」「怎麼找上玩家」），與第二卷諸國、第六卷組織同一套零件。
