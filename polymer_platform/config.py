from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "polymer_platform.db"


def get_database_path() -> Path:
    return DATABASE_PATH
