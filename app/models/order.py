
import enum
from sqlalchemy import UUID, Boolean, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid

class Order(Base):
    __tablename__ = "orders"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="orders")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
    order_lines = relationship("OrderLine", back_populates="order")