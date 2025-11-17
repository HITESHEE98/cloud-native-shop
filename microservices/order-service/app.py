from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # or ["https://literate-goldfish-r664g4pxr44hw6-5173.app.github.dev"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Order Service is Running!"}

@app.get("/healthz")
def healthz():
    return {"status": "ok", "service": "order"}

@app.get("/orders/{oid}")
def get_order(oid: str):
    return {"id": oid, "item": "Demo Order"}
