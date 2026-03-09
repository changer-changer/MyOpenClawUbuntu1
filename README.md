# MyOpenClawUbuntu1

OpenClaw 配置和记忆备份仓库

## 📁 目录结构

```
.
├── config/              # 配置文件（脱敏）
│   └── openclaw.json   # 主配置
├── workspace/          # 工作区文件
│   ├── *.md           # 核心记忆文件
│   ├── memory/        # 历史记忆
│   └── agents/        # Agent 配置
├── skills/            # Skill 配置
└── README.md          # 本文件
```

## 🔒 安全说明

- 所有 API Key 和 Token 都已脱敏（替换为占位符）
- 会话历史记录未包含（体积过大）
- 恢复时需要手动填入真实凭证

## 🔄 恢复步骤

1. 克隆仓库
2. 复制配置文件到 `~/.openclaw/`
3. 填入真实的 API Key
4. 重启 OpenClaw 网关

## 📝 备份内容

- [x] OpenClaw 主配置
- [x] 记忆文件 (MEMORY.md, USER.md, SOUL.md 等)
- [x] 历史记忆记录
- [x] Agent 配置结构
- [x] Skill 配置
- [ ] 会话历史（体积过大，不备份）
- [ ] Canvas 文件（体积过大，不备份）

## 🏷️ 版本

- OpenClaw: 2026.2.26
- 备份日期: $(date '+%Y-%m-%d %H:%M:%S')
