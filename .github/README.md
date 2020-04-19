🌐｜[English](./README.md)　[中文](./README.zh-hant.md)

# <div align="center"><img src="../SVG_Alt.svg" width=48 height=48 /><br />SVG Icon Library</div>

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
      <b>Author & Contributor</b><br />
      <img src="https://img.shields.io/github/contributors/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />
    </td>
    <td><a href="https://github.com/hugoalh">hugoalh</a></td>
  </tr>
  <tr>
    <td align="center"><b>License</b></td>
    <td><a href="../LICENSE.md">CC0 1.0</a></td>
  </tr>
  <tr>
    <td align="center"><b>Issue</b></td>
    <td>
      <b>Open: </b><img src="https://img.shields.io/github/issues-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />; <b>Closed: </b><img src="https://img.shields.io/github/issues-closed-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />
    </td>
  </tr>
  <tr>
    <td align="center"><b>Pull Request</b></td>
    <td>
      <b>Open: </b><img src="https://img.shields.io/github/issues-pr-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />; <b>Closed: </b><img src="https://img.shields.io/github/issues-pr-closed-raw/hugoalh/Library.SVG.Icon?style=flat-square&color=000000&label=%20" />
    </td>
  </tr>
</table>

## 📜 Description

A SVG icon library. <a href="https://hugoalh.github.io/Library.SVG.Icon">Click here to use the web view.</a>

## ✍ Getting Started

### Web Based

This method is suitable when:

- you want the icons are up to date, 
- your project is required to run online(internet connection),
- you want to test, or
- you want to have a minified project.

`*.html`

```html
<!-- Using <img>, but cannot control colour. --->
<img src="https://hugoalh.github.io/Library.SVG.Icon/{{IconName}}.svg" />

<!-- Using <svg>, can control colour. --->
<svg viewBox="0 0 24 24">
  <use xlink:href="https://hugoalh.github.io/Library.SVG.Icon/{{IconName}}.svg"></use>
</svg>
```

### Git Submodule

This method is suitable when:

- you do not want the update(s) may make a mess,
- you need to control which version of release you want,
- your project can run offline (exclude progressive web application due they can cache the icons), or
- your project is required to run offline(no internet connection).

#### Step

<ol>
  <li>Require <a href="https://git-scm.com/">Git</a>, then use Terminal/Bush to locate your project directory.</li>
  <li>Type in <code>git submodule add git+https://github.com/hugoalh/Library.SVG.Icon.git {{NewFolderName}}</code>, and it will clone this repository.</li>
  <li>For updating, type in <code>git submodule update --remote --merge</code>.</li>
</ol>

#### Usage

*There has many ways to use, here is just an example.*

`*.html`

```html
<!-- Using <img>, but cannot control colour. --->
<img src="{{NewFolderName}}/{{IconName}}.svg" />

<!-- Using <svg>, can control colour. --->
<svg viewBox="0 0 24 24">
  <use xlink:href="{{NewFolderName}}/{{IconName}}.svg"></use>
</svg>
```

## 🐛 Issue

Found any issue in this project? Submit the issue via [GitHub](https://github.com/hugoalh/Library.SVG.Icon/issues).
