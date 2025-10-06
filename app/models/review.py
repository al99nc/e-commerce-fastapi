# review model
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID  # ✅ Make sure this is here
from sqlalchemy.sql import func
import uuid
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.user import User
class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship(User, back_populates="reviews")
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="reviews")
    rating = Column(String, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(String, nullable=False)
