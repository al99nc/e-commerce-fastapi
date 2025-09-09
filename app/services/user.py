# services/user.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserRead, UserResponse, UserTokenRead
from passlib.context import CryptContext
from app.authentication.auth_configuration import get_password_hash, verify_password, create_tokens
from typing import Optional

class UserServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(self.db)
    
    def hash_password(self, password: str) -> str:
        return get_password_hash(password)

    async def create(self, user: UserCreate) -> UserResponse:
        # Check if user already exists
        existing_user = await self.repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user.email} already exists"
            )

        # Create user object with proper field mapping
        user_dict = user.model_dump() # converts Pydantic model to dictionary
        user_dict['name'] = user_dict.pop('full_name')  # Map full_name to name
        user_dict['password'] = self.hash_password(user_dict['password'])  # Hash password
        
        user = User(**user_dict)
        
        # Save to database
        created_user = await self.repository.create(user)
        
        # Generate tokens using the created user's data
        tokens = create_tokens(
            user_id=str(created_user.id),
            email=created_user.email,
            role=created_user.role.value  # Convert enum to string
        )
        
        # Update user with tokens
        created_user.refresh_token = tokens["refresh_token"]
        
        # Save updated user with tokens
        updated_user = await self.repository.update(created_user)
        
        # Return the created user with tokens
        return UserResponse(
            id=updated_user.id,
            email=updated_user.email,
            name=updated_user.name,
            role=updated_user.role,
            access_token=tokens["access_token"],
            created_at=updated_user.created_at,  # Add created_at
            updated_at=updated_user.updated_at   # Add updated_at
        )


    async def login(self, user: UserRead) -> UserResponse:
        # Check if user exists
        existing_user = await self.repository.get_by_email(user.email)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Verify password
        if not verify_password(user.password, existing_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        # Return the user
        return UserResponse.model_validate(existing_user)


    async def get_current_user(self, user: UserTokenRead) -> UserResponse:
        existing_user = await self.repository.get_by_email(user.email)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user.email} already exists"
            )
        return UserResponse.model_validate(existing_user)
