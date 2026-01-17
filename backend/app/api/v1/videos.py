from fastapi import APIRouter
from app.services.video_service import list_videos

router = APIRouter()

@router.get("/")
def videos():
    return list_videos()
