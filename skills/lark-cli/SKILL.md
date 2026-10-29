---
name: lark-cli
description: 飞书 / Lark 资源查询或修改、用户提供飞书资源链接、飞书 CLI 配置或排查时使用。通过 lark-cli 内置 skills 获取对应操作流程。
---

# 飞书 / Lark

1. 先运行 `lark-cli skills list`，获取当前可用的 skills。
2. 按 description 选择与任务对应的 skill，运行 `lark-cli skills read <name>` 并读取其指令。
3. 执行业务或配置命令前，按选中的 skill 查阅对应 reference 或命令的 `--help`，确认用法后执行。
