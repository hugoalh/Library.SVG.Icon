# <div align="center">SVG圖示資源庫</div>

🌐｜<a href="./README.md">English</a>　<a href="./README.zh-hant.md">中文</a>

<table>
  <tr>
    <td align="center"><strong>索引</strong></td>
    <td><a href="https://github.com/hugoalh/Library.SVG.Icon">hugoalh/Library.SVG</a></td>
  </tr>
  <tr>
    <td align="center">
      <strong>作者、貢獻者</strong><br />
      <img src="https://img.shields.io/github/contributors/hugoalh/Library.SVG.Icon?color=000000&label=%20" />
    </td>
    <td><a href="https://github.com/hugoalh">hugoalh</a></td>
  </tr>
  <tr>
    <td align="center"><strong>授權</strong></td>
    <td>
      <a href="../LICENSE.zh-hant.md">CC0 1.0</a>
    </td>
  </tr>
</table>

## 📜 說明

一個SVG圖示資源庫。<a href="https://hugoalh.github.io/Library.SVG.Icon">按此以使用快速瀏覽（英文）。</a>

## ✍ 開始使用

### 網路基礎

此方法適用於：

- you want the icons are up to date, 
- your project is required to run online(internet connection),
- you want to test, or
- you want to have a minified project.

```html
<!-- HTML --->

<img src="https://hugoalh.github.io/Library.SVG.Icon/{{IconName}}.svg" />

<svg viewBox="0 0 24 24">
  <use xlink:href="https://hugoalh.github.io/Library.SVG.Icon/{{IconName}}.svg"></use>
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
  <li>Open/Download <a href="https://git-scm.com/">Git</a>, then use Terminal/Bush to locate your project directory.</li>
  <li>Type in <code>git submodule add git+https://github.com/hugoalh/Library.SVG.Icon.git {{NewFolderName}}</code>, and it will clone this repository</li>
  <li>For updating, type in <code>git submodule update --remote --merge</code></li>
</ol>

#### 用法

There has many ways to use, here is just an example.

```html
<!-- HTML --->

<img src="{{NewFolderName}}/{{IconName}}.svg" />

<svg viewBox="0 0 24 24">
  <use xlink:href="{{NewFolderName}}/{{IconName}}.svg"></use>
</svg>
```
