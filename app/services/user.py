from typing import Optional, List
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate


    
class UserServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository


    async def create(self, user: UserCreate):
        self.repository.create(self.db, user)
        user = await self.user_repository.fetch_by_id(user.user_id)
