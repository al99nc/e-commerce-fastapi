from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.product_repo import ProductRepository
from app.repositories.seller_repo import SellerRepository
from app.schemas.seller import ProductData, SellerDash, SellerRead, BecomeSellerRead
from urllib.parse import quote
from app.repositories.seller_repo import SellerRepository
from app.repositories.home_repo import HomeRepository

class HomeServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = HomeRepository(self.db)
    async def get_home_data(self) -> dict:
        products = await self.repository.get_home_products()
        return {"products": products}