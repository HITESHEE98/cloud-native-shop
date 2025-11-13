import os
import time
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import CollectorRegistry, Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

SERVICE_NAME = os.getenv("SERVICE_NAME", "user")

app = FastAPI(title=f"{SERVICE_NAME.capitalize()} Service", version="0.1.0")

# --- simple in-process metrics ---
registry = CollectorRegistry()
REQ_TOTAL = Counter("http_requests_total", "Total HTTP requests", ["service", "path", "method"], registry=registry)
UP_GAUGE = Gauge("service_up", "Service up (1=up,0=down)", ["service"], registry=registry)
START_TIME = time.time()
UP_GAUGE.labels(service=SERVICE_NAME).set(1)

@app.middleware("http")
async def metrics_middleware(request, call_next):
    response = await call_next(request)
    try:
        REQ_TOTAL.labels(service=SERVICE_NAME, path=request.url.path, method=request.method).inc()
    except Exception:
        pass
    return response

@app.get("/")
def root():
    return {"message": f"{SERVICE_NAME.capitalize()} Service is Running!"}

@app.get("/healthz")
def healthz():
    return {"status": "ok", "service": SERVICE_NAME}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"id": user_id, "name": "Demo User"}

@app.get("/metrics")
def metrics():
    data = generate_latest(registry)
    return PlainTextResponse(content=data, media_type=CONTENT_TYPE_LATEST)
