# 第8章：快速开始

本章将指导你在最短时间内完成 OpenClaw 的安装、配置和首次使用，让你能够快速体验 OpenClaw 的强大功能。

## 8.1 系统要求

### 8.1.1 操作系统

OpenClaw 支持以下操作系统：

**支持的平台：**
- ✅ **Windows 10** 或更高版本
- ✅ **Windows 11**
- ✅ **Ubuntu 20.04** LTS 或更高版本
- ✅ **Ubuntu 22.04** LTS 或更高版本
- ✅ **Debian 11** 或更高版本
- ✅ **Fedora 35** 或更高版本
- ✅ **CentOS 8** 或更高版本
- ✅ **macOS 10.15** (Catalina) 或更高版本
- ✅ **macOS 11** (Big Sur) 或更高版本
- ✅ **macOS 12** (Monterey) 或更高版本
- ✅ **macOS 13** (Ventura) 或更高版本

**不支持的平台：**
- ❌ Windows 7 或更早版本
- ❌ Windows 8 或 8.1
- ❌ macOS 10.14 (Mojave) 或更早版本

### 8.1.2 硬件要求

**最低配置：**
- CPU: 双核 1.5 GHz
- 内存: 2 GB RAM
- 硬盘: 2 GB 可用空间
- 网络: 稳定的互联网连接

**推荐配置：**
- CPU: 四核 2.0 GHz 或更高
- 内存: 4 GB RAM 或更高
- 硬盘: 5 GB 可用空间或更高
- 网络: 宽带互联网连接

**高性能配置（用于生产环境）：**
- CPU: 八核 3.0 GHz 或更高
- 内存: 8 GB RAM 或更高
- 硬盘: 10 GB 可用空间或更高（SSD 推荐）
- 网络: 高速互联网连接，稳定的上行带宽

### 8.1.3 网络要求

OpenClaw 需要网络连接来：
- 与 AI 模型 API 通信
- 下载技能和依赖包
- 连接通讯平台（Discord、Telegram、QQ、WhatsApp 等）
- 访问外部工具和服务

**网络带宽：**
- 最低: 1 Mbps
- 推荐: 10 Mbps 或更高
- 高性能: 50 Mbps 或更高

**网络延迟：**
- 最低要求: < 500ms
- 推荐值: < 200ms
- 最佳体验: < 100ms

**防火墙/代理：**
如果您的网络环境需要代理，OpenClaw 支持通过配置代理访问外网：
```bash
# HTTP 代理
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080

# SOCKS 代理
export ALL_PROXY=socks5://proxy.example.com:1080
```

## 8.2 安装方式

OpenClaw 提供多种安装方式，以适应不同的使用场景和技术背景。

### 8.2.1 方式一：使用图形化安装器（推荐）

**适用人群：** 不熟悉命令行的用户、想要快速上手的用户

**步骤：**

**Windows：**
1. 下载 `OpenClaw-Installer-Pro.exe`
2. 双击运行安装程序
3. 按照界面提示完成安装
4. 安装完成后，从开始菜单启动 OpenClaw

**Linux：**
1. 下载 `openclaw-installer` 可执行文件
2. 赋予执行权限：`chmod +x openclaw-installer`
3. 运行安装器：`./openclaw-installer`
4. 按照图形界面提示完成配置

**macOS：**
1. 下载 `OpenClaw-Installer-Pro` 可执行文件
2. 赋予执行权限：`chmod +x OpenClaw-Installer-Pro`
3. 运行安装器：`./OpenClaw-Installer-Pro`
4. 按照图形界面提示完成配置

### 8.2.2 方式二：使用安装脚本

**适用人群：** 有一定命令行基础的用户

**Windows：**
```cmd
# 1. 下载源码包
unzip openclaw-installer-pro-v1.0.0.zip

# 2. 双击运行 install.bat
install.bat
```

**Linux/Mac：**
```bash
# 1. 下载源码包
unzip openclaw-installer-pro-v1.0.0.zip

# 2. 赋予执行权限
chmod +x install.sh

# 3. 运行安装脚本
./install.sh
```

### 8.2.3 方式三：从源码安装

**适用人群：** 开发者、需要定制安装的用户

**步骤：**

```bash
# 1. 克隆仓库
git clone https://github.com/kiiiik1/openclaw-installer-pro.git
cd openclaw-installer-pro

# 2. 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行程序
python src/main.py
```

### 8.2.4 方式四：使用 Docker

**适用人群：** 熟悉 Docker 的用户、需要隔离环境的用户

**步骤：**

```bash
# 1. 拉取镜像（如果提供了官方镜像）
docker pull openclaw/openclaw:latest

# 2. 运行容器
docker run -d \
  --name openclaw \
  -e OPENCLAW_MODEL_API="https://api.openai.com/v1/chat/completions" \
  -e OPENCLAW_MODEL_ID="gpt-4" \
  -e OPENCLAW_API_KEY="your-api-key" \
  openclaw/openclaw:latest

# 3. 查看日志
docker logs -f openclaw
```

**或使用 Docker Compose：**

```yaml
version: '3.8'
services:
  openclaw:
    image: openclaw/openclaw:latest
    environment:
      - OPENCLAW_MODEL_API=https://api.openai.com/v1/chat/completions
      - OPENCLAW_MODEL_ID=gpt-4
      - OPENCLAW_API_KEY=your-api-key
    volumes:
      - ./config:/home/openclaw/.openclaw
      - ./skills:/home/openclaw/.openclaw/extensions
    restart: unless-stopped
```

运行：
```bash
docker-compose up -d
```

## 8.3 首次配置

首次启动 OpenClaw 后，需要进行一些基本配置才能开始使用。

### 8.3.1 模型配置

OpenClaw 需要连接到大语言模型（LLM）才能工作。以下是支持的模型及其配置方式。

#### 配置界面（图形化）

使用图形化安装器时，会自动弹出配置窗口：

```
┌──────────────────────────────────────────┐
│        OpenClaw - 首次配置                │
├──────────────────────────────────────────┤
│                                          │
│  1. 模型地址:                             │
│  ┌────────────────────────────────────┐   │
│  │https://api.openai.com/v1/...    │   │
│  └────────────────────────────────────┘   │
│                                          │
│  2. 模型 ID:                              │
│  ┌────────────────────────────────────┐   │
│  │gpt-4                             │   │
│  └────────────────────────────────────┘   │
│                                          │
│  3. API Key:                              │
│  ┌────────────────────────────────────┐   │
│  │sk-...                             │   │
│  └────────────────────────────────────┘   │
│                                          │
│  4. 代理（可选）:                         │
│  ┌────────────────────────────────────┐   │
│  │http://192.168.48.1:7890          │   │
│  └────────────────────────────────────┘   │
│                                          │
│        [保存配置]  [取消]                  │
└──────────────────────────────────────────┘
```

#### 配置文件方式

配置文件位于 `~/.openclaw/config.yaml`：

```yaml
# OpenClaw 配置文件

# 模型配置
model:
  api_url: https://api.openai.com/v1/chat/completions
  model_id: gpt-4
  api_key: sk-your-api-key-here
  proxy: http://192.168.48.1:7890  # 可选

# 通讯平台配置
providers:
  discord:
    token: your-discord-bot-token
  telegram:
    token: your-telegram-bot-token

# 技能配置
skills:
  enabled:
    - weather
    - qqbot-cron
    - healthcheck
  directory: ~/.openclaw/extensions
```

### 8.3.2 渠道配置

配置通讯平台，让 OpenClaw 能够接收和发送消息。

#### Discord 配置

1. 访问 https://discord.com/developers/applications
2. 创建新应用（New Application）
3. 在 "Bot" 页面创建机器人
4. 复制机器人 Token
5. 在配置文件中添加：

```yaml
providers:
  discord:
    token: your-discord-bot-token
    prefix: !  # 命令前缀
```

#### Telegram 配置

1. 在 Telegram 中搜索 @BotFather
2. 发送 `/newbot` 创建新机器人
3. 按提示设置机器人名称和用户名
4. 复制获得的 Token
5. 在配置文件中添加：

```yaml
providers:
  telegram:
    token: your-telegram-bot-token
```

#### QQ 配置

使用 QQBot：

1. 访问 QQ 开放平台申请 Bot
2. 获取 Bot Token
3. 在配置文件中添加：

```yaml
providers:
  qqbot:
    app_id: your-app-id
    app_key: your-app-key
```

### 8.3.3 基础设置

#### 设置工作目录

OpenClaw 会在以下位置创建工作目录：
- Linux/Mac: `~/.openclaw/`
- Windows: `%USERPROFILE%\.openclaw\`

工作目录结构：
```
.openclaw/
├── config.yaml          # 主配置文件
├── logs/                # 日志文件
│   ├── gateway.log
│   └── provider.log
├── extensions/          # 技能目录
│   ├── weather/
│   ├── qqbot-cron/
│   └── ...
├── memory/              # 记忆文件
│   ├── MEMORY.md
│   └── 2024-01-01.md
└── workspace/           # 工作空间
    └── (你的工作文件)
```

#### 设置时区

OpenClaw 默认使用系统时区。如果需要手动设置：

```yaml
system:
  timezone: Asia/Shanghai
```

支持的时区列表：https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

#### 设置语言

OpenClaw 支持多语言：

```yaml
system:
  language: zh-CN  # 中文（简体）
  # 或
  language: en-US  # 英文
  # 或
  language: ja-JP  # 日语
```

#### 设置日志级别

控制日志的详细程度：

```yaml
logging:
  level: INFO  # DEBUG, INFO, WARNING, ERROR
  file: logs/openclaw.log
  max_size: 10MB
  backup_count: 5
```

## 8.4 验证安装

配置完成后，验证 OpenClaw 是否正常工作。

### 8.4.1 检查服务状态

```bash
# 检查 Gateway 是否运行
openclaw gateway status

# 检查各个 Provider 状态
openclaw provider list
```

### 8.4.2 发送测试消息

在已配置的通讯平台（如 Discord、Telegram）中，发送测试消息：

```
Hello, OpenClaw!
```

如果 OpenClaw 正常运行，它会回复类似：
```
Hello! 我是 OpenClaw，很高兴为你服务。
```

### 8.4.3 测试技能

发送命令测试技能是否正常：

```
/weather 北京
```

应该返回北京的天气信息。

### 8.4.4 查看日志

如果出现问题，查看日志文件：

```bash
# 查看最近的日志
tail -f ~/.openclaw/logs/gateway.log

# 或查看完整日志
cat ~/.openclaw/logs/gateway.log
```

## 8.5 常见安装问题

### 问题1：Python 版本不兼容

**错误信息：**
```
Python version 3.7 or higher is required
```

**解决方案：**
1. 升级 Python 到 3.8 或更高版本
2. 使用虚拟环境安装特定版本的 Python

### 问题2：依赖安装失败

**错误信息：**
```
ERROR: Could not find a version that satisfies the requirement xxx
```

**解决方案：**
1. 升级 pip：`python -m pip install --upgrade pip`
2. 使用国内镜像源：
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

### 问题3：权限错误（Linux/Mac）

**错误信息：**
```
Permission denied: '/usr/local/lib/python3.8'
```

**解决方案：**
1. 使用虚拟环境
2. 或使用 `--user` 参数：
   ```bash
   pip install --user -r requirements.txt
   ```

### 问题4：网络连接失败

**错误信息：**
```
Connection timeout
```

**解决方案：**
1. 检查网络连接
2. 配置代理：
   ```bash
   export http_proxy=http://proxy:port
   export https_proxy=http://proxy:port
   ```
3. 使用国内镜像源

### 问题5：Windows 上启动失败

**错误信息：**
```
'python' is not recognized as an internal or external command
```

**解决方案：**
1. 确保已安装 Python 3.8+
2. 将 Python 添加到系统 PATH
3. 重启命令行窗口

## 8.6 下一步

恭喜！你已经成功安装并配置了 OpenClaw。接下来你可以：

1. **学习基础使用** → 参考第9章：基础使用
2. **探索高级功能** → 参考第10章：高级功能
3. **开发自定义技能** → 参考第13章：技能开发
4. **部署到生产环境** → 参考第16章：部署最佳实践
5. **加入社区** → 访问 https://discord.com/invite/clawd

---

**提示：** 如果在安装过程中遇到问题，请查阅故障排除章节（第11章）或访问 OpenClaw 社区寻求帮助。
