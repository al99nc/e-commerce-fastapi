# user.py
from typing import Optional
from pydantic import EmailStr, Field
from .base import BaseSchema
# ... your user schemas here


class UserBase(BaseSchema):
    full_name : str

class UserCreate(UserBase):
    email : EmailStr 
    phone_number: Optional[PhoneNumber] = None
    password: str = Field(min_length=8, max_length=100)


class UserResponse(BaseSchema):  # Inherits id, created_at, updated_at
    email: str
    name: str
    # Don't need to repeat id, created_at, updated_at!