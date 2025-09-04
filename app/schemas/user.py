# schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID
from app.schemas.base import BaseSchema, BaseSchemaConfig

from pydantic_extra_types.phone_numbers import PhoneNumber
PhoneNumber.phone_format = 'E164'

# For creating a new user (what the client sends)
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: Optional[PhoneNumber] = None
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "phone_number": "+1234567890",
                "password": "securepassword123"
            }
        }

# For returning user data (what the API responds with)
class UserResponse(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    email: str
    name: str  # This should match your database field
    phone_number: Optional[str] = None
    
    class Config:
        from_attributes = True  # For SQLAlchemy compatibility
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "created_at": "2025-09-01T14:36:48.900Z",
                "updated_at": "2025-09-01T14:36:48.900Z",
                "email": "john.doe@example.com",
                "name": "John Doe",
                "phone_number": "+1234567890"
            }
        }

# For updating user data (optional - if you need it later)
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "Jane Doe",
                "phone_number": "+0987654321"
            }
        }
        
        
class UserRead(BaseSchemaConfig):
   email: str
   password: str

   class Config:
        json_schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "password": "securepassword123"
            }
        }
        
class UserTokenRead(BaseSchemaConfig):
   email: str
   id: UUID
   role: str

   class Config:
        json_schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "role": "CUSTOMER"
            }
        }