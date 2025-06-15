from fastapi import APIRouter

router = APIRouter(
    prefix="/game",
    tags=["game"]
)

@router.get("/ping")
async def ping():
    return {"message": "pong"}