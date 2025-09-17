from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db


router = APIRouter()
@router.get("/sell/")
async def get_seller_profile(
        user: seller_user
        db: AsyncSession = Depends(get_db)
):
    seller_service = SellerServices(db)
    return await seller_service.get_seller_profile(user) 