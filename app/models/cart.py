# Cart model
from datetime import datetime
import enum
import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, Integer, String, Float, func
from sqlalchemy.orm import relationship
from sqlmodel import Enum
from app.db.database import Base
from app.models.user import User    


class Status(enum.Enum):
    active = "ACTIVE"
    ordered = "ORDERED"
    cancelled = "CANCELLED"

class Cart(Base):
    __tablename__ = "carts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_by = Column(ForeignKey("users.id", as_uuid=True), nullable=False)
    created = relationship(User, backref="carts", uselist=False)
    status = Column(Enum(Status), nullable=False, default=Status.active)  # e.g., active, ordered, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())