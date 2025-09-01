from typing import Optional, List
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate
from app.schemas.base import BaseSchema


    
class UserServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository


    async def create(self, user: UserCreate):
        self.repository.create(self.db, user)
  # Check if user exists
    async def create(self, user_data: UserCreate) -> BaseSchema:
        # Check if user already exists (by email or username)
        existing_user = await self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user_data.email} already exists"
            )
        
        # Optional: Check username too if you have one
        if hasattr(user_data, 'username'):
            existing_username = await self.repository.get_by_username(user_data.username)
            if existing_username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Username {user_data.username} already taken"
                )
        
        # Create the user object
        user = User(**user_data.model_dump())
        
        # Save to database
        created_user = await self.repository.create(user)
        
        # Return the created user (converted to response model)
        return BaseSchema.model_validate(created_user)