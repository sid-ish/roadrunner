from fastapi import APIRouter
from app.api.v1 import jobs, videos, detections, health, auth, map_routes

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(videos.router, prefix="/videos", tags=["videos"])
api_router.include_router(detections.router, prefix="/detections", tags=["detections"])
api_router.include_router(map_routes.router, prefix="/map", tags=["map"])
