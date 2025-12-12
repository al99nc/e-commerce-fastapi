from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.seller import ProductData, SellerRead
from app.services.cart import CartServices
from app.services.product import ProductServices
from app.services.seller import SellerServices
from uuid import UUID


router = APIRouter()
@router.get("/cart", response_model=list[ProductData])
async def get_cart(
        user: SellerRead,
        db: AsyncSession = Depends(get_db)
    ):
        cart_services = CartServices(db)
        return await cart_services.get_cart(user)
@router.post("/add-to-cart/{product_id}")
async def add_to_cart(
        user: SellerRead,
        quantity: int,
        product_id: UUID,
        db: AsyncSession = Depends(get_db)
    ):
        cart_services = CartServices(db)
        return await cart_services.add_to_cart(user, product_id, quantity)