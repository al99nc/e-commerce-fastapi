# user.py
from typing import Optional
from uuid import UUID
from pydantic import EmailStr, Field
from .base import BaseSchema
# ... your user schemas here


class UserBase(BaseSchema):
    full_name : str
    #id + creadted at + updated at

class UserCreate(UserBase):
    #full_name from userbase 
    email : EmailStr 
    phone_number: Optional[str] = None
    password: str = Field(min_length=8, max_length=100)


class UserResponse(BaseSchema):  # Inherits id, created_at, updated_at
    email: str
    name: str
    # Don't need to repeat id, created_at, updated_at!
    
    
    class UserRead(BaseSchema):
        user_id: UUID
