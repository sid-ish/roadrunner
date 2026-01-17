from pydantic import BaseModel

class GeoPoint(BaseModel):
    lat: float | None = None
    lon: float | None = None
