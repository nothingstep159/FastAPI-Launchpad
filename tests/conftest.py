import os
import pytest
from scripts.init_db import run_migrations


@pytest.fixture(autouse=True)
def clean_db():
    """Ensure a clean database for each test run."""
    if os.path.exists("app.db"):
        os.remove("app.db")
    run_migrations()
    yield
