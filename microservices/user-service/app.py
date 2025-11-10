from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "User Service is Running!"}

@app.get("/healthz")
def health():
    return {"status": "ok", "service": "user"}

@app.get("/users/{uid}")
def get_user(uid: str):
    return {"id": uid, "name": "Demo User"}
