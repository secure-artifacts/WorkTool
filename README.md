# 任务整理工具

This package is a cleaned release build of `任务整理工具`, prepared for GitHub and cross-machine setup.

## Files

- `main.py`: main application entry
- `launch.py`: creates a local virtual environment and installs dependencies
- `requirements.txt`: base runtime dependencies
- `run.bat`: Windows launcher
- `run.sh`: Linux/macOS launcher
- `config.json`: clean runtime configuration

## First run

### Windows

Double-click `run.bat`

### Linux or macOS

Run:

```bash
chmod +x run.sh
./run.sh
```

## Notes

- Dependencies are installed only into `.venv`
- The system Python environment is not modified
- Heavy AI libraries are still installed on demand when related features are used
- The interactive AI assistant tab was removed from the clean release
