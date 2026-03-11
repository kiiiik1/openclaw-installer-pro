@echo off
REM OpenClaw Installer Pro - Windows 快速安装脚本

echo ========================================
echo   OpenClaw Installer Pro 安装程序
echo ========================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python
    echo 请先安装 Python 3.8 或更高版本
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] 检测到 Python
python --version
echo.

REM 升级 pip
echo [2/3] 升级 pip...
python -m pip install --upgrade pip

REM 安装依赖
echo [2/3] 安装依赖...
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo [错误] 依赖安装失败
    pause
    exit /b 1
)

echo.
echo [3/3] 启动程序...
python src/main.py

echo.
echo 如果程序启动失败，请检查上面的错误信息
pause
