from fastapi import APIRouter

router = APIRouter()
@router.get("/")
async def read_home():
    return {"message": "hi there, you just hit the frist deployed project created by Ali Hamed!"}