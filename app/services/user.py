# services/user.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserResponse
from passlib.context import CryptContext

# For password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(self.db)
    
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    async def create(self, user_data: UserCreate) -> UserResponse:
        # Check if user already exists
        existing_user = await self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user_data.email} already exists"
            )
        
        # Create user object with proper field mapping
        user_dict = user_data.model_dump()
        user_dict['name'] = user_dict.pop('full_name')  # Map full_name to name
        user_dict['password'] = self.hash_password(user_dict['password'])  # Hash password
        
        user = User(**user_dict)
        
        # Save to database
        created_user = await self.repository.create(user)
        
        # Return the created user
        return UserResponse.model_validate(created_user)