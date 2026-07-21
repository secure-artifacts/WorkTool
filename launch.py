from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import venv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
VENV_DIR = PROJECT_DIR / ".venv"
REQUIREMENTS = PROJECT_DIR / "requirements.txt"
MARKER = VENV_DIR / ".requirements.sha256"
MAIN_FILE = PROJECT_DIR / "main.py"


def in_project_venv() -> bool:
    try:
        return Path(sys.prefix).resolve() == VENV_DIR.resolve()
    except Exception:
        return False


def venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str]) -> None:
    subprocess.check_call(cmd, cwd=str(PROJECT_DIR))


def ensure_venv() -> None:
    if not VENV_DIR.exists():
        print("Creating project virtual environment...")
        venv.EnvBuilder(with_pip=True, clear=False, upgrade_deps=False).create(str(VENV_DIR))


def ensure_main_file() -> None:
    if not MAIN_FILE.exists():
        raise FileNotFoundError(
            f"Main entry file not found: {MAIN_FILE.name}. "
            "Please ensure launch.py and main.py are in the same folder."
        )


def ensure_requirements() -> None:
    if not REQUIREMENTS.exists():
        print("requirements.txt not found, skipping dependency installation.")
        return

    wanted = file_hash(REQUIREMENTS)
    current = MARKER.read_text(encoding="utf-8").strip() if MARKER.exists() else ""
    if current == wanted:
        return

    py = str(venv_python())
    print("Installing project dependencies into the virtual environment...")
    run([py, "-m", "pip", "install", "--upgrade", "pip"])
    run([py, "-m", "pip", "install", "-r", str(REQUIREMENTS)])
    MARKER.write_text(wanted, encoding="utf-8")


def main() -> None:
    ensure_venv()
    ensure_main_file()
    ensure_requirements()
    py = str(venv_python())
    os.execv(py, [py, str(MAIN_FILE), *sys.argv[1:]])


if __name__ == "__main__":
    main()
