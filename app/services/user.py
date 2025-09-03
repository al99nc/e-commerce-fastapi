# services/user.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserRead, UserResponse
from passlib.context import CryptContext

# For password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserServices:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(self.db)
    
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
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
        
        # Return the created user
        return UserResponse.model_validate(created_user)
    
    
    async def login(self, user: UserRead) -> UserResponse:
        # Check if user exists
        existing_user = await self.repository.get_by_email(user.email)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Verify password
        if not pwd_context.verify(user.password, existing_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        # Return the user
        return UserResponse.model_validate(existing_user)