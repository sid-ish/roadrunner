from fastapi import APIRouter
from app.services.detection_service import get_detections

router = APIRouter()

@router.get("/{job_id}")
def detections(job_id: str):
    return get_detections(job_id)
