"""Run Alembic migrations to initialize the database schema."""
from alembic import command
from alembic.config import Config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def run_migrations() -> None:
    """Apply all pending Alembic migrations."""
    alembic_cfg = Config(str(BASE_DIR / "alembic.ini"))
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":  # pragma: no cover
    run_migrations()
