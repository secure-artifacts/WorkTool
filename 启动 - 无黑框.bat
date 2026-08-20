@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" goto no_venv
if not exist "main.py" goto no_main

echo Starting main.py
call ".venv\Scripts\pythonw.exe" "main.py"
echo.
echo Exit code: %errorlevel%
pause
exit /b 0

:no_venv
echo venv not found. Run install.bat first.
pause
exit /b 1

:no_main
echo main.py not found in current folder.
pause
exit /b 1
