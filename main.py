from fastapi import FastAPI
import app.models  # Ensure models are imported for SQLAlchemy to register them
from app.routers import user

app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["users"])