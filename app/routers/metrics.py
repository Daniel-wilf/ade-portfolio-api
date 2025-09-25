from fastapi import APIRouter
from app.schemas.metrics import Metrics

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("", response_model=Metrics)
def get_metrics():
    return Metrics(uptime="100 hours", users=42)
