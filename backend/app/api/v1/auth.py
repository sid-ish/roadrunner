from fastapi import APIRouter
from app.utils.helpers import generate_token

router = APIRouter()

@router.get("/ping")
def ping():
    return {
        "token": generate_token()
    }
