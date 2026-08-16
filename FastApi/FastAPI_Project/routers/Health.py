from datetime import datetime,timezone
from fastapi import APIRouter,Depends
from Dependencies import Settings,get_settings

router = APIRouter(prefix="/health",tags=["health"])

@router.get("")
def health_check(settings:Settings=Depends(get_settings)):
    """ 
    Deliberately simple right now - no DB/Redis to check yet. 
    This gets meaningfully expanded in Days 88-96 to also verify 
    DB connectivity, Redis connectivity, and model reachability.
    """
    return {
        "status":"ok",
        "timestamp":datetime.now(timezone.utc).isoformat(),
        "api_version": settings.api_version,
    }
