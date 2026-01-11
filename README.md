<p align="center">
  <a href="https://bun.com"><img src="https://github.com/user-attachments/assets/50282090-adfd-4ddb-9e27-c30753c6b161" alt="Logo" height=170></a>
</p>
<h1 align="center">Bun</h1>

<p align="center">
<a href="https://bun.com/discord" target="_blank"><img height=20 src="https://img.shields.io/discord/876711213126520882" /></a>
<img src="https://img.shields.io/github/stars/oven-sh/bun" alt="stars">
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

## 快速链接

- 介绍
  - [什么是Bun?](https://teemo.mintlify.app/index)
  - [安装](https://teemo.mintlify.app/installation)
  - [快速开始](https://teemo.mintlify.app/quickstart)
  - [TypeScript](https://teemo.mintlify.app/typescript)

- 模板
  - [`bun init`](https://teemo.mintlify.app/cli/init)
  - [`bun create`](https://teemo.mintlify.app/cli/bun-create)

- CLI
  - [`bun upgrade`](https://teemo.mintlify.app/cli/bun-upgrade)

- 运行时
  - [`bun run`](https://teemo.mintlify.app/cli/run)
  - [文件类型 (加载器)](https://teemo.mintlify.app/runtime/loaders)
  - [TypeScript](https://teemo.mintlify.app/runtime/typescript)
  - [JSX](https://teemo.mintlify.app/runtime/jsx)
  - [环境变量](https://teemo.mintlify.app/runtime/environment-variables)
  - [Bun APIs](https://teemo.mintlify.app/runtime/bun-apis)
  - [Web APIs](https://teemo.mintlify.app/runtime/web-apis)
  - [Node.js兼容性](https://teemo.mintlify.app/runtime/nodejs-compat)
  - [单文件可执行程序](https://teemo.mintlify.app/bundler/executables)
  - [插件](https://teemo.mintlify.app/runtime/plugins)
  - [监听模式 / 热重载](https://teemo.mintlify.app/runtime/watch-mode)
  - [模块解析](https://teemo.mintlify.app/runtime/modules)
  - [自动导入](https://teemo.mintlify.app/runtime/autoimport)
  - [bunfig.toml](https://teemo.mintlify.app/runtime/bunfig)
  - [调试器](https://teemo.mintlify.app/runtime/debugger)
  - [$ Shell](https://teemo.mintlify.app/runtime/shell)

- 包管理器
  - [`bun install`](https://teemo.mintlify.app/cli/install)
  - [`bun add`](https://teemo.mintlify.app/cli/add)
  - [`bun remove`](https://teemo.mintlify.app/cli/remove)
  - [`bun update`](https://teemo.mintlify.app/cli/update)
  - [`bun link`](https://teemo.mintlify.app/cli/link)
  - [`bun unlink`](https://teemo.mintlify.app/cli/unlink)
  - [`bun pm`](https://teemo.mintlify.app/cli/pm)
  - [`bun outdated`](https://teemo.mintlify.app/cli/outdated)
  - [`bun publish`](https://teemo.mintlify.app/cli/publish)
  - [`bun patch`](https://teemo.mintlify.app/install/patch)
  - [`bun patch-commit`](https://teemo.mintlify.app/cli/patch-commit)
  - [全局缓存](https://teemo.mintlify.app/install/cache)
  - [工作区](https://teemo.mintlify.app/install/workspaces)
  - [生命周期脚本](https://teemo.mintlify.app/install/lifecycle)
  - [过滤](https://teemo.mintlify.app/cli/filter)
  - [锁文件](https://teemo.mintlify.app/install/lockfile)
  - [范围和注册表](https://teemo.mintlify.app/install/registries)
  - [覆盖和解析](https://teemo.mintlify.app/install/overrides)
  - [`.npmrc`](https://teemo.mintlify.app/install/npmrc)

- 打包器
  - [`Bun.build`](https://teemo.mintlify.app/bundler)
  - [加载器](https://teemo.mintlify.app/bundler/loaders)
  - [插件](https://teemo.mintlify.app/bundler/plugins)
  - [宏](https://teemo.mintlify.app/bundler/macros)
  - [与esbuild比较](https://teemo.mintlify.app/bundler/vs-esbuild)
  - [单文件可执行程序](https://teemo.mintlify.app/bundler/executables)
  - [CSS](https://teemo.mintlify.app/bundler/css)
  - [HTML](https://teemo.mintlify.app/bundler/html)
  - [热模块替换(HMR)](https://teemo.mintlify.app/bundler/hmr)
  - [使用HTML导入的全栈](https://teemo.mintlify.app/bundler/fullstack)

- 测试运行器
  - [`bun test`](https://teemo.mintlify.app/cli/test)
  - [编写测试](https://teemo.mintlify.app/test/writing)
  - [监听模式](https://teemo.mintlify.app/test/hot)
  - [生命周期钩子](https://teemo.mintlify.app/test/lifecycle)
  - [模拟](https://teemo.mintlify.app/test/mocks)
  - [快照](https://teemo.mintlify.app/test/snapshots)
  - [日期和时间](https://teemo.mintlify.app/test/time)
  - [DOM测试](https://teemo.mintlify.app/test/dom)
  - [代码覆盖率](https://teemo.mintlify.app/test/coverage)
  - [配置](https://teemo.mintlify.app/test/configuration)
  - [发现](https://teemo.mintlify.app/test/discovery)
  - [报告器](https://teemo.mintlify.app/test/reporters)
  - [运行时行为](https://teemo.mintlify.app/test/runtime-behavior)

- 包运行器
  - [`bunx`](https://teemo.mintlify.app/cli/bunx)

- API
  - [HTTP服务器(`Bun.serve`)](https://teemo.mintlify.app/api/http)
  - [WebSockets](https://teemo.mintlify.app/api/websockets)
  - [Workers](https://teemo.mintlify.app/api/workers)
  - [二进制数据](https://teemo.mintlify.app/api/binary-data)
  - [流](https://teemo.mintlify.app/api/streams)
  - [文件I/O(`Bun.file`)](https://teemo.mintlify.app/api/file-io)
  - [import.meta](https://teemo.mintlify.app/api/import-meta)
  - [SQLite(`bun:sqlite`)](https://teemo.mintlify.app/api/sqlite)
  - [PostgreSQL(`Bun.sql`)](https://teemo.mintlify.app/api/sql)
  - [Redis(`Bun.redis`)](https://teemo.mintlify.app/api/redis)
  - [S3客户端(`Bun.s3`)](https://teemo.mintlify.app/api/s3)
  - [FileSystemRouter](https://teemo.mintlify.app/api/file-system-router)
  - [TCP套接字](https://teemo.mintlify.app/api/tcp)
  - [UDP套接字](https://teemo.mintlify.app/api/udp)
  - [全局对象](https://teemo.mintlify.app/api/globals)
  - [$ Shell](https://teemo.mintlify.app/runtime/shell)
  - [子进程(spawn)](https://teemo.mintlify.app/api/spawn)
  - [转换器(`Bun.Transpiler`)](https://teemo.mintlify.app/api/transpiler)
  - [哈希](https://teemo.mintlify.app/api/hashing)
  - [颜色(`Bun.color`)](https://teemo.mintlify.app/api/color)
  - [控制台](https://teemo.mintlify.app/api/console)
  - [FFI(`bun:ffi`)](https://teemo.mintlify.app/api/ffi)
  - [C编译器(`bun:ffi` cc)](https://teemo.mintlify.app/api/cc)
  - [HTMLRewriter](https://teemo.mintlify.app/api/html-rewriter)
  - [测试(`bun:test`)](https://teemo.mintlify.app/api/test)
  - [Cookies(`Bun.Cookie`)](https://teemo.mintlify.app/api/cookie)
  - [工具](https://teemo.mintlify.app/api/utils)
  - [Node-API](https://teemo.mintlify.app/api/node-api)
  - [Glob(`Bun.Glob`)](https://teemo.mintlify.app/api/glob)
  - [语义化版本(`Bun.semver`)](https://teemo.mintlify.app/api/semver)
  - [DNS](https://teemo.mintlify.app/api/dns)
  - [fetch API扩展](https://teemo.mintlify.app/api/fetch)

## 指南

- 二进制
  - [将Blob转换为字符串](https://teemo.mintlify.app/guides/binary/blob-to-string)
  - [将Buffer转换为blob](https://teemo.mintlify.app/guides/binary/buffer-to-blob)
  - [将Blob转换为DataView](https://teemo.mintlify.app/guides/binary/blob-to-dataview)
  - [将Buffer转换为字符串](https://teemo.mintlify.app/guides/binary/buffer-to-string)
  - [将Blob转换为ReadableStream](https://teemo.mintlify.app/guides/binary/blob-to-stream)
  - [将Blob转换为Uint8Array](https://teemo.mintlify.app/guides/binary/blob-to-typedarray)
  - [将DataView转换为字符串](https://teemo.mintlify.app/guides/binary/dataview-to-string)
  - [将Uint8Array转换为Blob](https://teemo.mintlify.app/guides/binary/typedarray-to-blob)
  - [将Blob转换为ArrayBuffer](https://teemo.mintlify.app/guides/binary/blob-to-arraybuffer)
  - [将ArrayBuffer转换为Blob](https://teemo.mintlify.app/guides/binary/arraybuffer-to-blob)
  - [将Buffer转换为Uint8Array](https://teemo.mintlify.app/guides/binary/buffer-to-typedarray)
  - [将Uint8Array转换为Buffer](https://teemo.mintlify.app/guides/binary/typedarray-to-buffer)
  - [将Uint8Array转换为字符串](https://teemo.mintlify.app/guides/binary/typedarray-to-string)
  - [将Buffer转换为ArrayBuffer](https://teemo.mintlify.app/guides/binary/buffer-to-arraybuffer)
  - [将ArrayBuffer转换为Buffer](https://teemo.mintlify.app/guides/binary/arraybuffer-to-buffer)
  - [将ArrayBuffer转换为字符串](https://teemo.mintlify.app/guides/binary/arraybuffer-to-string)
  - [将Uint8Array转换为DataView](https://teemo.mintlify.app/guides/binary/typedarray-to-dataview)
  - [将Buffer转换为ReadableStream](https://teemo.mintlify.app/guides/binary/buffer-to-readablestream)
  - [将Uint8Array转换为ArrayBuffer](https://teemo.mintlify.app/guides/binary/typedarray-to-arraybuffer)
  - [将ArrayBuffer转换为Uint8Array](https://teemo.mintlify.app/guides/binary/arraybuffer-to-typedarray)
  - [将ArrayBuffer转换为数字数组](https://teemo.mintlify.app/guides/binary/arraybuffer-to-array)
  - [将Uint8Array转换为ReadableStream](https://teemo.mintlify.app/guides/binary/typedarray-to-readablestream)

- 生态系统
  - [使用React和JSX](https://teemo.mintlify.app/guides/ecosystem/react)
  - [在Bun中使用Gel](https://teemo.mintlify.app/guides/ecosystem/gel)
  - [在Bun中使用Prisma](https://teemo.mintlify.app/guides/ecosystem/prisma)
  - [向Bun应用添加Sentry](https://teemo.mintlify.app/guides/ecosystem/sentry)
  - [创建Discord机器人](https://teemo.mintlify.app/guides/ecosystem/discordjs)
  - [使用PM2作为守护进程运行Bun](https://teemo.mintlify.app/guides/ecosystem/pm2)
  - [在Bun中使用Drizzle ORM](https://teemo.mintlify.app/guides/ecosystem/drizzle)
  - [使用Nuxt和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/nuxt)
  - [使用Qwik和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/qwik)
  - [使用Astro和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/astro)
  - [使用Remix和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/remix)
  - [使用Vite和Bun构建前端](https://teemo.mintlify.app/guides/ecosystem/vite)
  - [使用Next.js和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/nextjs)
  - [使用systemd作为守护进程运行Bun](https://teemo.mintlify.app/guides/ecosystem/systemd)
  - [在Render上部署Bun应用程序](https://teemo.mintlify.app/guides/ecosystem/render)
  - [使用Hono和Bun构建HTTP服务器](https://teemo.mintlify.app/guides/ecosystem/hono)
  - [使用SvelteKit和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/sveltekit)
  - [使用SolidStart和Bun构建应用](https://teemo.mintlify.app/guides/ecosystem/solidstart)
  - [使用Elysia和Bun构建HTTP服务器](https://teemo.mintlify.app/guides/ecosystem/elysia)
  - [使用StricJS和Bun构建HTTP服务器](https://teemo.mintlify.app/guides/ecosystem/stric)
  - [使用Docker容器化Bun应用程序](https://teemo.mintlify.app/guides/ecosystem/docker)
  - [使用Express和Bun构建HTTP服务器](https://teemo.mintlify.app/guides/ecosystem/express)
  - [通过Drizzle ORM使用Neon Postgres](https://teemo.mintlify.app/guides/ecosystem/neon-drizzle)
  - [服务端渲染(SSR)React组件](https://teemo.mintlify.app/guides/ecosystem/ssr-react)
  - [使用Mongoose和Bun读写MongoDB数据](https://teemo.mintlify.app/guides/ecosystem/mongoose)
  - [使用Neon的Serverless Postgres与Bun](https://teemo.mintlify.app/guides/ecosystem/neon-serverless-postgres)

- HTMLRewriter
  - [使用HTMLRewriter提取网页链接](https://teemo.mintlify.app/guides/html-rewriter/extract-links)
  - [提取社交分享图片和Open Graph标签](https://teemo.mintlify.app/guides/html-rewriter/extract-social-meta)

- HTTP
  - [热重载HTTP服务器](https://teemo.mintlify.app/guides/http/hot)
  - [常见HTTP服务器用法](https://teemo.mintlify.app/guides/http/server)
  - [编写简单的HTTP服务器](https://teemo.mintlify.app/guides/http/simple)
  - [在HTTP服务器上配置TLS](https://teemo.mintlify.app/guides/http/tls)
  - [使用fetch发送HTTP请求](https://teemo.mintlify.app/guides/http/fetch)
  - [使用fetch()代理HTTP请求](https://teemo.mintlify.app/guides/http/proxy)
  - [启动HTTP服务器集群](https://teemo.mintlify.app/guides/http/cluster)
  - [将文件作为HTTP响应流式传输](https://teemo.mintlify.app/guides/http/stream-file)
  - [在Bun中使用Unix域套接字进行fetch](https://teemo.mintlify.app/guides/http/fetch-unix)
  - [通过HTTP使用FormData上传文件](https://teemo.mintlify.app/guides/http/file-uploads)
  - [使用异步迭代器的流式HTTP服务器](https://teemo.mintlify.app/guides/http/stream-iterator)
  - [使用Node.js流的流式HTTP服务器](https://teemo.mintlify.app/guides/http/stream-node-streams-in-bun)

- 安装
  - [添加依赖项](https://teemo.mintlify.app/guides/install/add)
  - [添加Git依赖项](https://teemo.mintlify.app/guides/install/add-git)
  - [添加Peer依赖项](https://teemo.mintlify.app/guides/install/add-peer)
  - [添加可信依赖项](https://teemo.mintlify.app/guides/install/trusted)
  - [添加开发依赖项](https://teemo.mintlify.app/guides/install/add-dev)
  - [添加tarball依赖项](https://teemo.mintlify.app/guides/install/add-tarball)
  - [添加可选依赖项](https://teemo.mintlify.app/guides/install/add-optional)
  - [生成与Yarn兼容的锁文件](https://teemo.mintlify.app/guides/install/yarnlock)
  - [使用工作区配置monorepo](https://teemo.mintlify.app/guides/install/workspaces)
  - [以不同名称安装包](https://teemo.mintlify.app/guides/install/npm-alias)
  - [在GitHub Actions中使用Bun安装依赖](https://teemo.mintlify.app/guides/install/cicd)
  - [在Artifactory中使用bun install](https://teemo.mintlify.app/guides/install/jfrog-artifactory)
  - [配置git以diff Bun的lockb锁文件](https://teemo.mintlify.app/guides/install/git-diff-bun-lockfile)
  - [覆盖bun install的默认npm注册表](https://teemo.mintlify.app/guides/install/custom-registry)
  - [使用Azure Artifacts npm注册表与bun install](https://teemo.mintlify.app/guides/install/azure-artifacts)
  - [从npm install迁移到bun install](https://teemo.mintlify.app/guides/install/from-npm-install-to-bun-install)
  - [为组织范围配置私有注册表与bun install](https://teemo.mintlify.app/guides/install/registry-scope)

- 进程
  - [从stdin读取](https://teemo.mintlify.app/guides/process/stdin)
  - [监听CTRL+C](https://teemo.mintlify.app/guides/process/ctrl-c)
  - [生成子进程](https://teemo.mintlify.app/guides/process/spawn)
  - [监听操作系统信号](https://teemo.mintlify.app/guides/process/os-signals)
  - [解析命令行参数](https://teemo.mintlify.app/guides/process/argv)
  - [从子进程中读取stderr](https://teemo.mintlify.app/guides/process/spawn-stderr)
  - [从子进程中读取stdout](https://teemo.mintlify.app/guides/process/spawn-stdout)
  - [获取纳秒级的进程运行时间](https://teemo.mintlify.app/guides/process/nanoseconds)
  - [生成子进程并通过IPC通信](https://teemo.mintlify.app/guides/process/ipc)

- 读取文件
  - [读取JSON文件](https://teemo.mintlify.app/guides/read-file/json)
  - [检查文件是否存在](https://teemo.mintlify.app/guides/read-file/exists)
  - [将文件作为字符串读取](https://teemo.mintlify.app/guides/read-file/string)
  - [将文件读取为Buffer](https://teemo.mintlify.app/guides/read-file/buffer)
  - [获取文件的MIME类型](https://teemo.mintlify.app/guides/read-file/mime)
  - [监视目录变化](https://teemo.mintlify.app/guides/read-file/watch)
  - [将文件作为ReadableStream读取](https://teemo.mintlify.app/guides/read-file/stream)
  - [将文件读取为Uint8Array](https://teemo.mintlify.app/guides/read-file/uint8array)
  - [将文件读取为ArrayBuffer](https://teemo.mintlify.app/guides/read-file/arraybuffer)

- 运行时
  - [删除文件](https://teemo.mintlify.app/guides/runtime/delete-file)
  - [运行Shell命令](https://teemo.mintlify.app/guides/runtime/shell)
  - [导入JSON文件](https://teemo.mintlify.app/guides/runtime/import-json)
  - [导入TOML文件](https://teemo.mintlify.app/guides/runtime/import-toml)
  - [在Bun中设置时区](https://teemo.mintlify.app/guides/runtime/timezone)
  - [设置环境变量](https://teemo.mintlify.app/guides/runtime/set-env)
  - [重新映射导入路径](https://teemo.mintlify.app/guides/runtime/tsconfig-paths)
  - [删除目录](https://teemo.mintlify.app/guides/runtime/delete-directory)
  - [读取环境变量](https://teemo.mintlify.app/guides/runtime/read-env)
  - [将HTML文件作为文本导入](https://teemo.mintlify.app/guides/runtime/import-html)
  - [在GitHub Actions中安装和运行Bun](https://teemo.mintlify.app/guides/runtime/cicd)
  - [使用Web调试器调试Bun](https://teemo.mintlify.app/guides/runtime/web-debugger)
  - [安装Bun的TypeScript声明](https://teemo.mintlify.app/guides/runtime/typescript)
  - [使用VS Code扩展调试Bun](https://teemo.mintlify.app/guides/runtime/vscode-debugger)
  - [使用V8堆快照检查内存使用情况](https://teemo.mintlify.app/guides/runtime/heap-snapshot)
  - [定义和替换静态全局变量和常量](https://teemo.mintlify.app/guides/runtime/define-constant)
  - [在macOS上对单文件JavaScript可执行程序进行代码签名](https://teemo.mintlify.app/guides/runtime/codesign-macos-executable)

- 流
  - [将ReadableStream转换为JSON](https://teemo.mintlify.app/guides/streams/to-json)
  - [将ReadableStream转换为Blob](https://teemo.mintlify.app/guides/streams/to-blob)
  - [将ReadableStream转换为Buffer](https://teemo.mintlify.app/guides/streams/to-buffer)
  - [将ReadableStream转换为字符串](https://teemo.mintlify.app/guides/streams/to-string)
  - [将ReadableStream转换为Uint8Array](https://teemo.mintlify.app/guides/streams/to-typedarray)
  - [将ReadableStream转换为块数组](https://teemo.mintlify.app/guides/streams/to-array)
  - [将Node.js Readable转换为JSON](https://teemo.mintlify.app/guides/streams/node-readable-to-json)
  - [将ReadableStream转换为ArrayBuffer](https://teemo.mintlify.app/guides/streams/to-arraybuffer)
  - [将Node.js Readable转换为Blob](https://teemo.mintlify.app/guides/streams/node-readable-to-blob)
  - [将Node.js Readable转换为字符串](https://teemo.mintlify.app/guides/streams/node-readable-to-string)
  - [将Node.js Readable转换为Uint8Array](https://teemo.mintlify.app/guides/streams/node-readable-to-uint8array)
  - [将Node.js Readable转换为ArrayBuffer](https://teemo.mintlify.app/guides/streams/node-readable-to-arraybuffer)

- 测试
  - [在`bun test`中监视方法](https://teemo.mintlify.app/guides/test/spy-on)
  - [在Bun测试运行器中提前退出](https://teemo.mintlify.app/guides/test/bail)
  - [在`bun test`中模拟函数](https://teemo.mintlify.app/guides/test/mock-functions)
  - [在Bun中使用监听模式运行测试](https://teemo.mintlify.app/guides/test/watch-mode)
  - [在`bun test`中使用快照测试](https://teemo.mintlify.app/guides/test/snapshot)
  - [使用Bun测试运行器跳过测试](https://teemo.mintlify.app/guides/test/skip-tests)
  - [在Bun中使用Testing Library](https://teemo.mintlify.app/guides/test/testing-library)
  - [在`bun test`中更新快照](https://teemo.mintlify.app/guides/test/update-snapshots)
  - [使用Bun测试运行器运行测试](https://teemo.mintlify.app/guides/test/run-tests)
  - [在Bun的测试运行器中设置系统时间](https://teemo.mintlify.app/guides/test/mock-clock)
  - [使用Bun测试运行器设置每个测试的超时时间](https://teemo.mintlify.app/guides/test/timeout)
  - [从Jest迁移到Bun的测试运行器](https://teemo.mintlify.app/guides/test/migrate-from-jest)
  - [使用Bun和happy-dom编写浏览器DOM测试](https://teemo.mintlify.app/guides/test/happy-dom)
  - [使用Bun测试运行器将测试标记为"待办"](https://teemo.mintlify.app/guides/test/todo-tests)
  - [使用Bun测试运行器多次重复运行测试](https://teemo.mintlify.app/guides/test/rerun-each)
  - [使用Bun测试运行器生成代码覆盖率报告](https://teemo.mintlify.app/guides/test/coverage)
  - [使用bun test导入、require和测试Svelte组件](https://teemo.mintlify.app/guides/test/svelte-test)
  - [使用Bun测试运行器设置代码覆盖率阈值](https://teemo.mintlify.app/guides/test/coverage-threshold)

- 工具
  - [生成UUID](https://teemo.mintlify.app/guides/util/javascript-uuid)
  - [哈希密码](https://teemo.mintlify.app/guides/util/hash-a-password)
  - [转义HTML字符串](https://teemo.mintlify.app/guides/util/escape-html)
  - [获取当前Bun版本](https://teemo.mintlify.app/guides/util/version)
  - [编码和解码base64字符串](https://teemo.mintlify.app/guides/util/base64)
  - [使用gzip压缩和解压数据](https://teemo.mintlify.app/guides/util/gzip)
  - [休眠固定毫秒数](https://teemo.mintlify.app/guides/util/sleep)
  - [检测代码是否在Bun中执行](https://teemo.mintlify.app/guides/util/detect-bun)
  - [检查两个对象是否深度相等](https://teemo.mintlify.app/guides/util/deep-equals)
  - [使用DEFLATE压缩和解压数据](https://teemo.mintlify.app/guides/util/deflate)
  - [获取当前入口点的绝对路径](https://teemo.mintlify.app/guides/util/main)
  - [获取当前文件的目录](https://teemo.mintlify.app/guides/util/import-meta-dir)
  - [检查当前文件是否为入口点](https://teemo.mintlify.app/guides/util/entrypoint)
  - [获取当前文件的文件名](https://teemo.mintlify.app/guides/util/import-meta-file)
  - [将文件URL转换为绝对路径](https://teemo.mintlify.app/guides/util/file-url-to-path)
  - [将绝对路径转换为文件URL](https://teemo.mintlify.app/guides/util/path-to-file-url)
  - [获取当前文件的绝对路径](https://teemo.mintlify.app/guides/util/import-meta-path)
  - [获取可执行bin文件的路径](https://teemo.mintlify.app/guides/util/which-path-to-executable-bin)

- WebSocket
  - [构建发布-订阅WebSocket服务器](https://teemo.mintlify.app/guides/websocket/pubsub)
  - [构建简单的WebSocket服务器](https://teemo.mintlify.app/guides/websocket/simple)
  - [启用WebSocket消息压缩](https://teemo.mintlify.app/guides/websocket/compression)
  - [在WebSocket上设置每套接字上下文数据](https://teemo.mintlify.app/guides/websocket/context)

- 写入文件
  - [删除文件](https://teemo.mintlify.app/guides/write-file/unlink)
  - [写入到stdout](https://teemo.mintlify.app/guides/write-file/stdout)
  - [将文件写入到stdout](https://teemo.mintlify.app/guides/write-file/cat)
  - [将Blob写入文件](https://teemo.mintlify.app/guides/write-file/blob)
  - [将字符串写入文件](https://teemo.mintlify.app/guides/write-file/basic)
  - [向文件追加内容](https://teemo.mintlify.app/guides/write-file/append)
  - [增量写入文件](https://teemo.mintlify.app/guides/write-file/filesink)
  - [将Response写入文件](https://teemo.mintlify.app/guides/write-file/response)
  - [复制文件到另一个位置](https://teemo.mintlify.app/guides/write-file/file-cp)
  - [将ReadableStream写入文件](https://teemo.mintlify.app/guides/write-file/stream)

## 贡献

请参阅[项目 > 贡献](https://teemo.mintlify.app/project/contributing)指南开始为Bun做贡献。

## 许可证

请参阅[项目 > 许可证](https://teemo.mintlify.app/project/license)页面了解有关Bun许可证的信息。