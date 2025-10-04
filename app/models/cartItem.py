import uuid
from app.db.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, func
from sqlalchemy.dialects.postgresql import UUID     
from sqlalchemy.orm import relationship

# from app.models.cart import Cart
# from app.models.product import Product

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    cart_id = Column(UUID(as_uuid=True), ForeignKey("carts.id"), nullable=False)
    cart = relationship("Cart", backref="items", uselist=False)

    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)  # Assuming products are identified by UUID
    product = relationship("Product", backref="cart_items", uselist=False)

    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False)  # Price at the time of adding to cart