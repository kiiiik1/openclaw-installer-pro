@echo off
REM OpenClaw Installer Pro - Windows Setup Script

echo ========================================
echo   OpenClaw Installer Pro Setup
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not detected
    echo Please install Python 3.8 or higher
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Python detected
python --version
echo.

REM Upgrade pip
echo [2/3] Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo [2/3] Installing dependencies...
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo [ERROR] Dependencies installation failed
    pause
    exit /b 1
)

echo.
echo [3/3] Starting application...
python src/main.py

echo.
echo If the application fails to start, please check the error messages above
pause
