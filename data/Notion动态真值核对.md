# Notion 动态真值核对清单

> 用途：当 Heart 处理交易、资产、纪律、心力、自控等会随时间变化的心理议题时，用本清单把判断锚回 Notion 的真实动态表。
> 边界：**只读。只允许使用 Notion fetch / query 类工具；禁止 create / update / comment / schema update / view create 等任何写入动作。**

---

## 1. 触发条件

出现以下任一场景，先按本清单核对，再进入心理分析：

- 用户谈到交易心态、T01、持仓、开仓、止损、止盈、追单、报复交易、纪律、门禁。
- 用户问"现在状态怎么样""真实情况是什么""今天有没有变化"。
- 本地日报、可视化报告、旧 JSON 镜像给出交易建议或状态，但未确认 Notion 当前持仓。
- 用户情绪明显与资产/交易结果耦合。

---

## 2. 真相优先级

1. **Notion 动态表当前行**：持仓、门禁、心力、自控、惩罚、洁净样本、A 股持仓。
2. `Trading-System` 最新早/午/晚系统日报：解释层与计划层，不能覆盖 Notion 当前持仓事实；晚间独立审查已经退役。
3. `Visual Workflow Collection` 的隐私安全状态报告：只能说明新鲜度和运行健康，不能提供仓位、交易或心理业务事实。
4. 本地 JSON、缓存、旧报告：只作线索，不能当动态真相。

若 1 与 2/3/4 冲突：**明确标注冲突，以 Notion 为准**。若 Notion 读不到：标注"动态真值未知"，不要假装已掌握当前仓位。

---

## 3. 数据源索引（Notion）

| 模块 | 数据库 ID | data source |
|---|---|---|
| 系统50笔交易（洁净进度样本） | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| （主）交易 Check | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| （Maker）交易 Check | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| （时间）交易 Check | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| 开仓前状态门禁 | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| 惩罚机制 | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| 心力监控模块 | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| 心智自控日记表 | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |
| A 股国家资产组合 | `<NOTION_RESOURCE_ID_REDACTED>` | `collection://<NOTION_RESOURCE_ID_REDACTED>` |

---

## 4. 核对顺序

### 4.1 当前持仓硬门禁

先查三张交易 Check：

- （主）交易 Check
- （Maker）交易 Check
- （时间）交易 Check

优先筛选 `状态 = 持仓中`，再看最新 `未开仓` 计划。至少记录：

- `计划起始时间`
- `标的`
- `状态`
- `交易策略`
- `开仓方式`
- `交易类型`
- `持仓量`
- `杠杆倍数`
- `按照计划执行`
- `情绪化操作`
- `计划质量`
- `备注（开仓理由）`
- `描述（复盘）`
- `更新时间`
- `url`

**判定规则：**

- 任一账户存在 `持仓中`：进入**仓位管理模式**，禁止把本地日报或可视化报告里的新开仓计划当成独立授权。
- 已有同方向持仓时：先核对止损、止盈、失效条件、是否需要减仓/取消挂单，再谈心理层的等待与失控感。
- `未开仓` 只能代表计划/挂单线索，不能推断已经成交。
- 时间交易 Check 若行数为 0，只能写"无可用记录"，不能推断时间纪律良好或不良。

### 4.2 状态门禁与心理负荷

随后查：

- 开仓前状态门禁：最新日期、主观结论、平静度、节奏一致性、结果依赖、连续止损数、身体状态。
- 心力监控模块：最新日期、工作心力消耗、交易专注度、异常标记、备注。
- 心智自控日记表：最新日期、是否按计划、计划完成度、内耗评分、情绪状态、出手频率。
- 惩罚机制：最近 90 天是否有新增惩罚、错误类型、严重程度、是否复发。
- 洁净样本：最新交易次数、状态、进度。

### 4.3 资产情绪相关

用户谈 A 股、资产压力、长期配置焦虑时，再查 A 股国家资产组合：

- 当前 `进行中` 行优先。
- 汇总持仓金额、目标金额、资产类型、风险等级、是否浮盈。
- 若有重复标的，标注为"数据结构重复/需人工确认"，不要自行合并成唯一真相。

---

## 5. 历史快照

> 具体账户、持仓、金额、日期与表现数据不进入版本库。运行时必须重新只读查询权威来源；本文件只保留核对流程。

## 6. 输出要求

交易相关心理回应必须显式写明：

- Notion 动态真值是否已读。
- 当前是否存在 `持仓中`。
- 若存在持仓：本次只讨论仓位管理心态/纪律，不给新开仓推动。
- 若 Notion 读不到：信心降级，并说明无法确认当前仓位。
