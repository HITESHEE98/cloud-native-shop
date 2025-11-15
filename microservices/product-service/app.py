from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Product Service is Running!"}

@app.get("/healthz")
def health():
    return {"status": "ok", "service": "product"}

@app.get("/products/{pid}")
def get_product(pid: str):
    # Simple dummy product
    return {"id": pid, "name": "Sample Product"}
