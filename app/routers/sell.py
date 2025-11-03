from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.seller import SellerRead, BecomeSellerRead
from app.services.seller import SellerServices

router = APIRouter()
@router.post("/sell/")# we don't use this "bec my front knows if the user is a seller or not using the token data" seller or customer
async def get_seller_profile(
        user: SellerRead,
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.get_seller_profile(user) 

@router.post("/become-seller/")
async def become_seller(
        user: BecomeSellerRead,#here we can use SellerCreate schema if we have additional fields for seller creation and do the necessary processing in the service layer i love this approach and U❤️❤️
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.become_seller(user)
@router.post("/seller/dashboard")
async def get_seller_dashboard(
        user: SellerRead,
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.get_seller_dashboard(user)
@router.get("/seller/create-product")
async def create_product(
        user: SellerRead,
        product_data: ProductData,
        db: AsyncSession = Depends(get_db)
):
        seller_service = SellerServices(db)
        return await seller_service.create_product(user, product_data)