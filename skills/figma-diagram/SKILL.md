---
name: figma-diagram
description: 在 FigJam 画图辅助说明。用于：用户要画图、图示、流程图、架构图、时序图；或你要解释的流程、pipeline、模块关系有 4 个以上节点或带分支，文字讲不清。
---

# figma-diagram

用 `mcp__figma__generate_diagram`（先 ToolSearch `select:mcp__figma__generate_diagram` 加载）把 Mermaid 渲染成 FigJam 图。本文件已含 Figma 官方 `figma-generate-diagram` skill 里用得上的规则，不再去读那份 skill 和它的 references。

目标是**一眼看懂**：读者扫一眼就抓住结构，细看能读懂每一步在做什么。图的质量优先；在不损失清楚度的前提下再求简洁。

## 步骤

1. **定内容**。列出要表达的节点和关系，只留回答当前问题必需的。依据来自代码、文档或对话里的事实；缺的信息留空并在回复里说明，不编边和节点。完成标准：每个节点都有进或出的边（起点终点除外），总数 ≤ 20。超过就拆成几张图，或把细节收进一个节点。
2. **选类型**，取第一个匹配：
   - 参与方之间按时间来回调用 → `sequenceDiagram`
   - 明确的状态和转移 → `stateDiagram-v2`
   - 表、字段、基数 → `erDiagram`
   - 带日期的排期 → `gantt`
   - 其余（流程、pipeline、决策、依赖、架构）→ `flowchart LR`；层级深、同层兄弟多时用 `TD`
   - 饼图、思维导图、类图、时间线、韦恩图不支持，直接告诉用户，不调工具。
3. **写 Mermaid**，按下面「画面规则」和「语法限制」。
4. **调用**。参数：`name`（简短标题）、`mermaidSyntax`、`planKey`（从当前已授权的 Figma 团队选择；未配置时先询问用户）。本会话已经画过图，就传上一张的 `fileKey`（链接 `figma.com/board/{fileKey}/...` 里那段），画在同一张白板上，免得草稿区堆文件。
5. **回复**。给出返回的链接（markdown 链接），再用一两句点出图里最关键的一处。图已经表达的结构不在文字里重复。

工具报错时，按报错改 Mermaid 重试一次；同一张图改两次仍不满意，停下问用户具体哪里不对。

## 画面规则

- **标签**：节点名要让没看过代码的人也能懂，短了能说清就短，说不清就写全（一般 15 个汉字以内）。边标签写清这一步传了什么或在什么条件下走，动词开头，从源节点视角写；流向一看就懂的边可以不加。不加句号。
- **形状表意，标签就不重复**：`db[("PostgreSQL")]`，不写「数据库: PostgreSQL」。默认矩形；只在有含义时换形状：
  - `{"..."}` 判断，`[("...")]` 存储，`(["..."])` 起止，`[["..."]]` 子流程，`[/"..."/]` 输入
- **边**：`-->` 主流程，`-.->` 异步、可选、稍后发生，`==>` 关键路径（全图最多一条链）。多对一用 `&` 合写：`a & b --> c`。
- **颜色**用来分组和标状态，让读者靠颜色就分出几类节点：同一阶段、同一模块、同一种状态用同一种色。每种颜色的含义要能从图上看出来，不明显时加一个图例节点（见下）。用 `classDef` 定义、`class` 批量套用。只有 `fill` 和 `stroke` 生效，用 FigJam 浅色系：
  - 绿 `fill:#CDF4D3,stroke:#66D575`（成功、输出），红 `fill:#FFCDC2,stroke:#FF7556`（出错、阻塞），黄 `fill:#FFECBD,stroke:#FFC943`（待定、人工），蓝 `fill:#C2E5FF,stroke:#3DADFF`（重点、核心），紫 `fill:#DCCCFF,stroke:#874FFF`（外部、特殊），青 `fill:#C6FAF6,stroke:#5AD8CC`（辅助），灰 `fill:#D9D9D9,stroke:#B3B3B3`（次要、已废弃）
- **说明**：某个节点需要补一句为什么或注意什么，用气泡节点挂在旁边：`n1@{ shape: comment, label: "重试 3 次后才进死信" }`，再 `dlq -.- n1`。图例同理，用一个 subgraph 放几个上色的示例节点。说明只加在读者会卡住的地方。
- **subgraph** 只在 3 个以上节点共享明确边界（阶段、子系统）时用，最多嵌套 2 层，加浅色底让边界显出来，几个组各用一种浅色：`style 组id fill:#C2E5FF,stroke:#3DADFF`；只有一个组就用 `fill:#F5F5F5,stroke:#B3B3B3`。边连到组内具体节点，不连组 id。

## 语法限制

渲染器会拒绝或吞掉这些，写完逐条对一遍：

- 不用 emoji、HTML 标签、`\n`。
- 所有节点文字和边文字都加双引号：`a["读取配置"]`、`-->|"失败"|`。
- 节点 id 用 camelCase 英文，不用下划线，不用 `end` `subgraph` `graph`。
- `sequenceDiagram` 里不写 `Note`，会被删掉。
- `gantt` 里的颜色样式会被删掉。

## 例子

```
flowchart LR
    src[/"Kafka 原始日志"/] --> parse["按 schema 解析"] --> valid{"格式合法?"}
    valid -->|"合法"| enrich["补全用户和地域字段"] --> store[("ClickHouse 明细表")]
    valid -->|"不合法"| dlq["写入死信队列"]
    dlq -.->|"人工修复后重放"| parse
    n1@{ shape: comment, label: "解析失败自动重试 3 次后才进死信" }
    dlq -.- n1
    classDef ok fill:#CDF4D3,stroke:#66D575
    classDef bad fill:#FFCDC2,stroke:#FF7556
    class store ok
    class dlq bad
```
