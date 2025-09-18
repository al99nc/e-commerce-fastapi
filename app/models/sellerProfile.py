# app/models/sellerProfile.py
from datetime import datetime
import enum
import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, Enum, Text, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import relationship
from app.models.user import User
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import Base

class SellerStatus(enum.Enum):
  pending = "PENDING"  # Waiting for approval
  approved = "APPROVED"  # Can sell products
  suspended = "SUSPENDED"  # Temporarily blocked
  banned = "BANNED"  # Permanently blocked
class SellerProfile(Base):
    __tablename__ = "sellerProfile"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship(User, uselist=False, backref="seller_profile")
#
    business_name = Column(String, nullable=False)
    business_address = Column(String, nullable=True)
    business_type = Column(String, nullable=True)
    business_phone = Column(String, nullable=True)
    business_email = Column(String, nullable=True)
    tax_id = Column(String, nullable=True)

    bank_account_name = Column(String, nullable=True)
    bank_account_number = Column(String, nullable=True)
    bank_name = Column(String, nullable=True)
    
    status = Column(Enum(SellerStatus), default=SellerStatus.pending)
    commission_rate = Column(Float, nullable=True, default=0.5)  # Default commission rate
    
    rating = Column(Float, nullable=True, default=0.0)
    reviews_count = Column(Integer, nullable=True, default=0)
    
      # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    approved_at = Column(DateTime(timezone=True), nullable=True)
    
    total_sales = Column(Float, nullable=True, default=0.0)
    total_orders = Column(Integer, nullable=True, default=0)


