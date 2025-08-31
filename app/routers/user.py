# routers/user.py
from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
async def get_all_users():
    # For now, just return fake data to test
    return [
        {
            "id": "1",
            "email": "test@test.com", 
            "name": "Test User",
            "created_at": "2024-01-01T00:00:00",
            "updated_at": "2024-01-01T00:00:00"
        }
    ]

@router.post("/signup/", response_model=UserResponse)
async def create_user(user: UserCreate):
    
    return 