from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.product_repo import ProductRepository
from app.repositories.seller_repo import SellerRepository
from app.schemas.seller import ProductData, SellerDash, SellerRead, BecomeSellerRead
from urllib.parse import quote
from app.repositories.cart_repo import CartRepository

class CartServices:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = CartRepository(self.db)
    async def add_to_cart(self, user: SellerRead, product_id: UUID, quantity: int) -> dict:
        # Logic to add a product to the cart for the user
        product = await self.repository.add_to_cart(user, product_id, quantity)
        return product