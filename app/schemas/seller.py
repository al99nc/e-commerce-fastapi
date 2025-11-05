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
    

class SellerDash(BaseModel):
    name: str
    email: EmailStr 
    
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
        
class ProductData(BaseModel):
    sellerId: UUID
    categoryId: UUID
    title: str
    description: Optional[str]
    price: Optional[float]
    discount_type: Optional[float]
    discount_value: Optional[float]
    stock: Optional[int]
    summary: Optional[str]
    tags: Optional[list[str]]
    picture: Optional[str]
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Sample Product",
                "description": "This is a sample product.",
                "price": 19.99,
                "discount_type": "percentage",
                "discount_value": 0.1,
                "stock": 100,
                "summary": "A brief summary of the product.",
                "tags": ["sample", "product", "ecommerce"],
                "picture": "C:/Users/gt store/Desktop/eecommerc/e-commerce/server/src/uploads/1753029300314.png"
            }
        }   