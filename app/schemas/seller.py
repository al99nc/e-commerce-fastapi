# schemas/seller.py
from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional
from datetime import datetime
from app.schemas.base import BaseSchema, BaseSchemaConfig
from pydantic_extra_types.phone_numbers import PhoneNumber

class SellerRead(BaseModel):
    id: UUID
    role: str 
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "7e2d5402-f408-4ac9-b9dc-f0413346a76b",  # UUID must be quoted
                "role": "seller"
            }
        }
    
class BecomeSellerRead(SellerRead):
    business_name: str
    business_type: str
    tax_id: str
    business_address: str
    business_phone: PhoneNumber
    business_email: EmailStr
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "7e2d5402-f408-4ac9-b9dc-f0413346a76b",  # UUID must be quoted
                "role": "seller",
                "business_name": "My Business",
                "business_type": "Retail",
                "tax_id": "123456789",
                "business_address": "123 Main St",
                "business_phone": "+9647711467565",
                "business_email": "seller@example.com"
            }
        }