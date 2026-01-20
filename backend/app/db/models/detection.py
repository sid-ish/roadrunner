from sqlalchemy import Column, String, Integer, Float, ForeignKey
from app.db.base import Base
import uuid

class Detection(Base):
    __tablename__ = "detections"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    job_id = Column(String, ForeignKey("jobs.id"), index=True)
    track_id = Column(Integer, nullable=True)
    frame_index = Column(Integer)
    label = Column(String)
    confidence = Column(Float)

    # bounding box (normalized 0–1)
    x1 = Column(Float)
    y1 = Column(Float)
    x2 = Column(Float)
    y2 = Column(Float)
