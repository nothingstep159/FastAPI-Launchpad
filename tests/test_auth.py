from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def test_signup_login_me():
    email = f"{uuid.uuid4().hex[:8]}@b.com"   # unique each run
    r = client.post("/auth/signup", json={"email": email, "password": "password123"})
    assert r.status_code == 201

    r = client.post("/auth/login", json={"email": email, "password": "password123"})
    assert r.status_code == 200
    token = r.json()["access_token"]

    r = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["email"] == email
