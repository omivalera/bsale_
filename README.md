<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Bsale_ Backend Doc</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
}

.simple-table-header {
	background: rgb(247, 246, 243);
	color: black;
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-opaquegray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="1cd6053b-1210-4b07-bc99-8b85e03d8273" class="page sans"><header><img class="page-cover-image" src="https://www.notion.so/images/page-cover/woodcuts_7.jpg" style="object-position:center 70%"/><div class="page-header-icon page-header-icon-with-cover"><span class="icon">👾</span></div><h1 class="page-title">Bsale_ Backend Doc</h1></header><div class="page-body"><p id="13949652-c68f-48d5-9cf4-c75077736ecd" class="">La implementación de esta API-REST fue mediante Django-rest y conectada una base de datos MySQL.</p><p id="936ff534-e272-47d0-949f-bd0dc2940002" class="">
</p><p id="1a3559e7-10c1-409a-9402-56541e400f03" class="">
</p><p id="e8dd0c40-4b25-4103-adbe-a27d4836623e" class="">
</p><h2 id="c2ad5d53-d4df-4d2e-9696-f26be76bf936" class="">Endpoints</h2><p id="8a26900d-4d6d-47c0-ad26-9088c26e70ae" class="">
</p><p id="3d312842-d492-49cd-ae99-cdcecce1637e" class="">
</p><pre id="4d2ce2fd-60ae-4412-b1a6-a0cb2a3e658d" class="code code-wrap"><code>{
    &quot;products&quot;: &quot;https://testapibsale.herokuapp.com/products/?format=api&quot;,
    &quot;groups&quot;: &quot;https://testapibsale.herokuapp.com/categories/?format=api&quot;,
    &quot;categories&quot;: &quot;https://testapibsale.herokuapp.com/categories/?format=api&quot;
}</code></pre><p id="002cff91-c9f0-46f9-8e91-927d2671c86a" class="">
</p><p id="bf93d936-e233-4062-9f52-a635e46c9509" class=""><mark class="highlight-red">/products/ </mark></p><ul id="05b2d7bb-2a28-43b1-bc5b-508b031160a1" class="bulleted-list"><li style="list-style-type:disc">Se filtra por productos </li></ul><ul id="9f1fe3e3-d89a-4de4-8e9d-8fa3735d1e5d" class="bulleted-list"><li style="list-style-type:disc">Se asignaron 12 cards por cada pagina</li></ul><ul id="e9aed7b1-e84c-458a-a442-c884fdea733e" class="bulleted-list"><li style="list-style-type:disc">Link donde visualizar = </li></ul><figure id="871c5b6d-3f34-420f-942c-8f8b9ec21c1a"><a href="https://testapibsale.herokuapp.com/products/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Product List</div><div class="bookmark-description">&quot;count&quot;: 57, &quot;next&quot;: &quot;https://testapibsale.herokuapp.com/products/?page=2&quot;, &quot;previous&quot;: null, &quot;results&quot;: [ { &quot;id&quot;: 5, &quot;name&quot;: &quot;ENERGETICA MR BIG&quot;, &quot;url_image&quot;: &quot;https://dojiw2m9tvv09.cloudfront.net/11132/product/misterbig3308256.jpg&quot;, &quot;price&quot;: 1490.0, &quot;discount&quot;: 20, &quot;category&quot;: { &quot;id&quot;: 1, &quot;name&quot;: &quot;bebida energetica&quot; } }, { &quot;id&quot;: 6, &quot;name&quot;: &quot;ENERGETICA RED BULL&quot;, &quot;url_image&quot;: &quot;https://dojiw2m9tvv09.cloudfront.net/11132/product/redbull8381.jpg&quot;, &quot;price&quot;: 1490.0, &quot;discount&quot;: 0, &quot;category&quot;: { &quot;id&quot;: 1, &quot;name&quot;: &quot;bebida energetica&quot;</div></div><div class="bookmark-href">https://testapibsale.herokuapp.com/products/</div></div></a></figure><p id="9ecb258a-a947-4d0c-bf24-4dcf73e3bdcb" class="">
</p><p id="735328ac-bd78-443c-a4a2-5ea4ddb72a9a" class="">
</p><p id="c54a955f-ae64-4a0c-8996-8bc53d0dd189" class=""><mark class="highlight-red">/groups/</mark></p><ul id="9544257b-341b-4faa-852b-3be02c2e3cad" class="bulleted-list"><li style="list-style-type:disc">Se filtra por grupo</li></ul><ul id="a7be5ef4-afd8-4a0c-a196-d26f4237f5a6" class="bulleted-list"><li style="list-style-type:disc">link donde visualizar = </li></ul><figure id="f70c30e2-12c0-4a9c-9670-5215bf166a84"><a href="https://testapibsale.herokuapp.com/categories/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Category List</div></div><div class="bookmark-href">https://testapibsale.herokuapp.com/categories/</div></div></a></figure><p id="48511b5e-0ecb-4bd5-8e04-028aecbf9f76" class="">
</p><p id="9379d9d6-3bdf-4dcf-8703-f7f840512cf1" class="">
</p><p id="605b03b5-2d23-4f36-9b5f-5a8483629250" class="">
</p><p id="c2ed0948-f6ae-4b92-b76b-e7733c9a439d" class=""><mark class="highlight-red">/categories/</mark></p><ul id="e9e73ce5-c637-40e2-9315-75b017eca311" class="bulleted-list"><li style="list-style-type:disc">Se filtra por categoría</li></ul><ul id="1c75bb50-c203-4b1a-93ec-4d9e253d46ba" class="bulleted-list"><li style="list-style-type:disc">Link donde visualizar = </li></ul><figure id="6a447297-e20b-405c-b041-5f9ff2a095e1"><a href="https://testapibsale.herokuapp.com/categories/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Category List</div></div><div class="bookmark-href">https://testapibsale.herokuapp.com/categories/</div></div></a></figure><p id="9a9bd40c-e3e8-4dd4-9c36-0c4dc1d24b99" class="">
</p><p id="378875bc-0c42-4162-8f50-14745d4b8053" class="">
</p><h1 id="9957ddc6-971f-4d57-982b-a79ee4b3cf8d" class=""><mark class="highlight-teal"><strong>Instalación en LOCAL</strong></mark></h1><p id="c7e5857a-8c36-4d94-b789-f83c7a0a94d3" class="">Al clonar el repositorio y antes de inicializar el server es <mark class="highlight-yellow">MUY IMPORTANTE</mark></p><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="90e832e6-1666-4fab-ad48-89b20705a977"><div style="font-size:1.5em"><span class="icon">🚨</span></div><div style="width:100%">Eliminar el archivo <code><strong>bs-config.js</strong></code><strong> este forma parte del deploy en remoto </strong></div></figure><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="86ad9ebb-e5d0-4a0d-a0a6-df12f3624cd1"><div style="font-size:1.5em"><span class="icon">🚨</span></div><div style="width:100%">Cambiar en el archivo <code>scripts.js</code>la variable <code>base_URL</code> que vendrá con el valor del deploy. 
Se debe colocar en su lugar  “http://127.0.0.1:8000/”</div></figure><p id="66596d2e-5417-4959-8012-27f1a3fc4f83" class="">
</p><p id="2d2518ed-6116-49fd-873f-18122ea10674" class="">
</p><p id="8b69379e-b4d9-4dda-8edf-403c7bc8a5c6" class="">Instalar las dependencias con </p><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="b08eab37-7b7d-4ef1-8340-a9f29e103062"><div style="font-size:1.5em"><span class="icon">🖥️</span></div><div style="width:100%"><code>pip install -r requirements.txt</code></div></figure><p id="e480463b-138a-473e-aa02-d7cc1ac8e228" class="">
</p><p id="701cca4c-9163-4d46-bfaa-40624b120479" class="">Se ejecuta el server</p><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="6a5bbfb9-64cb-4ecf-9f42-254f46484d49"><div style="font-size:1.5em"><span class="icon">🖥️</span></div><div style="width:100%"><code>python manage.py runserver</code></div></figure><p id="832f313e-7f4a-459f-868a-8508ec4e7ffe" class="">
</p><p id="da986748-463f-48ba-805a-2b6bd4ef62ab" class="">Ve al navegador y entra en </p><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="4dcc1ee0-0b12-4bad-80b4-6a3a1920fb26"><div style="font-size:1.5em"><span class="icon">🖥️</span></div><div style="width:100%"><mark class="highlight-teal">http://127.0.0.1:8000/</mark></div></figure><p id="7999aeb4-4564-48a8-9c47-65ca6566382c" class="">
</p></div></article></body></html>