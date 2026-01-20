from sqlalchemy.orm import Session
from redis import Redis

from app.db.session import SessionLocal
from app.db.models.job import Job
from app.schemas.job import JobCreate
from app.core.config import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    REDIS_JOB_QUEUE,
)

# Redis client (sync, lightweight)
redis_client = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
)

def create_job(payload: JobCreate):
    db: Session = SessionLocal()
    try:
        # Create DB job
        job = Job(
            youtube_url=payload.youtube_url,
            status="queued",
        )
        db.add(job)
        db.commit()
        db.refresh(job)

        # Push job ID to Redis queue
        # Worker will consume this later
        redis_client.rpush(REDIS_JOB_QUEUE, job.id)

        return {
            "job_id": job.id,
            "status": job.status,
        }
    finally:
        db.close()

def get_job_status(job_id: str):
    db: Session = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()

        if not job:
            return {"error": "Job not found"}

        return {
            "job_id": job.id,
            "status": job.status,
        }
    finally:
        db.close()
