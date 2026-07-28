@echo off
setlocal
cd /d "%~dp0"

echo [1/6] Check Python 3.11
py -3.11 -V >nul 2>nul
if errorlevel 1 goto no_python

if not exist ".venv\Scripts\python.exe" (
    echo [2/6] Create venv
    py -3.11 -m venv .venv
    if errorlevel 1 goto venv_fail
) else (
    echo [2/6] Use existing venv
)

echo [3/6] Upgrade pip tools
call ".venv\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel
if errorlevel 1 goto pip_fail

echo [4/6] Install base requirements
call ".venv\Scripts\python.exe" -m pip install -r "requirements-base.txt"
if errorlevel 1 goto base_fail

echo [5/6] Install torch cpu
call ".venv\Scripts\python.exe" -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
if errorlevel 1 goto torch_fail

echo [6/6] Install ai requirements
call ".venv\Scripts\python.exe" -m pip install -r "requirements-ai.txt"
if errorlevel 1 goto ai_fail

echo.
echo Install finished.
echo Optional packages:
echo .venv\Scripts\python.exe -m pip install -r "requirements-ai-optional.txt"
pause
exit /b 0

:no_python
echo Python 3.11 not found.
pause
exit /b 1

:venv_fail
echo Failed to create venv.
pause
exit /b 1

:pip_fail
echo Failed to upgrade pip tools.
pause
exit /b 1

:base_fail
echo Failed to install base requirements.
pause
exit /b 1

:torch_fail
echo Failed to install torch packages.
pause
exit /b 1

:ai_fail
echo Failed to install ai requirements.
pause
exit /b 1
