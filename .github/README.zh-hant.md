🌐｜[English](./README.md)　[中文](./README.zh-hant.md)

# <div align="center"><img src="../SVG_Alt.svg" width=48 height=48 /><br />SVG圖示資源庫</div>

<div align="center">
  <code>hugoalh/Library.SVG.Icon</code><br />
  <img src="https://img.shields.io/github/languages/count/hugoalh/Library.SVG.Icon?style=flat-square&logo=github" />
  <img src="https://img.shields.io/github/languages/top/hugoalh/Library.SVG.Icon?style=flat-square&logo=github" />
  <img src="https://img.shields.io/github/repo-size/hugoalh/Library.SVG.Icon?style=flat-square&logo=github" />
  <img src="https://img.shields.io/github/watchers/hugoalh/Library.SVG.Icon?style=flat-square&logo=github" />
  <img src="https://img.shields.io/github/stars/hugoalh/Library.SVG.Icon?style=flat-square&logo=github" />
  <img src="https://img.shields.io/github/forks/hugoalh/Library.SVG.Icon?style=flat-square&logo=github" />
</div>

<table>
  <tr>
    <td align="center">
      <b>作者、貢獻者</b><br />
      <img src="https://img.shields.io/github/contributors/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />
    </td>
    <td><a href="https://github.com/hugoalh">hugoalh</a></td>
  </tr>
  <tr>
    <td align="center"><b>授權</b></td>
    <td><a href="../LICENSE.zh-hant.md">CC0 1.0</a></td>
  </tr>
  <tr>
    <td align="center"><b>問題</b></td>
    <td>
      <b>開啟：</b><img src="https://img.shields.io/github/issues-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />；<b>已關閉：</b><img src="https://img.shields.io/github/issues-closed-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />
    </td>
  </tr>
  <tr>
    <td align="center"><b>合併請求</b></td>
    <td>
      <b>開啟：</b><img src="https://img.shields.io/github/issues-pr-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />；<b>已關閉：</b><img src="https://img.shields.io/github/issues-pr-closed-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />
    </td>
  </tr>
</table>
</table>

## 📜 說明

一個SVG圖示資源庫。<a href="https://hugoalh.github.io/Library.SVG.Icon">按此以使用快速瀏覽（英文）。</a>

## ✍ 開始使用

### 網路基礎

此方法適用於：

- 你想使圖示保持在最新版本，
- 你的專案需要在線運作（互聯網連接），
- 你只想測試，或者
- 你想要一個迷你的專案。

`*.html`

```html
<!-- 使用<img>，但是不能夠控制色彩。 --->
<img src="https://hugoalh.github.io/Library.SVG.Icon/{{圖示名稱}}.svg" />

<!-- 使用<svg>，能夠控制色彩。 --->
<svg viewBox="0 0 24 24">
  <use xlink:href="https://hugoalh.github.io/Library.SVG.Icon/{{圖示名稱}}.svg"></use>
</svg>
```

### Git模組（Git Submodule）

此方法適用於：

- you do not want the update(s) may make a mess,
- you need to control which version of release you want,
- your project can run offline (exclude progressive web application due they can cache the icons), or
- your project is required to run offline(no internet connection).

#### 步驟

<ol>
  <li>Require <a href="https://git-scm.com/">Git</a>, then use Terminal/Bush to locate your project directory.</li>
  <li>Type in <code>git submodule add git+https://github.com/hugoalh/Library.SVG.Icon.git {{NewFolderName}}</code>, and it will clone this repository.</li>
  <li>For updating, type in <code>git submodule update --remote --merge</code>.</li>
</ol>

#### 用法

*There has many ways to use, here is just an example.*

`*.html`

```html
<!-- 使用<img>，但是不能夠控制色彩。 --->
<img src="{{NewFolderName}}/{{圖示名稱}}.svg" />

<!-- 使用<svg>，能夠控制色彩。 --->
<svg viewBox="0 0 24 24">
  <use xlink:href="{{NewFolderName}}/{{圖示名稱}}.svg"></use>
</svg>
```

## 🐛 問題

在這個專案中發現任何問題？通過[GitHub](https://github.com/hugoalh/Library.SVG.Icon/issues)提交該問題。
