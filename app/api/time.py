from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/current-time")
async def get_current_time():
    current_time = datetime.now().isoformat()
    return {"current_time": current_time, "message": "Que onda perros!"}