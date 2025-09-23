
import enum
from sqlalchemy import UUID, Boolean, DateTime, Enum, Text, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid

class OrderLine(Base):
    __tablename__ = "order_lines"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="order_lines")

    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    
    product = relationship("Product", back_populates="order_lines")
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False)
