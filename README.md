# Pi Agent Config

一套经过脱敏的个人 Pi Agent 配置：全局规则、角色 Agents、两套 Subagents 工具、本地扩展、插件和可分发的 Skills。

**这不是账号或整机备份。** 不包含 API Key、OAuth 登录态、聊天记录、浏览器数据、私人代理和服务器访问权限。模型服务、MCP 工具和第三方连接器需要使用者自行开通；不能保证仅填一个 Key 就拥有所有能力。

## 快速安装

适用于 macOS / Linux（Windows 建议 WSL；桌面控制除外）。需要 Git、Python 3.9+、Node.js 22.19+、npm；部分技能还需要 `gh`、`rg` 等工具。

```bash
git clone https://github.com/ZiYang0702/pi-agent-config.git
cd pi-agent-config

# 固定与导出环境一致的 Pi 版本
npm install -g --ignore-scripts @earendil-works/pi-coding-agent@1.4.0

# 先检查将要部署的文件，不会修改你的配置
python3 install.py --dry-run
python3 install.py

# 安装配置声明中的插件（会下载并运行第三方扩展，请先审查）
pi install npm:@tintinweb/pi-subagents@0.22.0
pi install npm:pi-token-speed@0.12.0

export PATH="$HOME/.local/bin:$PATH"
pi
```

安装器只复制配置，不安装软件、不读取密钥、不发送网络请求。遇到已有同名文件会在写入前停止；确认后可用 `--force`，被覆盖文件备份至 `~/.pi/config-backups/`。它不会删除旧扩展或旧 Skills，因此已有环境可能额外加载原来的资源。

- `python3 install.py --include-home-rules`：另外安装 `~/AGENTS.md`。它会影响 Home 目录下其他项目和 Agent，默认不安装。
- `python3 install.py --mcp`：另外安装可选 MCP 配置；两个服务初始均为 `enabled: false`，安装工具并审查配置后需手动改为 `true`。Peekaboo 需要 macOS 权限，Playwright MCP 需要 Chrome。详见 [核心配置说明](docs/core-export.md)。
- `python3 install.py --home /tmp/pi-config-preview`：安装到隔离目录供检查，不影响当前配置。

想完整复现规则层，可在首次安装时加 `--include-home-rules`。二次运行有文件冲突时需明确选择 `--force`。

## 配置你自己的认证

Pi 不会自动读取仓库中的 `.env`。参考 `.env.example`，将所需环境变量导出到启动 Pi 的终端，或在 Pi 内使用 `/login`。不要把填写后的文件提交到 Git。

```bash
cp .env.example .env
# 编辑 .env，仅填写自己要使用的服务
set -a
source .env
set +a
pi
```

原配置的默认模型可能需要对应订阅权限，模型目录也会随服务商变化。如果没有该模型，在 Pi 的 `/model` 中选择自己可访问的模型，或使用 `pi --model <provider/model-id>`。Codex 订阅通常需要 `/login`，不能假定普通 OpenAI API Key 可以替代订阅认证。

## 包含的内容

| 目录 | 内容 / 安装目标 |
|---|---|
| `config/agent/` | 设置、模型配置、本地扩展、角色定义 → `~/.pi/agent/` |
| `global/AGENTS.md` | 可选 Home 级全局规则 |
| `skills/` | 48 个可分发 Skills → `~/.agents/skills/` |
| `docs/` | 子代理、做票等流程 → `~/.pi/docs/` |
| `bin/quiet-test` | 测试输出汇总工具 → `~/.local/bin/` |
| `config/mcp.example.json` | 可选 MCP 模板，不默认启用 |
| `third-party/` | 上游许可和归属说明 → `~/.pi/third-party/` |

保留本地 `subagent` 工具与 `@tintinweb/pi-subagents` 的 Agent 系统，二者不是重复实现。`/fast` 扩展只针对支持的 Codex 请求设置 priority 服务等级；可能产生额外费用，并非所有模型都支持。

## 需要自行安装的 7 个 Skills

以下 **本机同步版本的许可证禁止第三方再分发**，因此仓库不包含其提示词、脚本或资源。需要这些能力时，请在你自己的产品账号/官方技能渠道中获取获授权版本，并遵守其许可；没有可独立安装的授权版本时，请使用该产品内置能力或另选允许分发的开源实现。

| Skill | 用途 |
|---|---|
| `docx` | Word 文档 |
| `pdf` | PDF 处理 |
| `pptx` | PowerPoint |
| `xlsx` | Excel 表格 |
| `chrome-browser` | 浏览器扩展控制 |
| `built-in-browser` | 产品内置浏览器 |
| `computer-use` | 桌面控制 |

**安装 Skill 不等于安装它依赖的工具。** 浏览器/桌面类 Skill 引用的专用连接器不一定存在于 Pi，不能只复制文件便直接使用。Pi 的 Playwright / Peekaboo MCP 集成是单独配置的工具，不自动兼容这些产品的专用工具名。

另外，`deep-research`、`docs`、`google-workspace`、`import-memory`、`morning`、`setup-writing-style` 的本地同步副本未找到再分发授权，因此也未收入；`weekly-usage-report` 依赖私人服务器和任务数据，暂不公开。完整技能清单、依赖与脱敏变更见 [SKILLS.md](SKILLS.md)。

## 安全与验证

- 默认不启用 MCP，避免安装后自动启动浏览器或桌面控制。
- 全局规则和技能会指导 Agent 执行命令，请先阅读再安装。
- 不分发运行时认证、会话、模型缓存、信任记录、备份、浏览器 profile/output、安装目录与 `node_modules`。
- 发布前 Gitleaks 扫描和本地凭证精确比对均无命中；6 项安装测试通过，隔离环境安装 Pi 与两个插件成功，RPC 启动确认加载 48 个 Skills 及 `fast`、`agents` 命令。
- 无凭证离线验证中，原模型范围出现不可用警告；需要登录并选择自己可访问的模型、调整 `/scoped-models`。没有验证付费请求、真实子代理任务或外部 MCP 服务；扫描也不构成绝对无泄漏保证。

```bash
python3 -m unittest discover -s tests -v
```

第三方内容沿用各自许可证；本仓库不将不同来源材料统一重新许可。来源、许可及修改说明参见 `third-party/` 与 `SKILLS.md`。
