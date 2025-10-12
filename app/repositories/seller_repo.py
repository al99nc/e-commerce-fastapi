from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models import user
from app.models.sellerProfile import SellerProfile, SellerStatus
from app.models.user import UserRole
from app.models.user import User

from sqlmodel import select

class SellerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, seller_id: UUID) -> Optional[User]:
        """Find a seller by its ID"""
        result = await self.db.execute(
            select(User).where(User.id == seller_id, User.role == 'SELLER')
        )
        return result.scalar_one_or_none()
    async def create_seller(self, user) -> SellerProfile:
        """Create a new seller"""
        # First check if user exists
        existing_user = await self.db.execute(
            select(User).where(User.id == user.id)
        )
        user_exists = existing_user.scalar_one_or_none()
        
        if not user_exists:
            raise ValueError(f"User with id {user.id} does not exist")

        new_seller = SellerProfile(
            id=user.id,
            user_id=user.id,
            business_name=user.business_name,
            business_type=user.business_type,
            tax_id=user.tax_id,
            business_address=user.business_address,
            business_phone=str(user.business_phone) if user.business_phone else None,
            business_email=user.business_email,
            commission_rate=0.05,  # 5% default
            status=SellerStatus.pending,  # Needs approval
            total_sales=0,
            total_orders=0,
            rating=0.0,
            reviews_count=0
        )
        self.db.add(new_seller)
        await self.db.commit()
        await self.db.refresh(new_seller)
        return new_seller
    async def update_user_role(self, user_id: UUID) -> Optional[User]:
        """Update the role of a user"""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        if user:
            user.role = UserRole.SELLER
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
        return user