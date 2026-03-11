#!/bin/bash
# OpenClaw Installer Pro - Linux/Mac 快速安装脚本

echo "========================================"
echo "  OpenClaw Installer Pro 安装程序"
echo "========================================"
echo

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未检测到 Python3"
    echo "请先安装 Python 3.8 或更高版本"
    echo "Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "macOS: brew install python3"
    exit 1
fi

echo "[1/3] 检测到 Python3"
python3 --version
echo

# 升级 pip
echo "[2/3] 升级 pip..."
python3 -m pip install --upgrade pip --user

# 安装依赖
echo "[2/3] 安装依赖..."
python3 -m pip install -r requirements.txt --user

if [ $? -ne 0 ]; then
    echo "[错误] 依赖安装失败"
    exit 1
fi

echo
echo "[3/3] 启动程序..."
python3 src/main.py

echo
echo "如果程序启动失败，请检查上面的错误信息"
