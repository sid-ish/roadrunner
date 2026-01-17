from sqlalchemy import Column, String, Float
from app.db.base import Base

class Detection(Base):
    __tablename__ = "detections"
    id = Column(String, primary_key=True)
    defect_type = Column(String)
    severity = Column(Float)
