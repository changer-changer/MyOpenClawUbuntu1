# Model-Si 小红书自动化运营系统 v4.0
## 全自主闭环运营架构

**版本**: v4.0  
**架构**: 记忆隔离 + 全自动循环 + 自我进化  
**循环周期**: 30分钟  
**核心目标**: 建立有影响力的IP + 商业闭环

---

## 🏗️ 系统架构

### 三层记忆体系

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: 通用技术记忆 (MEMORY.md)                          │
│  - Playwright CDP模式                                       │
│  - 跨项目技术原则                                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Layer 2: 小红书核心战略 (xhs-memory/mode-si/memory/03_semantic/) │
│  - CORE_STRATEGY.md        # 战略定位                       │
│  - OPERATION_LOOP.md       # 运营闭环（本文件）             │
│  - SELF_IMPROVEMENT.md     # 自我进化记录                   │
│  - BOTTLENECKS.md          # 瓶颈识别与解决                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: 运行时数据                                        │
│  - 01_episodic/            # 草稿                           │
│  - 02_reflective/          # 发布记录                       │
│  - 03_semantic/            # 沉淀原则                       │
│  - performance_data/       # 数据追踪                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 30分钟全自动闭环

### 8步工作流循环

```
┌──────────────┐
│  1. Align    │ ◄──── 读取CORE_STRATEGY.md
│    对齐战略   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  2. Route    │ ◄──── 检查ROADMAP，确定当前阶段
│    路线检查   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  3. Topic    │ ◄──── 从TOPIC_LIBRARY选择
│    选题确认   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  4. Research │ ◄──── scripts/search/run.py 调研
│    即时调研   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  5. Recall   │ ◄──── 读取本文件核心原则
│    认知加载   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  6. Create   │ ◄──── 生成封面+文案
│    多模态创作 │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  7. Act      │ ◄──── scripts/publish/run.py 发布
│    拟人发布   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  8. Reflect  │ ◄──── 数据收集→反馈分析→优化
│    反思进化   │
└──────────────┘
       │
       └──────────────► 回到Step 1（30分钟后）
```

---

## 📊 Step 8: Reflect 详细流程

### 8.1 数据收集（自动）

```python
# 发布后自动执行
1. 截图当前笔记页面
2. 抓取点赞/收藏/评论数
3. 抓取评论内容
4. 记录到 performance_data/YYYYMMDD_HHMMSS.json
```

### 8.2 视觉自检（Sub-Agent）

**创建sub-agent任务**:
```
task: 审视刚刚发布的小红书笔记，找出视觉和内容问题
input: 
  - 笔记截图
  - 发布参数（标题、文案、封面路径）
  - CORE_STRATEGY.md 规范
output:
  - 问题列表（严重/一般/建议）
  - 改进建议
  - 是否符合赛博朋克视觉规范
```

**自检检查项**:
- [ ] 封面是否符合深色+霓虹青规范
- [ ] 字体是否为 JetBrains Mono
- [ ] 页码是否正确（单图不标）
- [ ] 文案是否有emoji轰炸
- [ ] CTA是否为特权型钩子
- [ ] 语言是否符合极客隐喻

### 8.3 反馈分析（Sub-Agent）

**创建sub-agent任务**:
```
task: 分析评论反馈，提取用户需求和内容优化方向
input:
  - 评论JSON数据
  - 高互动评论列表
  - 问题类评论列表
output:
  - 用户高频需求
  - 内容优化建议
  - 新选题灵感
```

### 8.4 数据沉淀

**更新文件**:
1. `memory/02_reflective/performance_YYYYMMDD.md` - 发布记录
2. `memory/03_semantic/FEEDBACK_OPTIMIZATION.md` - 优化记录
3. `planning/TOPIC_LIBRARY.md` - 根据反馈更新选题库

---

## 🚀 自我进化系统

### 持续瓶颈识别

每次循环结束后，自问：

```markdown
## 当前运行瓶颈检查清单

### 内容创作瓶颈
- [ ] 封面生成速度是否太慢？
- [ ] 文案创作是否符合新规范？
- [ ] 调研质量是否足够？

### 技术瓶颈
- [ ] 是否有更好的反检测方案？
- [ ] 发布流程是否稳定？
- [ ] 数据收集是否完整？

### 战略瓶颈
- [ ] 定位是否需要调整？
- [ ] 变现路径是否清晰？
- [ ] 内容差异化是否足够？

### 自动化瓶颈
- [ ] 30分钟周期是否合理？
- [ ] 是否需要人工介入点？
- [ ] 错误处理是否完善？
```

### 自我优化流程

```
1. 识别瓶颈
   └─► 记录在 BOTTLENECKS.md

2. 提出需求
   └─► "需要XX技能来解决YY问题"

3. 自我解决（尝试）
   ├─► 修改现有脚本
   ├─► 创建新工具
   ├─► 优化流程
   └─► 记录在 SELF_IMPROVEMENT.md

4. 验证效果
   └─► 下一轮循环检验

5. 知识沉淀
   └─► 更新CORE_STRATEGY.md
   └─► 更新本文件
```

---

## 🛠️ 所需技能清单

### 当前已具备
- ✅ 百度搜索（search/run.py）
- ✅ 封面生成（cover/run.py）
- ✅ 发布脚本（publish/run.py）
- ✅ 评论查看（comments/run.py）
- ✅ 反馈截图（feedback/run.py）

### 需要开发（自我进化）
- 🔄 赛博朋克封面生成器 v2.0
- 🔄 自动数据追踪系统
- 🔄 评论情感分析
- 🔄 竞品监控系统
- 🔄 热点趋势追踪

---

## 📈 商业闭环目标

### 短期目标（1-30天）
- 建立稳定的内容产出节奏
- 测试新模式的接受度
- 积累初始粉丝和数据

### 中期目标（31-90天）
- 建立"AI炼金术士"人设
- 筛选高意图用户群体
- 测试变现产品（课程/社群）

### 长期目标（90天+）
- 建立完整商业闭环
- 实现自动化变现
- 成为垂直领域KOL

---

## ⚡ 自动化执行脚本

### 主循环脚本（待创建）

```bash
#!/bin/bash
# scripts/autopilot/run.sh - 30分钟全自动循环

while true; do
    echo "[$(date)] 开始新一轮运营循环..."
    
    # Step 1-8
    python3 scripts/autopilot/execute_loop.py
    
    echo "[$(date)] 本轮完成，等待30分钟..."
    sleep 1800  # 30分钟
done
```

### 执行逻辑（待创建）

```python
# scripts/autopilot/execute_loop.py

def main_loop():
    # Step 1: 对齐战略
    strategy = load_strategy()
    
    # Step 2: 路线检查
    current_phase = check_roadmap()
    
    # Step 3: 选题确认
    topic = select_topic()
    
    # Step 4: 即时调研
    research_data = run_research(topic)
    
    # Step 5: 认知加载
    principles = load_principles()
    
    # Step 6: 多模态创作
    content = create_content(topic, research_data, principles)
    
    # Step 7: 拟人发布
    note_id = publish(content)
    
    # Step 8: 反思进化
    if note_id:
        collect_data(note_id)
        screenshot_self_check(note_id)
        analyze_feedback(note_id)
        identify_bottlenecks()
        self_improve()
    
    log_completion()
```

---

## 📝 记录要求

### 必须记录的内容

1. **每次发布**
   - 发布记录到 `memory/02_reflective/`
   - 数据到 `performance_data/`

2. **每次自检**
   - 问题列表到 `memory/02_reflective/self_check_*.md`
   - 截图到 `assets/self_check/`

3. **每次反馈分析**
   - 分析结果到 `memory/03_semantic/FEEDBACK_OPTIMIZATION.md`
   - 新选题到 `planning/TOPIC_LIBRARY.md`

4. **每次瓶颈识别**
   - 瓶颈记录到 `memory/03_semantic/BOTTLENECKS.md`
   - 解决方案到 `memory/03_semantic/SELF_IMPROVEMENT.md`

5. **每次优化**
   - 更新本文件
   - 更新CORE_STRATEGY.md
   - 更新SKILL.md

---

## ✅ 安装检查清单

当其他用户安装此skill时，应检查：

- [ ] Chrome CDP在9222端口运行
- [ ] 小红书已登录
- [ ] xhs-memory/目录结构完整
- [ ] 所有脚本可执行
- [ ] 30分钟循环已配置
- [ ] sub-agent环境就绪

---

**系统版本**: v4.0  
**创建时间**: 2026-03-07  
**架构设计**: 全自主闭环 + 自我进化  
**状态**: 🚀 待实施
