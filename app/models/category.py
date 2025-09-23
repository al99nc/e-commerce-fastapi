from sqlalchemy import Column, String, DateTime, ForeignKey, Index, ARRAY, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    
    # Primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Self-referencing foreign key
    parent_category = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=True)
    
    # Basic fields
    slug = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)  # Changed to Text to match Prisma String
    
    # Tags as array (PostgreSQL specific) or JSON for other databases
    tags = Column(ARRAY(String), nullable=False, default=list)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Self-referencing relationships
    parent = relationship("Category", remote_side=[id], back_populates="children")
    children = relationship("Category", back_populates="parent")
    products_id = Column(ARRAY(UUID(as_uuid=True)), nullable=False, default=list)    
    products = relationship("Product", back_populates="category")


