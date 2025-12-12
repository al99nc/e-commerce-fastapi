from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.home import HomeServices

router = APIRouter()

@router.get("/")
async def read_home(db: AsyncSession = Depends(get_db)):
    homeservices = HomeServices(db)  # ✅ Pass db session
    return await homeservices.get_home_data()