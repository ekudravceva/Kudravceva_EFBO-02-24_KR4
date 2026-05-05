import pytest
from fastapi.testclient import TestClient
from app.main import app, db

@pytest.fixture
def client():
    db.clear()
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_db():
    db.clear()
    yield
    db.clear()