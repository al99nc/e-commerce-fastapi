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
        """Add a new user to the database"""
        self.db.add(user)  # Stage it
        await self.db.commit()  # Save it
        await self.db.refresh(user)  # Get the updated version with ID
        return user

    async def get_by_id(self, user_id: int) -> Optional[User]:
        """Find a user by its ID"""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_user_id(self, user_id: int) -> Optional[User]:
        """Find a user by the user's ID"""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> List[User]:
        """Get all users"""
        result = await self.db.execute(select(User))
        return result.scalars().all()

    async def update(self, user: User) -> User:
        """Update an existing user"""
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete(self, profile: User):
        """Delete a profile"""
        await self.db.delete(profile)
        await self.db.commit()