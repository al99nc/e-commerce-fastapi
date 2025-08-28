from datetime import datetime
from pydantic import BaseModel

class BaseSchemaConfig(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class BaseSchema(BaseSchemaConfig):
    id: str
    created_at: datetime
    updated_at: datetime