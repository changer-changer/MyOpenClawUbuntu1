---
name: Self-Improving Agent v4.0
slug: self-improving
version: 4.0.0
homepage: https://github.com/openclaw/self-improving
changelog: |
  v4.0.0 - Integrated Edition:
  - Merged v2 + v3 features
  - Added heartbeat monitoring
  - Enhanced validation system
  - Added prediction engine
  - Removed platform-specific content
  - Generic framework for any domain
description: |
  Comprehensive self-reflection and continuous improvement system with:
  - 3-Tier Memory (Daily/Feedback/Principles)
  - Knowledge Tree with validation
  - Error prediction engine
  - Automated heartbeat monitoring
  - Metrics tracking and analytics
---

# Self-Improving Agent v4.0
## 集成版 - 三级记忆 + 验证系统 + 预测引擎

**版本**: v4.0.0  
**架构**: 三级记忆 + 技能树 + 验证系统 + 预测引擎 + 心跳监控  
**目标**: 持续自我进化，对齐用户目的，预防错误复发

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
├── v4-integrated/             # 增强功能 (原v3-enhanced)
│   ├── meta/                  # 运行时元数据
│   ├── metrics/               # 性能指标
│   ├── predictions/           # 错误预测
│   └── validation/            # 经验验证
│       ├── pending/           # 待验证
│       ├── verified/          # 已验证
│       └── failed/            # 验证失败
│
├── heartbeat/                 # 心跳监控
│   ├── status.json            # 当前状态
│   ├── schedule.json          # 调度配置
│   └── last-run.log           # 最后运行日志
│
├── issues/                    # 问题追踪
│   ├── corrections.md         # 错误记录
│   ├── recurring.md           # 重复问题
│   └── resolved.md            # 已解决问题
│
└── system/                    # 系统配置
    ├── check.sh               # 状态检查脚本
    ├── init.sh                # 初始化脚本
    ├── heartbeat.sh           # 心跳脚本 ⭐新增
    └── config.json            # 配置文件
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
- **验证状态**: pending/verified/failed

### 验证系统 (v4新增)
经验需要通过验证才能提升评级：
1. 创建经验 → `validation/pending/`
2. 多次使用后验证 → `validation/verified/` 或 `validation/failed/`
3. 已验证经验可提升到更高评级

---

## 🔮 错误预测引擎 (v4新增)

### 功能
- 分析历史错误模式
- 在执行前预警可能的问题
- 推荐预防方案

### 数据路径
- `v4-integrated/predictions/error_patterns.json`

### 使用方式
每次任务前自动检查：
```bash
cat ~/self-improving/system/heartbeat.sh | bash
```

---

## 💓 心跳监控系统 (v4新增)

### 功能
- 定期检查系统状态
- 自动记录每日日记
- 提醒复盘和验证
- 同步metrics数据

### 配置
编辑 `heartbeat/schedule.json`:
```json
{
  "enabled": true,
  "interval_minutes": 30,
  "checks": [
    "daily_log",
    "feedback_pending",
    "validation_queue",
    "metrics_sync"
  ],
  "notifications": true
}
```

### 运行心跳
```bash
# 手动运行
bash ~/self-improving/system/heartbeat.sh

# 或添加到crontab (每30分钟)
*/30 * * * * bash ~/self-improving/system/heartbeat.sh
```

---

## 🔄 工作流程

### 每次任务的标准流程

```
1. 运行心跳检查
   bash system/heartbeat.sh
   ↓
2. 读取 L3_PRINCIPLES.md
   ↓
3. 查阅 knowledge-tree/ 相关经验
   ↓
4. 检查 predictions/ 错误预警
   ↓
5. 执行任务
   ↓
6. 记录数据到 v4-integrated/metrics/
   ↓
7. 写入 L1_DAILY_LOG（记录做了什么）
   ↓
8. 用户反馈或自我反思
   ↓
9. 写入 L2_FEEDBACK（复盘分析）
   ↓
10. 提炼新经验 → 创建知识树文件 + validation/pending/
   ↓
11. 发现原则更新 → 修改 L3_PRINCIPLES.md
   ↓
12. 如有错误 → 记录到 issues/corrections.md + predictions/
```

### 每日结束时

1. 运行心跳检查
2. 完成L1日记（记录今天所有事件）
3. 撰写L2每日复盘（反思对齐度）
4. 检查 validation/pending/ 队列
5. 识别需要新增/更新的技能树条目
6. 如有重大发现，更新L3原则
7. 同步 metrics 数据

### 每周/每月

1. 运行心跳检查
2. 基于L1日记，撰写L2周/月复盘
3. 趋势分析（问题是否重复出现？）
4. 技能树整理（验证状态更新）
5. predictions/ 模式更新
6. L3原则review（是否有需要修正的？）

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

### 预防错误复发
通过预测引擎：
- 识别错误模式
- 提前预警
- 主动预防

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
### 工作流经验
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
## 验证状态: verified
## 更新记录
```

---

## 🚀 快速开始

### 新Agent安装后立即执行

```bash
# 1. 运行初始化
bash ~/self-improving/system/init.sh

# 2. 运行状态检查
bash ~/self-improving/system/check.sh

# 3. 读取根本原则
cat ~/self-improving/memory/L3_PRINCIPLES.md

# 4. 配置心跳监控
cat ~/self-improving/heartbeat/schedule.json

# 5. 开始工作！
```

### 每次任务前必读

```markdown
1. 运行心跳检查
2. 读取 L3_PRINCIPLES.md
3. 查阅 knowledge-tree/ 相关经验
4. 检查 predictions/ 错误预警
5. 执行任务
6. 记录到 L1_DAILY_LOG
7. 复盘写入 L2_FEEDBACK
```

---

## 📊 系统状态检查

运行系统检查脚本:
```bash
bash ~/self-improving/system/check.sh
```

输出示例:
```
==========================================
Self-Improving Agent v4.0 - 系统检查
==========================================

1. 检查目录结构...
  ✅ L1_DAILY_LOG 目录
  ✅ L2_FEEDBACK/daily 目录
  ✅ knowledge-tree/tasks 目录
  ✅ v4-integrated/metrics 目录
  ✅ heartbeat/ 目录

2. 检查核心文件...
  ✅ L3_PRINCIPLES.md
  ✅ SKILL.md
  ✅ README.md
  ✅ heartbeat/schedule.json

3. 检查今日记录...
  ✅ 今天日记已记录 (25 行)
  ⚠️  今天复盘未完成

4. 技能树统计...
  📊 任务经验: 3 个
  📊 通用模式: 2 个
  ✅ 技能树有内容

5. 验证队列...
  📋 待验证: 2 个
  ✅ 已验证: 1 个

6. 心跳状态...
  ✅ 心跳已启用
  ⏱️  上次运行: 5分钟前
  ✅ 调度正常

==========================================
检查结果: 10 通过, 0 失败
==========================================
🎉 系统状态良好！
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

### 验证流程
```
创建经验 → pending → 使用3次 → verified → 
使用5次 → ⭐⭐⭐⭐ → 使用10次 → ⭐⭐⭐⭐⭐ → 
提炼到L3原则
```

### 预测引擎
系统自动学习你的错误模式：
- 记录错误 → issues/corrections.md
- 分析模式 → predictions/error_patterns.json
- 预警提示 → heartbeat 检查时显示

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
- ✅ 错误预测准确率 > 80%
- ✅ 心跳系统稳定运行

---

## 🤝 与其他Skill的关系

- **project-context-manager**: 项目管理经验存入技能树
- **learning**: 学习方法论存入L3原则
- **任何其他skill**: 各领域经验均可沉淀到本系统

---

## 🆕 v4.0 新增功能

### 心跳监控
- 自动化状态检查
- 定时提醒复盘
- 数据自动同步

### 验证系统
- 经验需要验证才能升级
- 防止错误经验固化
- 科学验证最佳实践

### 预测引擎
- 错误模式识别
- 提前预警
- 主动预防

### Metrics追踪
- 性能数据记录
- 趋势分析
- 优化建议

---

**版本**: v4.0.0 - Integrated Edition  
**最后更新**: 2026-03-09  
**维护者**: OpenClaw
