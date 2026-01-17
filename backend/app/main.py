from fastapi import FastAPI
from app.core.auth_middleware import auth_middleware
from app.core.cors import setup_cors
from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine

# 1️⃣ Create app FIRST
app = FastAPI(title="Roadrunner API", version="1.0")

# 2️⃣ Register middleware AFTER app exists
app.middleware("http")(auth_middleware)

# 3️⃣ Setup CORS
setup_cors(app)

# 4️⃣ Include routes
app.include_router(api_router)

# 5️⃣ Startup event for DB init (ONLY place)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# 6️⃣ Root health check
@app.get("/")
def root():
    return {"status": "Roadrunner backend running"}
