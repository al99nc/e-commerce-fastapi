from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models import user
from app.models.cart import Cart
from app.models.cartItem import CartItem
from app.models.order import Order
from app.models.orderLine import OrderLine
from app.models.product import Product
from app.models.sellerProfile import SellerProfile, SellerStatus
from app.models.user import UserRole
from app.models.user import User
from app.schemas.base import BaseSchema
from app.schemas.seller import ProductData, SellerRead, SellerRead
class HomeRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def get_home_products(self) -> List[ProductData]:
        """Fetch products for home page display"""
        result = await self.db.execute(
            select(Product).where(Product.status == "active")
        )
        products = result.scalars().all()
        return [ProductData.from_orm(product) for product in products]