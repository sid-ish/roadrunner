from app.db.base import Base
from app.db.session import engine

# 🔥 IMPORT ALL MODELS EXPLICITLY
from app.db.models.job import Job
from app.db.models.detection import Detection

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done")
