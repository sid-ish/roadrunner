from fastapi import APIRouter

router = APIRouter()

@router.get("/{job_id}")
def get_map_data(job_id: str):
    return []
