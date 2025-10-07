from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.seller import SellerRead
from app.services.seller import SellerServices

router = APIRouter()
@router.post("/sell/")
async def get_seller_profile(
        user: SellerRead,
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.get_seller_profile(user) 

@router.post("/become-seller/")
async def become_seller(
        user: SellerRead,#here we can use SellerCreate schema if we have additional fields for seller creation and do the necessary processing in the service layer i love this approach and U❤️❤️
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.get_seller_profile(user)