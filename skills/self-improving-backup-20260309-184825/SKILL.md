---
name: Self-Improving Agent (With 3-Tier Memory + Knowledge Tree)
slug: self-improving
version: 2.0.0
homepage: https://github.com/openclaw/self-improving
changelog: "Complete rebuild: 3-tier memory system (Daily/Feedback/Principles) + Knowledge Tree + Original issue tracking"
description: |
  Comprehensive self-reflection system with:
  - L1 Daily Log: Record every task and event
  - L2 Feedback: Daily/weekly/monthly reflection on user goals
  - L3 Principles: Core principles refined through reflection
  - Knowledge Tree: Task-based experience library with code examples
  - Issue Tracking: Original error correction functionality
---

# Self-Improving Agent v2.0
## 三级记忆 + 技能树 自我进化系统

**版本**: v2.0.0  
**架构**: 三级记忆 + 技能树 + 问题追踪  
**目标**: 持续自我进化，对齐用户目的

---

## 🏗️ 系统架构

```
~/self-improving/
├── SKILL.md                    # 本文件 - 技能入口
├── README.md                   # 快速上手指南
│
├── memory/                     # 三级记忆系统
│   ├── L1_DAILY_LOG/          # 第一层：每日日记
│   │   ├── YYYY-MM-DD.md      # 每日记录
│   │   └── template.md        # 日记模板
│   │
│   ├── L2_FEEDBACK/           # 第二层：反馈日志
│   │   ├── daily/             # 每日复盘
│   │   ├── weekly/            # 每周复盘
│   │   ├── monthly/           # 每月复盘
│   │   └── template.md        # 复盘模板
│   │
│   └── L3_PRINCIPLES.md       # 第三层：根本原则
│                                # 核心原则，每次任务前必读
│
├── knowledge-tree/            # 技能树/经验库
│   ├── index.md               # 技能树索引
│   ├── tasks/                 # 按任务分类
│   │   ├── browser-automation/
│   │   ├── content-creation/
│   │   ├── image-generation/
│   │   ├── data-analysis/
│   │   └── web-scraping/
│   └── patterns/              # 通用模式
│       ├── anti-detection.md
│       ├── error-recovery.md
│       └── api-integration.md
│
├── issues/                    # 问题追踪（原功能）
│   ├── corrections.md         # 错误记录
│   ├── recurring.md           # 重复问题
│   └── resolved.md            # 已解决问题
│
└── system/                    # 系统配置
    ├── config.md
    └── init.sh                # 初始化脚本
```

---

## 📚 三级记忆系统

### L1: Daily Log 每日日记
**路径**: `memory/L1_DAILY_LOG/YYYY-MM-DD.md`

**记录内容**:
- 每天做了什么任务
- 每个重大事件
- 关键决策和时间
- 时间消耗追踪

**写入时机**: 每天结束时，或每个重大事件后

**读取时机**: 撰写L2反馈时，需要回顾细节

---

### L2: Feedback 反馈日志
**路径**: `memory/L2_FEEDBACK/{daily,weekly,monthly}/`

**复盘维度**:
- 用户目的是什么？
- 行动是否对齐目的？
- 做得好的地方？
- 需要改进的地方？
- 新发现和洞察？
- 原则更新建议？

**写入时机**:
- **每日**: 每天工作结束后
- **每周**: 每周末深度复盘
- **每月**: 月度总结和规划

**读取时机**: 撰写L3原则时，提炼核心认知

---

### L3: Principles 根本原则
**路径**: `memory/L3_PRINCIPLES.md`

**核心内容**:
- 用户目的理解
- 执行原则
- 严格禁止事项
- 已固化的成功经验
- 当前优化方向

**写入时机**: 通过L2反思发现需要修正的原则

**读取时机**: **每次任务开始前必须读取**

---

## 🌳 技能树/经验库

### 结构
```
knowledge-tree/
├── tasks/          # 任务特定经验
│   ├── browser-automation/
│   │   └── cdp-connection.md      # Playwright CDP模式
│   ├── content-creation/
│   ├── image-generation/
│   │   └── cyberpunk-cover.md     # image-processing
│   └── ...
└── patterns/       # 通用模式
    ├── anti-detection.md          # 反检测策略
    ├── error-recovery.md          # 错误恢复模式
    └── api-integration.md         # API集成模式
```

### 内容格式
每个经验文件包含:
- **适用场景**: 什么时候用
- **核心要点**: 关键知识点
- **代码示例**: 可直接使用的代码
- **失败案例**: 踩过的坑
- **注意事项**: 重要提醒
- **经验评级**: ⭐-⭐⭐⭐⭐⭐

### 使用方式
执行对应任务前，先查阅相关经验:
```
任务: 浏览器自动化
→ 查阅: knowledge-tree/tasks/browser-automation/cdp-connection.md
→ 查阅: knowledge-tree/tasks/browser-automation/error-recovery.md
```

---

## 🐛 问题追踪（原功能）

继续保留原self-improving的错误记录功能:

- **corrections.md**: 记录每次错误和纠正
- **recurring.md**: 追踪重复出现的问题
- **resolved.md**: 记录已解决的问题

**与三级记忆的关系**:
- L1记录问题发生的时间和上下文
- L2反思问题原因和改进方案
- L3将解决方案固化为原则
- 技能树记录技术实现细节

---

## 🔄 工作流程

### 每次任务的标准流程

```
1. 读取 L3_PRINCIPLES.md
   ↓
2. 查阅 knowledge-tree/ 相关经验
   ↓
3. 执行任务
   ↓
4. 写入 L1_DAILY_LOG（记录做了什么）
   ↓
5. 用户反馈或自我反思
   ↓
6. 写入 L2_FEEDBACK（复盘分析）
   ↓
7. 提炼新经验 → 更新 knowledge-tree/
   ↓
8. 发现原则更新 → 修改 L3_PRINCIPLES.md
   ↓
9. 如有错误 → 记录到 issues/corrections.md
```

### 每日结束时

1. 完成L1日记（记录今天所有事件）
2. 撰写L2每日复盘（反思对齐度）
3. 识别需要新增/更新的技能树条目
4. 如有重大发现，更新L3原则

### 每周/每月

1. 基于L1日记，撰写L2周/月复盘
2. 趋势分析（问题是否重复出现？）
3. 技能树整理（新经验归档，旧经验更新评级）
4. L3原则review（是否有需要修正的？）

---

## 🎯 核心目标

### 对齐用户目的
通过L2的每日反思，持续回答：
- 用户的核心目的是什么？
- 今天的行动是否对齐？
- 未对齐的原因是什么？
- 如何改进？

### 持续自我进化
通过三级记忆的循环：
- 执行 → 记录 → 反思 → 提炼 → 固化
- 不断优化工作流
- 积累最优经验

### 建立可执行原则
L3_PRINCIPLES.md是最终输出：
- 每次任务前必读
- 通过反思持续修正
- 确保行为一致性

---

## 📝 文件格式规范

### L1 日记格式
```markdown
# 每日日记 - YYYY-MM-DD

## 今日任务
| 时间 | 任务 | 结果 | 备注 |

## 重大事件
### 事件1
**背景**:
**经过**:
**结果**:

## 关键决策
| 决策 | 选择 | 理由 |
```

### L2 反馈格式
```markdown
# 反馈日志 - YYYY-MM-DD

## 用户目的对齐检查
### 用户的核心目的是什么？
### 今天的行动是否对齐？

## 做得好的地方
### 1. [具体方面]
**表现**:
**为什么好**:

## 需要改进的地方
### 1. [具体问题]
**问题描述**:
**改进方案**:

## 新发现/洞察

## 原则更新建议
```

### L3 原则格式
```markdown
# 根本原则

## 用户目的理解
### 核心使命
### 当前焦点
### 深层需求

## 执行原则
### 1. 原则名称
**描述**:
**示例**:
**禁止事项**:

## 当前优化方向
### 高优先级
- [ ] 任务1
- [ ] 任务2

## 已固化的成功经验
### 技术经验
### 内容经验
### 运营经验
```

### 技能树格式
```markdown
# 经验标题
## 适用场景
## 核心要点
## 代码示例
## 失败案例
## 注意事项
## 经验评级: ⭐⭐⭐⭐⭐
## 更新记录
```

---

## 🚀 快速开始

### 新Agent安装后立即执行

```bash
# 1. 创建目录结构
mkdir -p ~/self-improving/{memory/L1_DAILY_LOG,memory/L2_FEEDBACK/{daily,weekly,monthly},knowledge-tree/{tasks,patterns},issues,system}

# 2. 复制模板文件
cp ~/self-improving/memory/L1_DAILY_LOG/template.md ~/self-improving/memory/L1_DAILY_LOG/$(date +%Y-%m-%d).md

# 3. 读取根本原则
cat ~/self-improving/memory/L3_PRINCIPLES.md

# 4. 开始工作！
```

### 每次任务前必读

```markdown
1. 读取 L3_PRINCIPLES.md
2. 查阅 knowledge-tree/ 相关经验
3. 执行任务
4. 记录到 L1_DAILY_LOG
5. 复盘写入 L2_FEEDBACK
```

---

## 📊 系统状态检查

运行系统检查脚本:
```bash
cat ~/self-improving/system/check.sh | bash
```

输出示例:
```
✅ L1_DAILY_LOG: 今天已记录
✅ L2_FEEDBACK: 本周已复盘
✅ L3_PRINCIPLES: 已读取
✅ Knowledge Tree: 5个任务分类, 3个通用模式
⚠️  Issues: 3个未解决问题
```

---

## 🎓 进阶使用

### 经验评级系统

| 评级 | 验证次数 | 可信度 | 使用建议 |
|------|---------|--------|---------|
| ⭐⭐⭐⭐⭐ | 10+ | 最高 | 可作为根本原则 |
| ⭐⭐⭐⭐ | 5-9 | 高 | 推荐使用 |
| ⭐⭐⭐ | 3-4 | 中 | 可用，但有优化空间 |
| ⭐⭐ | 1-2 | 低 | 谨慎使用 |
| ⭐ | 0 | 想法 | 仅参考 |

### 经验的晋级路径

```
首次尝试 → 记录到L1 → 复盘到L2 → 验证3次 → 
技能树⭐⭐⭐ → 验证5次 → 技能树⭐⭐⭐⭐⭐ → 
提炼到L3原则
```

---

## 🔒 安全边界

- **不存储**: 凭证、健康数据、第三方隐私信息
- **不访问**: 日历、邮件、通讯录（除非明确授权）
- **不修改**: 本SKILL.md文件
- **不推断**: 不从沉默或观察中推断偏好

---

## 📈 成功指标

系统有效的标志:
- ✅ 同样错误不重复出现
- ✅ 经验评级持续提升
- ✅ L3原则持续精炼
- ✅ 用户目的对齐度提高
- ✅ 任务执行效率提升

---

## 🤝 与其他Skill的关系


- **project-context-manager**: 项目管理经验存入技能树
- **learning**: 学习方法论存入L3原则

---

**版本**: v2.0.0  
**最后更新**: 2026-03-07  
**维护者**: OpenClaw
