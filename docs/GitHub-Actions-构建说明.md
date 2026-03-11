# GitHub Actions 自动构建

本项目使用 GitHub Actions 自动构建多平台可执行文件。

## 📦 构建流程

### 自动构建（推荐）

当你发布新的 Release 时，GitHub Actions 会自动构建以下平台的可执行文件：

- ✅ **Windows** - `OpenClaw-Installer-Pro.exe`
- ✅ **Linux** - `openclaw-installer`
- ✅ **macOS** - `OpenClaw-Installer-Pro`
- ✅ **源码包** - `.zip` 文件

### 手动触发构建

你也可以手动触发构建流程：

1. 访问 GitHub 仓库
2. 点击 "Actions" 标签
3. 选择对应的工作流：
   - "Build Windows Executable" - 构建 Windows 版本
   - "Build Linux Executable" - 构建 Linux 版本
   - "Build macOS Executable" - 构建 macOS 版本
   - "Build Source Distribution" - 构建源码包
4. 点击 "Run workflow"

## 🚀 发布新版本

### 方法一：通过 GitHub 网页（推荐）

1. 访问 https://github.com/kiiiik1/openclaw-installer-pro/releases/new
2. 创建新标签（如 `v1.0.1`）
3. 填写版本标题和说明
4. 点击 "Publish release"
5. 等待 GitHub Actions 自动构建完成
6. 构建完成后，可执行文件会自动上传到 Release

### 方法二：使用 GitHub CLI

```bash
# 创建 Release 并自动构建所有平台
gh release create v1.0.1 \
  --title "v1.0.1 - 版本说明" \
  --notes "版本更新内容..."
```

## 📋 构建产物

### Windows
- **文件名**: `OpenClaw-Installer-Pro.exe`
- **大小**: 约 60-80MB
- **用途**: Windows 系统，可直接运行（无需 Python）

### Linux
- **文件名**: `openclaw-installer`
- **大小**: 约 60-80MB
- **用途**: Linux 系统，可直接运行（无需 Python）

### macOS
- **文件名**: `OpenClaw-Installer-Pro`
- **大小**: 约 60-80MB
- **用途**: macOS 系统，可直接运行（无需 Python）

### 源码包
- **文件名**: `openclaw-installer-pro-vX.Y.Z.zip`
- **大小**: 约 20KB
- **用途**: 所有平台，需要 Python 运行环境

## 🔧 工作流配置

工作流文件位于 `.github/workflows/` 目录：

- `build-windows.yml` - Windows 构建
- `build-linux.yml` - Linux 构建
- `build-macos.yml` - macOS 构建
- `build-source.yml` - 源码打包
- `release-all.yml` - 联合构建（Release 时）

## 📊 构建时间

- Windows: 约 3-5 分钟
- Linux: 约 2-3 分钟
- macOS: 约 3-5 分钟
- 源码包: 约 1 分钟

## ⚠️ 注意事项

1. **首次构建可能需要较长时间**，因为需要下载依赖
2. **构建失败时**，检查 Actions 日志查看错误信息
3. **Windows 可执行文件**首次运行可能被安全软件拦截，需要在 Windows 设置中允许
4. **Linux 可执行文件**需要赋予执行权限：`chmod +x openclaw-installer`
5. **macOS 可执行文件**首次运行可能需要授权

## 🆘 常见问题

### Q: 构建失败了怎么办？

A: 检查 Actions 页面的构建日志，查看具体错误信息。常见原因：
- 依赖安装失败
- PyInstaller 配置问题
- 代码语法错误

### Q: 如何查看构建进度？

A: 访问 GitHub 仓库的 "Actions" 标签，可以实时查看构建进度和日志。

### Q: 可以下载构建产物吗？

A: 可以。在 Actions 页面中，每个成功的构建都会提供下载链接。

### Q: 能否自定义构建参数？

A: 可以编辑 `.github/workflows/` 下的工作流文件，修改 PyInstaller 参数。

---

**Happy Building! 🚀**
