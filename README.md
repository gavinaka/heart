# Heart · AkaGavin 私人心理 Agent

一个只对 AkaGavin 一人服务的心理支持 Agent：提供共情、结构化反思、循证心理方法与风险识别；不冒充执业心理治疗师或精神科医生。

定位：本项目只管**心态 / 情绪 / 心理**维度；事业、资产、交易、育儿等业务事实路由回 `Akagavin` 或对应源库。

---

## 怎么用（启动方式）

任何 AI 会话开场，把下面这段作为启动指令（或让 Agent 先读 `AGENTS.md` / `AGENT.md`）：

```
你现在是 Heart 心理 Agent。请按以下顺序加载后再开始：
1. C:\Users\31702\Desktop\Heart\AGENTS.md
2. C:\Users\31702\Desktop\Heart\governance\runtime_contract.md  （常驻精简契约 + 安全分流）
3. 仅在有分量的心理会话中，按需读取相关议题与最近 1 条相关会话；轻量问题不加载历史
4. 出现危机信号才加载完整危机协议；方法论与阶段地图也按需读取
5. 个人画像（引用 Akagavin，不复制；真相源 profile.json）：
   C:\Users\31702\Desktop\Akagavin\profile\profile.json
   C:\Users\31702\Desktop\Akagavin\domains\{assets,career,family,life}.md
   C:\Users\31702\Desktop\Akagavin\akagavin_profile_memory.md
6. 若涉及交易 / 资产 / 纪律 / 持仓 / T01：
   先读 C:\Users\31702\Desktop\Heart\data\Notion动态真值核对.md
   再只读核对 Notion 当前行；若任一账户持仓中，默认进入仓位管理模式。
然后用一句精确共情接住我，再开始。只有出现真实新进展或明确跟进约定时才更新议题追踪与会话记录。
```

---

## 目录结构

```
Heart/
├─ AGENTS.md                 自动加载入口：引用 AGENT.md + 安全协议 + 议题追踪
├─ AGENT.md                  根宪法：身份 / 安全协议 / 沟通协议 / 协同 / 个体化框架 / 回答结构
├─ README.md                 本文件：用法与协同说明
├─ domains/
│  ├─ 危机干预协议.md         最高优先级：风险信号、危机动作、求助资源、转介阈值
│  ├─ 方法论.md               流派工具箱：CBT/ACT/MI/DBT/正念/精神动力 + 选择速查
│  └─ 阶段心态地图.md         AkaGavin 当前人生阶段的心理张力解读与工作要点
└─ data/
   ├─ 议题追踪.md            活状态：有连续性需要时按需读取，有真实进展时更新
   └─ sessions/
      └─ 会话记录模板.md       每次会话记录的模板 + 索引
```

> **连续性闭环**：`议题追踪.md` 是工作流的记忆中枢，但不是每次会话的固定税。需要连续性时读取相关项，有真实进展时更新；会话记录只保存有价值的心理工作，避免噪声。

---

## 与生态的协同（引用不复制 · 只读不改）

Heart 是桌面工作流生态的一员，对其余活跃工作流 **只读、绝不修改**（与 `Visual Workflow Collection` 同构的硬约束）：

| Agent | 角色 | Heart 用它做什么 |
|---|---|---|
| `Akagavin` | 私人助理 + **画像单一来源** | 读画像，把情绪放回真实坐标 |
| `Trading-System` | 交易系统化引擎 | 核对交易走平/回撤的现实真值（T01） |
| `Technical expert` | AI 技术专家工作流 | 挑战驱动/快速精通模式的现实出口（T02） |
| `Visual Workflow Collection` | 隐私最小化状态聚合 | 只看可见性、新鲜度和运行健康，不读取业务正文 |
| `交易机会触发（预警）` | TradingView/Taker 候选预警 | 只识别候选工作流是否健康；候选不是交易信号 |
| `Agent Health Monitor` | 七 Agent 治理监控 | 只读治理证据；健康分不代表心理或交易质量 |

- **只读边界（硬约束）**：Heart 从不创建/修改/删除上述任何工作流的文件，产物只落在自己目录。
- **领域分工**：业务事实（交易仓位、资产数字、育儿方案）→ 对应源库；这些事带来的**心态与情绪** → Heart。
- **状态检查省 token**：Codex 与 Claude 的 SessionStart hook 都运行 [`scripts/开场同步.py`](scripts/开场同步.py)，只检查七 Agent 状态元数据，不触发 Visual、不读取业务正文。
- **状态不等于业务真值**：`OK` 只代表状态全景在 24 小时内；交易、资产或事业事实仍需回所属 Agent 核实。
- **交易动态真值**：交易相关心理议题必须先按 [`data/Notion动态真值核对.md`](data/Notion动态真值核对.md) 只读核对 Notion。Notion 当前行 > Trading 最新早/午/晚系统日报 > 本地缓存；Visual 只能证明状态新鲜度，不能进入业务真值排序。有 `持仓中` 就进入仓位管理模式，不推动新开仓。

---

## 三条最重要的原则（来自 AGENT.md）

1. **安全先于一切**——出现自伤/失控信号立即切危机协议，停止分析与挑战。
2. **不病理化清醒的痛苦**——他的时间焦虑、结构性悲观、诊断式自省多是高认知者的合理张力，不是障碍；把它当病治是冒犯。
3. **不替代执业医生**——可识别风险、建议就医、解释精神医学知识，但不下临床诊断、不荐处方药。

---

> 版本 v1.3 · 2026-07-04（加入 Notion 动态真值优先级与交易持仓硬门禁）
