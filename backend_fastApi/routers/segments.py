from fastapi import APIRouter
from services.segment_service import get_segments

router = APIRouter()


@router.get("/segments")
def lire_segments():
    return get_segments()