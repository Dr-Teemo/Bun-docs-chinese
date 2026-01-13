<p align="center">
  <a href="https://bun.com"><img src="https://github.com/user-attachments/assets/50282090-adfd-4ddb-9e27-c30753c6b161" alt="Logo" height="170" /></a>
</p>
<h1 align="center">Bun</h1>

<p align="center">
<a href="https://bun.com/discord" target="_blank"><img height="20" src="https://img.shields.io/discord/876711213126520882" /></a>
<img src="https://img.shields.io/github/stars/oven-sh/bun" alt="stars" />
<a href="https://twitter.com/jarredsumner/status/1542824445810642946"><img src="https://img.shields.io/static/v1?label=speed&message=fast&color=success" alt="Bun speed" /></a>
</p>

<div align="center">
  <a href="https://teemo.mintlify.app/">中文文档</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://discord.com/invite/CXdq2DP29u">Discord</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://github.com/oven-sh/bun/issues/new">问题反馈</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://github.com/oven-sh/bun/issues/159">路线图</a>
  <br />
</div>

### [阅读文档 →](https://teemo.mintlify.app/)

## 什么是Bun？

Bun是一个JavaScript和TypeScript应用的一体化工具包。它作为一个名为`bun`的单一可执行文件发布。

其核心是_Bun运行时_，这是一个快速的JavaScript运行时，设计为**Node.js的直接替代品**。它使用Zig编写，底层由JavaScriptCore驱动，大大减少了启动时间和内存使用。

```bash
bun run index.tsx             # 开箱即支持TS和JSX
```

`bun`命令行工具还实现了测试运行器、脚本运行器和Node.js兼容的包管理器。对于开发，你不再需要1000个node_modules，只需要`bun`即可。Bun内置的工具比现有选项快得多，并且可以在现有的Node.js项目中使用，几乎不需要修改。

```bash
bun test                      # 运行测试
bun run start                 # 运行package.json中的`start`脚本
bun install <pkg>             # 安装一个包
bunx cowsay 'Hello, world!'   # 执行一个包
```

## 安装

Bun支持Linux(x64和arm64)、macOS(x64和Apple Silicon)和Windows(x64)。

> **Linux用户** — 强烈推荐内核版本5.6或更高，但最低要求是5.1。

> **x64用户** — 如果看到"illegal instruction"或类似错误，请查看我们的[CPU要求](https://teemo.mintlify.app/docs/installation#cpu-requirements-and-baseline-builds)

```sh
# 使用安装脚本(推荐)
curl -fsSL https://bun.com/install | bash

# 在windows上
powershell -c "irm bun.sh/install.ps1 | iex"

# 使用npm
npm install -g bun

# 使用Homebrew
brew tap oven-sh/bun
brew install bun

# 使用Docker
docker pull oven/bun
docker run --rm --init --ulimit memlock=-1:-1 oven/bun
```

### 升级

要升级到最新版本的Bun，请运行：

```sh
bun upgrade
```

Bun每次提交到`main`分支时都会自动发布一个canary版本。要升级到最新的canary版本，请运行：

```sh
bun upgrade --canary
```

[查看canary版本](https://github.com/oven-sh/bun/releases/tag/canary)


## 贡献

请参阅[项目 > 贡献](https://teemo.mintlify.app/project/contributing)指南开始为Bun做贡献。

## 许可证

请参阅[项目 > 许可证](https://teemo.mintlify.app/project/license)页面了解有关Bun许可证的信息。