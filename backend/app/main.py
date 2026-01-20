from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.core.auth_middleware import auth_middleware
from app.core.cors import setup_cors
from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Roadrunner API", version="1.0")

# 🔐 Auth middleware
app.middleware("http")(auth_middleware)

# 🌐 CORS
setup_cors(app)

# 🚏 Routes
app.include_router(api_router)

# 🗄️ DB init
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# 🏠 Root
@app.get("/")
def root():
    return {"status": "Roadrunner backend running"}

# 🔥 THIS IS THE IMPORTANT PART
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Roadrunner API",
        version="1.0",
        description="Roadrunner backend",
        routes=app.routes,
    )

    # ✅ Define security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "RoadrunnerToken": {
            "type": "apiKey",
            "in": "header",
            "name": "X-ROADDRUNNER-TOKEN",
        }
    }

    # ✅ Apply globally
    openapi_schema["security"] = [
        {"RoadrunnerToken": []}
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
