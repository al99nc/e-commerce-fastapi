# app/models/sellerProfile.py
from datetime import datetime
import enum
import uuid
from sqlalchemy import UUID, Boolean, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey, Mapped, func, relationship, mapped_column

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.database import Base

class SellerStatus(enum.Enum):
  pending = "PENDING"  # Waiting for approval
  approved = "APPROVED"  # Can sell products
  suspended = "SUSPENDED"  # Temporarily blocked
  banned = "BANNED"  # Permanently blocked
class SellerProfile(Base):
    __tablename__ = "sellerProfile"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), )
    
##  علاوي افتهم ال relationship هاي 
## موجودة بال هستري بب بريف 
#https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
#your litterly my hero best best in the market i love uuuuuuuu so so much❤️❤️❤️❤️❤️