from fastapi import FastAPI
import app.models  # Ensure models are imported for SQLAlchemy to register them
from app.routers import user
from app.routers import sell

app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(sell.router, prefix="/api", tags=["Seller"])