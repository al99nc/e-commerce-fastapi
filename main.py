from fastapi import FastAPI
import app.models  # Ensure models are imported for SQLAlchemy to register them
from app.routers import product
from app.routers import user
from app.routers import sell
# all of this work is to just make these routers appear in the docs(swagger ui)
app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(sell.router, prefix="/api", tags=["Seller"])
app.include_router(product.router, prefix="/products", tags=["Products"])