# user.py
from datetime import datetime
import enum
import uuid
from sqlalchemy import UUID, Boolean, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.database import Base

class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"
    SELLER = "SELLER"

class Locale(enum.Enum):
    en = "en"
    ar = "ar"
class User(Base):
    __tablename__ = "users"
    
    # Primary fields
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Basic user info
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    # Additional fields from your existing database
    phone_number = Column(String, nullable=True)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)
    avatar = Column(String, nullable=True)
    locale = Column(Enum(Locale), default=Locale.en)
    last_login = Column(DateTime(timezone=True), nullable=True)
    email_validated = Column(Boolean, nullable=False, default=False)
    phone_validated = Column(Boolean, nullable=False, default=False)
    bio = Column(String, nullable=True)
    company = Column(String, nullable=True)
    # Fix the relationship (remove this for now until you create SellerProfile model)
    # seller_profile = relationship("SellerProfile", uselist=False, back_populates="user")