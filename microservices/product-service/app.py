from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
