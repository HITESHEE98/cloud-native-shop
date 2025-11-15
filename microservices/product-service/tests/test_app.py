from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Product Service is Running!"

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["service"] == "product"

def test_product_dynamic():
    r = client.get("/products/123")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "123"
    assert "name" in data
