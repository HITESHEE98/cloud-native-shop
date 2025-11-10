from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "User Service is Running!"

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["service"] == "user"

def test_user_dynamic():
    r = client.get("/users/42")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "42"
    assert "name" in data
