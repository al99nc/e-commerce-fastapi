# app/models/sellerProfile.py
from datetime import datetime
import enum
import uuid
from sqlalchemy import UUID, Boolean, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey, Mapped, func, relationship, mapped_column
from app.models.user import User
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
    user_id = Column(ForeignKey("users.id", as_uuid=True), nullable=False)
    user = relationship(User, uselist=False, backref="seller_profile")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


#https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html