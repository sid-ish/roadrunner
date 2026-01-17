from pydantic import BaseModel

class Video(BaseModel):
    id: str
    source: str
