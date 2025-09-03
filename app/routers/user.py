

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserResponse , UserRead
from app.services.user import UserServices
from app.db.database import get_db

router = APIRouter()

@router.post("/signup/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserServices(db)
    return await user_service.create(user)



@router.post("/login/", response_model=UserResponse)
async def login_user(
    user: UserRead,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserServices(db)
    return await user_service.login(user)

