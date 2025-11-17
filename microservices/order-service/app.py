from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Order Service is Running!"}

@app.get("/healthz")
def healthz():
    return {"status": "ok", "service": "order"}

@app.get("/orders/{oid}")
def get_order(oid: str):
    return {"id": oid, "item": "Demo Order"}
