# MyOpenClawUbuntu1 - OpenClaw 完整备份

OpenClaw 配置、记忆和多 Agent 备份仓库

## 📁 备份内容

### 1. 主配置 (`config/`)
- `openclaw.json` - 主配置文件（已脱敏）

### 2. 工作区 (`workspace/`)
- **核心记忆文件**: AGENTS.md, USER.md, SOUL.md, MEMORY.md 等
- **历史记忆**: `memory/` 目录下的每日记录
- **多 Agent 配置**: `agents/` 目录下所有 agent 的结构
- **项目文件**: xhs-memory, 论文收集 等

### 3. Skills (`skills/`)
- 所有已安装的 skill 配置

### 4. Agents 详情
当前备份包含以下 Agents：
| Agent | 会话数 | 说明 |
|-------|--------|------|
| main | 2 | 主 Agent |
| engineer-musk | 1 | 工程师角色 |
| scientist | 0 | 科学家角色 |

---

## 🚀 快速开始

### 自动备份（推荐）

```bash
# 运行自动备份脚本
~/backup_openclaw.sh
```

脚本会自动：
1. 复制所有配置文件（脱敏）
2. 复制所有记忆文件
3. 复制所有 Agent 配置
4. 提交到 git
5. Push 到 GitHub

### 手动备份

```bash
cd ~/claw-backup

# 1. 运行同步脚本
./sync_from_openclaw.sh

# 2. 提交更改
git add .
git commit -m "Backup $(date '+%Y-%m-%d %H:%M:%S')"

# 3. Push
git push
```

---

## 📋 备份清单

### ✅ 包含的内容

- [x] OpenClaw 主配置 (`~/.openclaw/openclaw.json`)
- [x] 所有 Agent 配置 (`~/.openclaw/agents/*/agent/`)
- [x] Agent 认证结构（脱敏）
- [x] Agent 会话结构（脱敏）
- [x] Workspace 记忆文件 (`~/.openclaw/workspace/*.md`)
- [x] Workspace 历史记忆 (`~/.openclaw/workspace/memory/`)
- [x] Workspace 项目文件 (xhs-memory, 论文收集等)
- [x] Skill 配置 (`~/.openclaw/skills/`)
- [x] 定时任务配置 (`~/.openclaw/cron/`)

### ❌ 不包含的内容（大文件/敏感信息）

- [ ] 会话历史记录 (`.jsonl` 文件)
- [ ] Canvas 文件
- [ ] 日志文件
- [ ] 实际的 API Key 和 Token（已脱敏）
- [ ] node_modules
- [ ] Git 仓库

---

## 🔒 安全说明

### 脱敏处理
所有敏感信息已替换为占位符：

```json
// 原始
"token": "02b0e24314138266378fd77d375203e620cb32b05101e56c"

// 备份中
"token": "<YOUR_GATEWAY_TOKEN>"
```

### 需要手动恢复的敏感信息

恢复配置后，需要手动填入：
1. **Gateway Token** - 在 `config/openclaw.json` 中
2. **Telegram Bot Token** - 在 `config/openclaw.json` 中
3. **API Keys** - 在 `workspace/agents/*/agent/auth-profiles.json` 中

---

## 🔄 恢复步骤

### 1. 克隆仓库

```bash
git clone https://github.com/changer-changer/MyOpenClawUbuntu1.git
cd MyOpenClawUbuntu1
```

### 2. 恢复配置

```bash
# 运行恢复脚本
./restore_to_openclaw.sh
```

或手动复制：

```bash
# 主配置
cp config/openclaw.json ~/.openclaw/

# Workspace
cp -r workspace/* ~/.openclaw/workspace/

# Agents
for agent in workspace/agents/*/; do
    agent_name=$(basename "$agent")
    mkdir -p ~/.openclaw/agents/$agent_name
    cp -r workspace/agents/$agent_name/* ~/.openclaw/agents/$agent_name/
done
```

### 3. 填入敏感信息

编辑以下文件，填入真实的 API Key 和 Token：
- `~/.openclaw/openclaw.json` - Gateway Token, Telegram Bot Token
- `~/.openclaw/agents/*/agent/auth-profiles.json` - API Keys

### 4. 重启 OpenClaw

```bash
openclaw gateway restart
```

---

## 🛠️ 脚本说明

### `backup_openclaw.sh`
一键备份脚本，完成以下操作：
1. 同步文件到备份目录
2. 提交 git
3. Push 到 GitHub

### `sync_from_openclaw.sh`
从 OpenClaw 同步文件到备份目录：
- 脱敏处理
- 更新所有 agents
- 清理旧文件

### `restore_to_openclaw.sh`
从备份恢复到 OpenClaw：
- 复制配置文件
- 提醒填入敏感信息

---

## 📅 备份历史

| 日期 | 说明 |
|------|------|
| 2026-03-09 | 初始备份，3 个 agents，15 个 skills |

---

## 📝 维护说明

### 添加新的 Agent

当创建新 agent 时，备份会自动包含：
```bash
~/backup_openclaw.sh
```

### 排除特定文件

编辑 `.gitignore` 添加排除规则：
```gitignore
# 排除特定目录
workspace/some-large-project/

# 排除特定文件类型
*.log
*.tmp
```

### 更新备份频率建议

- **每次重大配置变更后**: 立即备份
- **每日**: 自动备份记忆文件
- **每周**: 完整备份检查

---

## ⚠️ 已知限制

1. **会话历史不备份**: 体积过大，且可重建
2. **Canvas 文件不备份**: 体积过大
3. **需要手动填入凭证**: 安全考虑，API Key 已脱敏

---

**最后更新**: 2026-03-09
**OpenClaw 版本**: 2026.2.26
**维护者**: changer-changer
