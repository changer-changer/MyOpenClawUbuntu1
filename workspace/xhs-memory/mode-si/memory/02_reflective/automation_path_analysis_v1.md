# 自动化路径双轨引擎分析与沉淀 (Automation Path Analysis)

更新时间：2026-03-05

为了实现小红书 IP 的全自动防封锁运营，目前我们在工程上彻底打通了**两条并行路径**。本文件记录了两条路径的核心差异、执行瓶颈、以及未来 Agent 接手时的选择依据。

---

## 路线 A：Agent 原生 CDP 注入流 (The "Autopilot" Fast Path)

**核心逻辑**：Agent 不写 Python 代码，直接通过 `browser_subagent` 连接本地已启动的 Chrome (localhost:9222)。抛弃传统的视觉识别找按钮，直接使用高度凝练的 JavaScript 操作 DOM。

- **执行主体**：AI 自身原生工具 (`browser_subagent` + `execute_browser_javascript`)
- **适用场景**：用户要求“立刻发帖”、“极速发帖”、“要求 Agent 全权托管的 5 小时睡眠模式”。
- **执行速度**：**极快 (秒级)**。跳过了视觉渲染、屏幕截图回传和 AI 视觉理解的极其漫长的等待。
- **核心技巧 (Tricks)**：
  1.  绕开文本框拦截：不要用 `.focus()` 和键盘模拟打字，小红书前端框架会拦截。必须用 `Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(element, value);` 强行改值，并派发 `input` 事件欺骗 React。
  2.  绕开富文本编辑器：找 `#post-textarea` 或 `[contenteditable="true"]`，直接改 `.innerHTML` 并派发 `blur` 事件。
  3.  跳过找按钮：`Array.from(document.querySelectorAll('button')).find(btn => btn.innerText.includes('发布')).click();`
- **此前为何慢？(瓶颈分析)**：之前极慢是因为 Agent 尝试用“人类视觉”去审视网页，截图 -> 传给视觉模型 -> 计算元素的 X, Y 坐标 -> 移动鼠标去点。在小红书这种存在大量懒加载、骨架屏的动态 SPA 网页中，这种方案会导致极高的出错重试率和延迟（单步几十秒）。

---

## 路线 B：Playwright 沉浸式拟人流 (The "Stealth Python" Path)

**核心逻辑**：Agent 编写并维护独立的 `.py` 脚本（如 `publish_post.py` 或 `autonomous_5h_loop.py` 中的 Python 逻辑），依赖 `playwright` 和随机的 `time.sleep`。

- **执行主体**：操作系统的 Python 解释器。
- **适用场景**：长期稳健运行、面对极高强度的风控期（如官方严查 API/JS 注入）、或者遇到复杂的系统级弹窗（如选择系统文件）。
- **执行速度**：**较慢 (约 50-60 秒)**。为了拟真，脚本中强行加入了大量 `time.sleep()`，模拟人类鼠标的滑动、犹豫和缓慢打字。
- **核心技巧 (Tricks)**：
  1.  必须要挂载原生 userDataDir，以此继承本地登录态，**绝对不能**每次新开无痕窗口扫码。
  2.  启动参数必须带 `--disable-blink-features=AutomationControlled`，隐藏 `navigator.webdriver` 标志。
  3.  上传文件时不能点弹窗，必须定位 `<input type="file">` 元素后调用 Playwright 本身的 `set_input_files()` API。
- **优势**：在防封（Anti-Ban）维度得分最高。因为所有的操作时序、打字速度度可以受控分布，最像真人。

---

## ⚡实测数据基准比对 (Benchmark 2026-03-05)

根据刚才在第五篇 (微信100条自动回) 和 第六篇 (熬夜做PPT) 的实机测试对比：

| 测试维度         | 路线 A (纯JS极速注入方案) | 路线 B (Playwright纯拟人方案) | 瓶颈卡点分析                                                             |
| :--------------- | :------------------------ | :---------------------------- | :----------------------------------------------------------------------- |
| **标题输入**     | 瞬间 (< 0.1秒)            | 4.59 秒                       | 路线B采用 `delay=150ms` 模拟人手敲击每个字符                             |
| **正文输入**     | 瞬间 (< 0.1秒)            | 23.58 秒                      | 路线B采用 `delay=50ms` 模拟连续大段文本输入                              |
| **图片上传**     | ❌ 浏览器安全拦截         | 4.12 秒 (利用API接管)         | JS 无法读写本地磁盘文件，必须降级使用 CDP/Playwright的 `set_input_files` |
| **核心交互耗时** | **不到 1 秒**             | **约 54 秒**                  | 拟人化虽然慢，但是它提供了 100% 的底层安全。                             |

---

## 最终结论与 Agent 决策树

未来的 Agent 在接手时，请严格遵守以下决策：

1. **默认状态下**：执行 **路线 A (原生 CDP 注入)**。由你亲自下发 JS 给浏览器，实现发帖和数据抓取。唯快不破，且不需要维护易碎的 Python 环境。
2. **当遇到安全拦截弹窗/账号异常告警时**：立即降级回 **路线 B (Playwright 拟人)**，增加操作间隔，进入龟速拟人模式。
