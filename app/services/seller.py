# services/user.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.seller_repo import SellerRepository
from app.schemas.seller import SellerRead, BecomeSellerRead
from urllib.parse import quote
class SellerServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = SellerRepository(self.db)

    async def get_seller_profile(self, user: SellerRead) -> SellerRead:
        # Fetch seller profile from the database using the repository
        seller = await self.repository.get_by_id(user.id)
        if not seller:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Seller with id {user.id} not found"
            )
        return SellerRead(seller)
    async def become_seller(self, user: BecomeSellerRead) -> SellerRead:
        existing_user = await self.repository.get_by_id(user.id)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User is a seller with id {user.id} already exists"
            )
            
        seller = await self.repository.create_seller(user)
        updated_user = await self.repository.update_user_role(user.id)
        return SellerRead.from_orm(seller)  # Use from_orm instead of direct instantiation
