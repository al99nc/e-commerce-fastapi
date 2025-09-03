from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models import user
from app.models.user import User

from sqlmodel import select


class UserRepository:
    def __init__(self, db = AsyncSession):
        self.db = db

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_email(self, email: str):
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    async def get_by_username(self, username: str):
        result = await self.db.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()
    
    async def create(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_by_id(self, profile_id: int) -> Optional[User]:
        """Find a profile by its ID"""
        result = await self.db.execute(
            select(User).where(User.id == profile_id)
        )
        return result.scalar_one_or_none()

    async def get_by_user_id(self, user_id: int) -> Optional[User]:
        """Find a profile by the user's ID"""
        result = await self.db.execute(
            select(User).where(User.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> List[User]:
        """Get all profiles"""
        result = await self.db.execute(select(User))
        return result.scalars().all()

    async def update(self, profile: User) -> User:
        """Update an existing profile"""
        await self.db.commit()
        await self.db.refresh(profile)
        return profile

    async def delete(self, profile: User):
        """Delete a profile"""
        await self.db.delete(profile)
        await self.db.commit()