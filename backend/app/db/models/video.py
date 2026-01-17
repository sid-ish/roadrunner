from sqlalchemy import Column, String
from app.db.base import Base

class Video(Base):
    __tablename__ = "videos"
    id = Column(String, primary_key=True)
    source = Column(String)
