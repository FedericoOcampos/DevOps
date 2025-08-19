from fastapi import APIRouter
from datetime import datetime

from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.get("/current-time")
async def get_current_time():
    now = datetime.now()
    current_time = now.isoformat()
    body = f"Que onda perros!\n{current_time}"
    return PlainTextResponse(content=body)