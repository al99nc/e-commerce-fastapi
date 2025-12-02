   
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.product_repo import ProductRepository
from app.repositories.seller_repo import SellerRepository
from app.schemas.seller import ProductData, SellerDash, SellerRead, BecomeSellerRead
from urllib.parse import quote
from app.repositories.seller_repo import SellerRepository
class ProductServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = ProductRepository(self.db)
        self.seller_repository = SellerRepository(self.db)
   
    async def create_product(self, user: SellerRead, product_data: ProductData) -> dict:
        seller = await self.seller_repository.get_by_id(user.id)
        if not seller:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Seller with id {user.id} not found"
            )
        # Logic to create a product for the seller
        product = await self.repository.create_product(seller, product_data)
        return product
    async def update_product(self, user: SellerRead, productId: UUID, product_data: ProductData) -> dict:
        seller = await self.seller_repository.get_by_id(user.id)
        if not seller:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Seller with id {user.id} not found"
            )
        # Logic to update a product for the seller
        product = await self.repository.update_product(seller, productId, product_data)
        return product
    
    async def delete_product(self, user: SellerRead, product_id: UUID) -> dict:
        seller = await self.seller_repository.get_by_id(user.id)
        if not seller:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Seller with id {user.id} not found"
            )
        # Logic to delete a product for the seller
        product = await self.repository.delete_product(seller, product_id)
        return product  