# OpenClaw 默认技能包

这个目录包含了 OpenClaw Installer Pro 内置的技能配置。

## 技能列表

### 1. qqbot-cron

**描述**: QQBot 定时提醒技能。支持一次性和周期性提醒的创建、查询、取消。

**用途**:
- 设置定时提醒（如：10分钟后提醒我）
- 创建周期性任务（如：每天早上8点提醒我喝水）
- 查询和管理提醒

**安装方式**:
```bash
openclaw skills install qqbot-cron
```

### 2. qqbot-media

**描述**: QQBot 图片/语音/视频/文件收发能力。

**用途**:
- 接收和发送图片
- 接收和发送语音消息
- 接收和发送视频
- 文件传输

**安装方式**:
```bash
openclaw skills install qqbot-media
```

### 3. weather

**描述**: 获取当前天气和天气预报。

**用途**:
- 查询当前天气
- 获取未来几天预报
- 查询不同城市天气

**数据源**: wttr.in, Open-Meteo（无需 API Key）

**安装方式**:
```bash
openclaw skills install weather
```

### 4. healthcheck

**描述**: 系统安全加固和风险配置。

**用途**:
- 安全审计
- 防火墙配置
- SSH 加固
- 系统更新检查

**安装方式**:
```bash
openclaw skills install healthcheck
```

---

## 使用方法

这些技能会在安装 OpenClaw 时自动安装。安装后，通过聊天平台即可使用。

### 示例对话

**使用 qqbot-cron:**
```
你: 10分钟后提醒我喝水
AI: 好的，已设置10分钟后的提醒
```

**使用 weather:**
```
你: 北京今天天气怎么样
AI: [天气信息]
```

**使用 healthcheck:**
```
你: 检查系统安全状态
AI: [系统安全报告]
```

---

## 更多技能

更多技能请访问：
- GitHub: https://github.com/openclaw/awesome-openclaw-skills
- Gitee: https://gitee.com/devai/awesome-openclaw-skills

---

**OpenClaw Installer Pro** - 内置技能包
