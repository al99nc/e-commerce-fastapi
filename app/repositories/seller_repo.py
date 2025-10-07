from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models import user
from app.models.user import User

from sqlmodel import select

class SellerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, seller_id: int) -> Optional[User]:
        """Find a seller by its ID"""
        result = await self.db.execute(
            select(User).where(User.id == seller_id, User.role == 'SELLER')
        )
        return result.scalar_one_or_none()