# Ubuntu + Android 知识库同步方案

## 你的需求
- ✅ 类似WPS：本地文件夹 ↔ 云端 ↔ 手机 双向同步
- ✅ 支持 Ubuntu
- ✅ 支持 Markdown/txt
- ✅ 小白友好

---

## 🥇 推荐：坚果云（完美替代WPS同步）

### 为什么选坚果云
| 功能 | WPS会员 | 坚果云 |
|------|---------|--------|
| 本地文件夹映射 | ✅ | ✅ |
| Ubuntu支持 | ❌ | ✅ 官方客户端 |
| WebDAV挂载 | ❌ | ✅ 更灵活 |
| Markdown支持 | ❌ | ✅ 配合Obsidian |
| 国内速度 | 快 | 快 |

### Ubuntu 安装坚果云

#### 方法一：官方客户端（推荐）
```bash
# 下载deb包
wget https://www.jianguoyun.com/static/exe/installer/nutstore_linux_src_installer.tar.gz

# 解压安装
tar -zxvf nutstore_linux_src_installer.tar.gz
cd nutstore_linux_src_installer
./install.sh
```

#### 方法二：如果你是坚果云会员（WebDAV挂载为本地磁盘）⭐更WPS-like
```bash
# 安装davfs2
sudo apt install davfs2

# 创建挂载点
mkdir -p ~/NutstoreWebDAV

# 挂载坚果云WebDAV（需要你的WebDAV地址和密码）
sudo mount -t davfs https://dav.jianguoyun.com/dav/ ~/NutstoreWebDAV
```

**WebDAV优点**：
- 知识库文件夹像本地磁盘一样使用
- 任何软件（Obsidian/VS Code/Typora）直接打开编辑
- 实时同步，和WPS体验几乎一样

---

## 📝 编辑工具推荐（Ubuntu上）

### 方案1：Obsidian（最推荐）
```bash
# 下载AppImage
wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.5.3/Obsidian-1.5.3.AppImage

# 赋予执行权限
chmod +x Obsidian-1.5.3.AppImage

# 运行
./Obsidian-1.5.3.AppImage
```
- 打开坚果云同步下来的知识库文件夹
- 完美支持Markdown
- 和Windows/Mac体验一致

### 方案2：VS Code
```bash
sudo snap install code --classic
```
- 安装 Markdown 插件
- 适合喜欢代码编辑器的用户

### 方案3：Typora（Markdown专用编辑器）
```bash
# 下载安装
wget -qO - https://typora.io/linux/public-key.asc | sudo tee /etc/apt/trusted.gpg.d/typora.asc
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt update
sudo apt install typora
```
- 所见即所得的Markdown编辑
- 简洁美观

---

## 📱 Android端配合

1. **安装坚果云App**
   - 自动同步知识库到手机

2. **安装Obsidian App**
   - 打开坚果云里的知识库文件夹
   - 或者直接用坚果云内置Markdown预览

---

## 🎯 最终推荐配置

```
Ubuntu电脑
├── 坚果云客户端（同步知识库到 ~/Nutstore/知识库/）
└── Obsidian → 打开 ~/Nutstore/知识库/
       ↓ 自动同步
坚果云服务器
       ↓ 自动同步
Android手机
├── 坚果云App（文件管理）
└── Obsidian App（知识库浏览编辑）
```

---

## 💡 会员对比

如果你已经有WPS会员，可以考虑：
- **保留WPS会员**：在Windows上继续用（双系统的话）
- **坚果云免费版**：每月1G上传/3G下载，txt知识库够用
- **坚果云付费版**：30元/月，无限流量，比WPS便宜

---

## ⚠️ 注意

1. **WebDAV模式**：坚果云WebDAV有流量限制（免费版），但同步txt足够
2. **文件冲突**：如果同时在两端编辑同一文件，会产生冲突副本
3. **大文件**：txt知识库一般很小，不用担心

