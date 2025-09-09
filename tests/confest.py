import pytest
from app.database import Base, engine

@pytest.fixture(autouse=True)
def clean_db():
    # wipe and recreate schema for a clean slate every test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
