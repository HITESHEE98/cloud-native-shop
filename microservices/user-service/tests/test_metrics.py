import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastapi.testclient import TestClient
from app import app

def test_metrics_endpoint():
    c = TestClient(app)
    r = c.get("/metrics")
    assert r.status_code == 200
    # basic sanity: Prometheus output should include a HELP/TYPE line
    assert "service_up" in r.text
    assert "http_requests_total" in r.text
