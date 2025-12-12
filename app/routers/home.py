from fastapi import APIRouter

from app.services.home import HomeServices

router = APIRouter()
@router.get("/")
async def read_home():
    homeservices = HomeServices()
    return await homeservices.get_home_data()
    