#!/bin/bash
# 从 OpenClaw 同步文件到备份目录

set -e

OPENCLAW_DIR="$HOME/.openclaw"
BACKUP_DIR="$HOME/claw-backup"

echo "=========================================="
echo "🔄 同步 OpenClaw 到备份目录"
echo "=========================================="
echo ""

# 检查目录
if [ ! -d "$OPENCLAW_DIR" ]; then
    echo "❌ OpenClaw 目录不存在: $OPENCLAW_DIR"
    exit 1
fi

cd "$BACKUP_DIR"

# 创建目录结构
mkdir -p config
mkdir -p workspace/agents
mkdir -p workspace/memory
mkdir -p skills
mkdir -p cron

echo "📁 目录结构已创建"
echo ""

# 1. 同步主配置（脱敏）
echo "📝 处理主配置..."
python3 << 'PYTHON'
import json
import os

openclaw_dir = os.path.expanduser("~/.openclaw")
backup_dir = os.path.expanduser("~/claw-backup")

# 读取原始配置
config_path = os.path.join(openclaw_dir, "openclaw.json")
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # 脱敏处理
    # Gateway token
    if 'gateway' in config and 'auth' in config['gateway']:
        if 'token' in config['gateway']['auth']:
            config['gateway']['auth']['token'] = '<YOUR_GATEWAY_TOKEN>'
    
    # Channel tokens
    if 'channels' in config:
        for channel, settings in config['channels'].items():
            if isinstance(settings, dict):
                if 'botToken' in settings:
                    settings['botToken'] = f'<YOUR_{channel.upper()}_BOT_TOKEN>'
                if 'token' in settings:
                    settings['token'] = f'<YOUR_{channel.upper()}_TOKEN>'
    
    # Auth profiles (只保留结构，删除密钥)
    if 'auth' in config and 'profiles' in config['auth']:
        for profile_id, profile in config['auth']['profiles'].items():
            if 'key' in profile:
                profile['key'] = f'<YOUR_API_KEY_FOR_{profile_id}>'
    
    # 保存脱敏配置
    with open(os.path.join(backup_dir, 'config/openclaw.json'), 'w') as f:
        json.dump(config, f, indent=2)
    
    print("  ✓ openclaw.json (已脱敏)")
else:
    print("  ⚠ openclaw.json 不存在")
PYTHON

# 2. 同步 Workspace 文件
echo ""
echo "📂 同步 Workspace 文件..."

# 复制所有 .md 文件
for file in "$OPENCLAW_DIR/workspace/"*.md; do
    if [ -f "$file" ]; then
        cp "$file" "$BACKUP_DIR/workspace/"
        echo "  ✓ $(basename "$file")"
    fi
done

# 复制 memory 目录
if [ -d "$OPENCLAW_DIR/workspace/memory" ]; then
    rsync -av --delete "$OPENCLAW_DIR/workspace/memory/" "$BACKUP_DIR/workspace/memory/" 2>/dev/null || \
    cp -r "$OPENCLAW_DIR/workspace/memory/"* "$BACKUP_DIR/workspace/memory/" 2>/dev/null || true
    echo "  ✓ memory/"
fi

# 复制其他重要目录（排除大文件）
for dir in xhs-memory 论文收集 我的知识库; do
    if [ -d "$OPENCLAW_DIR/workspace/$dir" ]; then
        mkdir -p "$BACKUP_DIR/workspace/$dir"
        # 排除 git 仓库和大文件
        rsync -av --delete \
            --exclude='.git' \
            --exclude='node_modules' \
            --exclude='*.pyc' \
            --exclude='__pycache__' \
            "$OPENCLAW_DIR/workspace/$dir/" "$BACKUP_DIR/workspace/$dir/" 2>/dev/null || true
        echo "  ✓ $dir/"
    fi
done

# 3. 同步所有 Agents
echo ""
echo "👤 同步 Agents..."

for agent_dir in "$OPENCLAW_DIR/agents/"*/; do
    if [ -d "$agent_dir" ]; then
        agent_name=$(basename "$agent_dir")
        echo "  Agent: $agent_name"
        
        # 创建 agent 目录结构
        mkdir -p "$BACKUP_DIR/workspace/agents/$agent_name/agent"
        mkdir -p "$BACKUP_DIR/workspace/agents/$agent_name/sessions"
        
        # 复制 agent 配置（脱敏）
        if [ -f "$agent_dir/agent/auth-profiles.json" ]; then
            python3 << PYTHON
import json
import os

auth_path = "$agent_dir/agent/auth-profiles.json"
backup_path = "$BACKUP_DIR/workspace/agents/$agent_name/agent/auth-profiles.json"

with open(auth_path, 'r') as f:
    auth = json.load(f)

# 脱敏所有密钥
for profile_id, profile in auth.get('profiles', {}).items():
    if 'key' in profile:
        profile['key'] = '<YOUR_API_KEY>'

os.makedirs(os.path.dirname(backup_path), exist_ok=True)
with open(backup_path, 'w') as f:
    json.dump(auth, f, indent=2)
PYTHON
            echo "    ✓ auth-profiles.json (已脱敏)"
        fi
        
        # 复制 sessions 结构（不包含历史）
        if [ -f "$agent_dir/sessions/sessions.json" ]; then
            python3 << PYTHON
import json
import os

sessions_path = "$agent_dir/sessions/sessions.json"
backup_path = "$BACKUP_DIR/workspace/agents/$agent_name/sessions/sessions.json"

with open(sessions_path, 'r') as f:
    sessions = json.load(f)

# 清空会话内容，只保留结构
if 'sessions' in sessions:
    sessions['sessions'] = {}

os.makedirs(os.path.dirname(backup_path), exist_ok=True)
with open(backup_path, 'w') as f:
    json.dump(sessions, f, indent=2)
PYTHON
            echo "    ✓ sessions.json (结构)"
        fi
        
        # 复制其他配置文件
        for file in agent.json models.json; do
            if [ -f "$agent_dir/agent/$file" ]; then
                cp "$agent_dir/agent/$file" "$BACKUP_DIR/workspace/agents/$agent_name/agent/" 2>/dev/null || true
            fi
        done
    fi
done

# 4. 同步 Skills
echo ""
echo "🛠️  同步 Skills..."
skill_count=0
for skill_dir in "$OPENCLAW_DIR/skills/"*/; do
    if [ -f "$skill_dir/SKILL.md" ]; then
        skill_name=$(basename "$skill_dir")
        mkdir -p "$BACKUP_DIR/skills/$skill_name"
        cp "$skill_dir/SKILL.md" "$BACKUP_DIR/skills/$skill_name/"
        ((skill_count++)) || true
    fi
done
echo "  ✓ $skill_count 个 skills"

# 5. 同步定时任务配置
echo ""
echo "⏰ 同步定时任务..."
if [ -f "$OPENCLAW_DIR/cron/jobs.json" ]; then
    cp "$OPENCLAW_DIR/cron/jobs.json" "$BACKUP_DIR/cron/"
    echo "  ✓ cron/jobs.json"
fi

# 6. 生成备份报告
echo ""
echo "📊 备份统计:"
echo "  Agents: $(ls $BACKUP_DIR/workspace/agents/ 2>/dev/null | wc -l)"
echo "  Skills: $(ls $BACKUP_DIR/skills/ 2>/dev/null | wc -l)"
echo "  记忆文件: $(ls $BACKUP_DIR/workspace/memory/ 2>/dev/null | wc -l)"
echo "  核心文档: $(ls $BACKUP_DIR/workspace/*.md 2>/dev/null | wc -l)"

echo ""
echo "=========================================="
echo "✅ 同步完成"
echo "=========================================="
echo ""
echo "下一步:"
echo "  提交更改: git add . && git commit -m 'Backup $(date)'"
echo "  推送到 GitHub: git push"
