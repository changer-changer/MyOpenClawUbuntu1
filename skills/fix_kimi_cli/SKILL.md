---
name: Fix Kimi Code Connection
description: Resolves the "LLM provider error: Connection error" caused by Kimi-CLI's IPv6 / OS version detection issue.
---

# Kimi Code Connection Fix Skill

## 🔍 问题解析 (What is the issue?)

当你遇到 \`LLM provider error: Connection error\` 时，这通常发生在终端环境里的 Kimi 代码助手插件（\`kimi-cli\`）。

根源在于 Kimi 的官方 Python 客户端中，负责构建 HTTP 请求头（Headers）的代码逻辑存在一个兼容性 Bug。在部分 Linux 环境（特别是深度定制版本或者特定的网络配置下），Kimi 请求头中自动抓取的 \`X-Msh-Os-Version\` (获取自 \`platform.version()\`) 会导致服务端的安全策略拒绝连接，或者因为 IPv6 TLS 握手失败而超时。

每次你通过 \`uv\` 或 \`pip\` 更新了 \`kimi-cli\` 后，官方原本的有缺陷的代码就会重新覆盖我们修改过的代码，导致问题复发。

## 🛠️ 解决方案原理 (How it works?)

这个 Skill 的作用非常直接：

1. 定位你本地安装 \`kimi-cli\` 的位置。
2. 找到负责构建 Header 的核心文件 \`oauth.py\`。
3. 强行将获取系统版本的代码 \`platform.version()\` 替换为硬编码的字符串 \`"Linux-Custom"\`。

这样骗过服务端的环境检测后，连接错误就会立刻消失。

## 🚀 执行指南 (Execution)

如果再次遇到这个问题，你只需要**运行这个 Skill 目录下的自动修复脚**即可：

\`\`\`bash
bash ~/.openclaw/skills/fix_kimi_cli/scripts/apply_fix.sh
\`\`\`

---

_Agent 内部执行指令_:
当用户请求修复 kimi-cli 连接问题时，请使用 \`run_command\` 运行 \`bash ~/.openclaw/skills/fix_kimi_cli/scripts/apply_fix.sh\`。
