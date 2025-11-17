from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Order Service is Running!"


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    body = r.json()
    assert body["service"] == "order"
    assert body["status"] == "ok"


def test_order_dynamic():
    r = client.get("/orders/42")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "42"
    assert "item" in data
