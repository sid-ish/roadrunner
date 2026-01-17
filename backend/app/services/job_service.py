from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.job import Job
from app.schemas.job import JobCreate

def create_job(payload: JobCreate):
    db: Session = SessionLocal()
    try:
        job = Job(
            youtube_url=payload.youtube_url,
            status="queued"
        )
        db.add(job)
        db.commit()
        db.refresh(job)

        return {
            "job_id": job.id,
            "status": job.status
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
            "status": job.status
        }
    finally:
        db.close()
