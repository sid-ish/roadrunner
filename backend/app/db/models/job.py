from sqlalchemy import Column, String
from app.db.base import Base
import uuid

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    status = Column(String, default="queued")
    youtube_url = Column(String, nullable=False)
