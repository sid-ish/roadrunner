from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.helpers import verify_token

# Public / unauthenticated paths
EXCLUDED_PATHS = [
    "/",
    "/favicon.ico",
    "/api/v1/health",
    "/api/v1/auth/ping",
    "/docs",
    "/openapi.json",
    "/redoc"
]


async def auth_middleware(request: Request, call_next):
    path = request.url.path

    # Allow public routes
    if path in EXCLUDED_PATHS:
        return await call_next(request)

    # Allow static assets used by docs
    if path.startswith("/docs") or path.startswith("/openapi"):
        return await call_next(request)

    # Custom token header
    token = request.headers.get("X-ROADDRUNNER-TOKEN")

    if not token or not verify_token(token):
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized"}
        )

    return await call_next(request)
