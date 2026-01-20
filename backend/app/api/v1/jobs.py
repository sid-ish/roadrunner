from fastapi import APIRouter
from app.schemas.job import JobCreate, JobResponse
from app.services.job_service import create_job, get_job_status

router = APIRouter()

@router.post("/", response_model=JobResponse)
def create(job: JobCreate):
    # Creates job + enqueues to Redis
    return create_job(job)

@router.get("/{job_id}")
def status(job_id: str):
    return get_job_status(job_id)
