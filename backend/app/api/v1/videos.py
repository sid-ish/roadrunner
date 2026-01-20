from fastapi import APIRouter, UploadFile, File
import uuid, shutil, os

router = APIRouter()

VIDEO_DIR = "data/videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    out_path = os.path.join(VIDEO_DIR, f"{job_id}.mp4")

    with open(out_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "job_id": job_id
    }
