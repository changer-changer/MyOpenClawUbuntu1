#!/bin/bash
# 从备份恢复 OpenClaw 配置

set -e

BACKUP_DIR="$(cd "$(dirname "$0")" && pwd)"
OPENCLAW_DIR="$HOME/.openclaw"

echo "=========================================="
echo "🔄 从备份恢复 OpenClaw"
echo "=========================================="
echo ""
echo "备份目录: $BACKUP_DIR"
echo "目标目录: $OPENCLAW_DIR"
echo ""

# 确认
read -p "⚠️  这将覆盖现有的 OpenClaw 配置，确定继续? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "已取消"
    exit 0
fi

# 创建备份
backup_time=$(date +%Y%m%d_%H%M%S)
if [ -d "$OPENCLAW_DIR" ]; then
    echo "📦 创建现有配置备份..."
    cp -r "$OPENCLAW_DIR" "${OPENCLAW_DIR}.backup.${backup_time}"
    echo "  ✅ 已备份到: ${OPENCLAW_DIR}.backup.${backup_time}"
fi

echo ""
echo "🔄 开始恢复..."

# 1. 恢复主配置
echo ""
echo "📝 恢复主配置..."
if [ -f "$BACKUP_DIR/config/openclaw.json" ]; then
    mkdir -p "$OPENCLAW_DIR"
    
    # 提示填入敏感信息
    echo ""
    echo "  ⚠️  注意: 配置文件中的敏感信息需要手动填入"
    echo "     - Gateway Token"
    echo "     - Telegram Bot Token"
    echo "     - API Keys"
    
    cp "$BACKUP_DIR/config/openclaw.json" "$OPENCLAW_DIR/"
    echo "  ✅ config/openclaw.json"
fi

# 2. 恢复 Workspace
echo ""
echo "📂 恢复 Workspace..."
if [ -d "$BACKUP_DIR/workspace" ]; then
    mkdir -p "$OPENCLAW_DIR/workspace"
    
    # 复制所有文件
    cp -r "$BACKUP_DIR/workspace/"* "$OPENCLAW_DIR/workspace/" 2>/dev/null || true
    echo "  ✅ workspace/"
fi

# 3. 恢复 Agents
echo ""
echo "👤 恢复 Agents..."
if [ -d "$BACKUP_DIR/workspace/agents" ]; then
    for agent_dir in "$BACKUP_DIR/workspace/agents/"*/; do
        if [ -d "$agent_dir" ]; then
            agent_name=$(basename "$agent_dir")
            echo "  Agent: $agent_name"
            
            mkdir -p "$OPENCLAW_DIR/agents/$agent_name"
            cp -r "$agent_dir"* "$OPENCLAW_DIR/agents/$agent_name/" 2>/dev/null || true
            
            echo "    ✅ 配置已恢复"
            echo "    ⚠️  需要填入 API Key: ~/.openclaw/agents/$agent_name/agent/auth-profiles.json"
        fi
    done
fi

# 4. 恢复 Skills
echo ""
echo "🛠️  恢复 Skills..."
if [ -d "$BACKUP_DIR/skills" ]; then
    mkdir -p "$OPENCLAW_DIR/skills"
    
    for skill_dir in "$BACKUP_DIR/skills/"*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            mkdir -p "$OPENCLAW_DIR/skills/$skill_name"
            cp -r "$skill_dir"* "$OPENCLAW_DIR/skills/$skill_name/" 2>/dev/null || true
        fi
    done
    
    skill_count=$(ls -1 "$BACKUP_DIR/skills/" 2>/dev/null | wc -l)
    echo "  ✅ $skill_count 个 skills"
fi

echo ""
echo "=========================================="
echo "✅ 恢复完成!"
echo "=========================================="
echo ""
echo "⚠️  重要: 需要手动填入敏感信息"
echo ""
echo "编辑以下文件，填入真实的 API Key 和 Token:"
echo ""
echo "1. Gateway Token:"
echo "   ~/.openclaw/openclaw.json"
echo "   路径: gateway.auth.token"
echo ""
echo "2. Telegram Bot Token (如启用):"
echo "   ~/.openclaw/openclaw.json"
echo "   路径: channels.telegram.botToken"
echo ""
echo "3. API Keys (每个 Agent):"
echo "   ~/.openclaw/agents/*/agent/auth-profiles.json"
echo "   路径: profiles.*.key"
echo ""
echo "完成后重启 OpenClaw:"
echo "   openclaw gateway restart"
echo ""
