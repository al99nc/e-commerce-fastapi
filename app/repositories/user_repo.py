from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models.user import User
from sqlalchemy.orm import selectinload

class UserRepository:
    def __init__(self, db = AsyncSession):
         self.db = db


    async def fetch_by_id(self, id = UUID) -> Optional[User]:
         statement = select(User).where(User.id == id)
         result = await self.db.execute(statement)
         return result.scalar_one_or_none()
