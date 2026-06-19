from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Backend Deployment Success 🚀",
        "status": "running",
        "timestamp": datetime.now()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }