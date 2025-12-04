from fastapi import APIRouter, Depends
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.seller import ProductData, SellerRead
from app.services.cart import CartServices
from app.services.product import ProductServices
from app.services.seller import SellerServices


router = APIRouter()
@router.post("/add-to-cart")
async def add_to_cart(
        user: SellerRead,
        product_data: ProductData,
        db: AsyncSession = Depends(get_db)
    ):
        cart_services = CartServices(db)
        return await cart_services.add_to_cart(user, product_data
)