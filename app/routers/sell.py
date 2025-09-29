from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.seller import SellerRead
from app.services.seller import SellerServices

router = APIRouter()
@router.get("/sell/")
async def get_seller_profile(
        user: SellerRead,
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.get_seller_profile(user) 