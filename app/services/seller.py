# services/user.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.seller_repo import SellerRepository
from app.repositories.user_repo import UserRepository
from app.schemas.seller import SellerRead
from app.schemas.user import UserCreate, UserRead, UserResponse, UserTokenRead
from passlib.context import CryptContext
from typing import Optional
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
        return SellerRead.from_orm(seller)