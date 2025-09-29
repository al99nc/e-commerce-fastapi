# schemas/seller.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID
from app.schemas.base import BaseSchema, BaseSchemaConfig

from pydantic_extra_types.phone_numbers import PhoneNumber
PhoneNumber.phone_format = 'E164'

class SellerRead(BaseSchemaConfig):
    id = UUID
    role = "seller"
    example = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "role": "seller"
    } 