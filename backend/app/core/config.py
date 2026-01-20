# app/core/config.py

PROJECT_NAME = "Roadrunner"

# Auth
AUTH_SECRET = "roadrunner-secret-key"
TOKEN_TTL_SECONDS = 300  # 5 minutes

# Redis
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_JOB_QUEUE = "roadrunner:jobs"
