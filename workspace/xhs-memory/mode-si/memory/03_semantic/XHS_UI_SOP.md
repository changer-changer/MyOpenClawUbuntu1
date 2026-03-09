# 小红书创作者中心操作 SOP (标准执行路径)

为解决 Agent 每次探索页面耗时过长、频繁报错的问题，特定义此最优操作路径。任何自动化脚本（基于 CDP、Pyppeteer 或注入）**必须**遵循此文档中的 CSS Selectors 和 JavaScript 执行逻辑。

## 1. 免密登录与隐蔽性前提

- **严禁使用原生 Playwright 直接启动全新浏览器**。
- 必须使用 `chrome-remote-interface` 或连接到本地已经通过 `--remote-debugging-port=9222` 启动的常驻 Chrome 实例。
- 这样能继承本地所有的 Cookie 状态，完美避开小红书的反爬滑块验证。

## 2. 最优页面控制流 (Publish Flow)

### 2.1 页面初始化

- Target URL: `https://creator.xiaohongshu.com/publish/publish`
- 动作：加载完毕后，使用 JS 模拟平滑滚动，并随机 Wait 2~4 秒。

### 2.2 Title (标题) 注入

由于直接使用 `page.type()` 可能触发前端框架拦截报错，最佳实践是直接通过 JS 注入并抛出 React 识别的 Input Event：

```javascript
function setTitle(titleContent) {
  const titleInput =
    document.querySelector(".c-input_inner") ||
    document.querySelector('[placeholder*="标题"]');
  if (titleInput) {
    const nativeSetter = Object.getOwnPropertyDescriptor(
      window.HTMLInputElement.prototype,
      "value",
    ).set;
    nativeSetter.call(titleInput, titleContent);
    titleInput.dispatchEvent(new Event("input", { bubbles: true }));
  }
}
```

### 2.3 Content (正文) 注入

小红书的正文使用了富文本编辑器 (`contenteditable="true"` 或特定编辑器 DOM)。最好的方式：

```javascript
function setContent(postContent) {
  const editor =
    document.querySelector("#post-textarea") ||
    document.querySelector('[contenteditable="true"]');
  if (editor) {
    // 先聚焦
    editor.focus();
    // 覆盖内容
    editor.innerHTML = postContent.replace(/\n/g, "<br>"); // 保留换行符
    editor.dispatchEvent(new Event("input", { bubbles: true }));
    editor.dispatchEvent(new Event("blur", { bubbles: true }));
  }
}
```

### 2.4 上传图片 (Upload Image)

不要让 Agent 视觉寻找按钮然后试图操作系统的文件选择框。直接定位 `<input type="file">` 隐藏节点进行文件喂入（在 Puppeteer/Playwright 连接模式下）：

- Selector: `input[type="file"][accept*="image"]`
- Action (Python Pypeteer/Playwright):
  ```python
  file_input = await page.querySelector('input[type="file"]')
  await file_input.uploadFile('/path/to/cover.png')
  ```

### 2.5 发布按钮 (Publish)

触发发布：

```javascript
function clickPublish() {
  // 根据文字定位发布按钮是最稳妥的
  const buttons = Array.from(document.querySelectorAll("button"));
  const publishBtn = buttons.find((btn) => btn.innerText.includes("发布"));
  if (publishBtn) {
    publishBtn.click();
  }
}
```

## 3. 发前发后闭环调查 SOP (Pre/Post Research Flow)

- **前置调查 (Pre-flight Research)**：在网页版探索搜索页 `https://www.xiaohongshu.com/search_result?keyword={URL编码关键字}`。抓取前 10 篇高赞笔记的标题结构和痛点评论。
- **发布后复盘 (Post-flight Analysis)**：访问 `https://creator.xiaohongshu.com/data/core` (数据核心面板)，抓取曝光、阅读、互动转化漏斗数据，更新至 `memory/02_reflective/`。
