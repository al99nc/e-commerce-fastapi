
import enum
from sqlalchemy import UUID, Boolean, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlmodel import ARRAY
from app.db.database import Base
import uuid

class ProductStatus(enum.Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"
    out_of_stock = "OUT_OF_STOCK"
    discontinued = "DISCONTINUED"

class DiscountType(enum.Enum):
    none = "NONE"
    percent = "PERCENT"
    amount = "AMOUNT"

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")
    
    seller_id = Column(UUID(as_uuid=True), ForeignKey("seller_profiles.id"), nullable=False)
    seller = relationship("SellerProfile", back_populates="products")

    title = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    summary = Column(String, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    discount_value = Column(Float, nullable=True, default=0.0)
    discount_type = Column(Enum(DiscountType), nullable=True)
    tags = Column(ARRAY(String), nullable=False, default=list)
    

    status = Column(Enum(ProductStatus), nullable=False, default=ProductStatus.active)
    stock_quantity = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    order_lines = relationship("OrderLine", back_populates="product")