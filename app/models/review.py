# review model
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.user import User
class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    user = relationship(User, )
    
    product_id = Column(String, nullable=True)