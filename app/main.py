from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from app.routers.metrics import router as metrics_router

app = FastAPI(title="Portfolio API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(metrics_router)
from app.routers.items import router as items_router
app.include_router(items_router)
