from pydantic import BaseModel
from typing import List

class Detection(BaseModel):
    timestamp: float
    defect_type: str
    bbox: List[int]
    severity: float
