from pydantic import BaseModel

class JobCreate(BaseModel):
    youtube_url: str
    mode: str = "recorded"

class JobResponse(BaseModel):
    job_id: str
    status: str
