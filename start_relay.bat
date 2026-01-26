@echo off
REM Stream Proxy Server - Windows Launcher
REM This script starts the Python stream proxy (no FFmpeg required)

echo.
echo ========================================
echo    Stream Proxy Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from python.org
    pause
    exit /b 1
)

echo Starting stream proxy...
echo.
python "%~dp0stream_relay.py"

pause
