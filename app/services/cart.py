from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.product_repo import ProductRepository
from app.repositories.seller_repo import SellerRepository
from app.schemas.seller import ProductData, SellerDash, SellerRead, BecomeSellerRead
from urllib.parse import quote
from app.repositories.cart_repo import CartRepository
from app.schemas.seller import SellerRead
from app.repositories.seller_repo import get_by_id
class CartServices:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = CartRepository(self.db)
        self.seller_repository = SellerRepository(self.db)
    async def add_to_cart(self, user: SellerRead, product_id: UUID, quantity: int) -> dict:
        # Logic to add a product to the cart for the user
        product = await self.repository.add_to_cart(user, product_id, quantity)
        return product
    async def get_cart(self, user: SellerRead) -> list[ProductData]:
        user = await self.seller_repository.get_by_id(user.id)
        cart = await self.repository.get_cart(user)
        return cart