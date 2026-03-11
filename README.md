# OpenClaw Installer Pro

OpenClaw 一键部署工具，为国内用户打造的简单易用的图形化安装器。

## ✨ 特性

- 🚀 **一键部署** - 下载、配置、启动 OpenClaw，全程图形化操作
- 🎯 **极简配置** - 只需填3项：模型地址、模型ID、Key
- 📦 **内置技能** - 预置常用技能，开箱即用
- 🔧 **智能适配** - 自动检测系统环境，适配国内网络
- 📖 **完整文档** - 附带产品说明和使用指南

## 📋 系统要求

- Windows 10/11 或 Linux (Ubuntu 20.04+)
- 网络连接（支持代理）
- 至少 2GB 可用磁盘空间

## 🛠️ 快速开始

### Windows 用户

1. 下载 `openclaw-installer-pro.exe`
2. 双击运行
3. 配置模型信息：
   - 模型地址：如 `https://api.example.com`
   - 模型ID：如 `glm-4`
   - API Key：你的密钥
4. 点击"开始安装"
5. 等待下载完成，自动启动

### Linux 用户

```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python src/main.py
```

## 📝 配置说明

| 配置项 | 说明 | 示例 |
|--------|------|------|
| 模型地址 | 大模型API的完整URL | `https://open.bigmodel.cn/api/paas/v4/chat/completions` |
| 模型ID | 使用的模型名称 | `glm-4` |
| API Key | 访问密钥 | `xxxxxxxxxxxxxxxx` |

## 🎓 内置技能

程序内置以下常用技能：
- qqbot-cron - QQ定时提醒
- qqbot-media - QQ媒体收发
- weather - 天气查询
- healthcheck - 系统健康检查

## 💰 支持项目

如果您觉得这个工具对您有帮助，欢迎通过支付宝扫描以下二维码支持：

<qqimg>https://raw.githubusercontent.com/kiiiik1/vip-soft/refs/heads/main/alipay.jpg</qqimg>

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**OpenClaw Installer Pro** - 让 AI 助手触手可及
