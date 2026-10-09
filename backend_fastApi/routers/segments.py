from fastapi import APIRouter, HTTPException

from services.segment_service import get_segments


router = APIRouter()


@router.get("/segments")
def lire_segments(vehicle: str = "pl"):

    try:
        return get_segments(vehicle)

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Le véhicule doit être pl, vul ou vc"
        )