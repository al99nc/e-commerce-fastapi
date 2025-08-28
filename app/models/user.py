from datetime import datetime
import enum
import uuid
from sqlalchemy import UUID, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey
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
    
    # Fix the UUID primary key - try this approach:
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    # OR if you want proper UUID type:
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    slug = Column(String, unique=True)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)
    name = Column(String)
    avatar = Column(Text)
    locale = Column(Enum(Locale), default=Locale.en)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    email_validated = Column(DateTime, nullable=True)
    phone_validated = Column(DateTime, nullable=True)
    bio = Column(String, nullable=True)
    company = Column(String, nullable=True)
    
    # Fix the relationship (remove this for now until you create SellerProfile model)
    # seller_profile = relationship("SellerProfile", uselist=False, back_populates="user")