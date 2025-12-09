from app.routers import home
from fastapi import FastAPI
import app.models  # Ensure models are imported for SQLAlchemy to register them
from app.routers import cart, product
from app.routers import user
from app.routers import sell
import os
print("=" * 50)
print("ENVIRONMENT VARIABLES:")
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
print(f"PORT: {os.getenv('PORT')}")
print("=" * 50)
# all of this work is to just make these routers appear in the docs(swagger ui)
app = FastAPI()
app.include_router(user.router, tags=["Users"])
app.include_router(sell.router, tags=["Seller"])
app.include_router(product.router, tags=["Products"])
app.include_router(cart.router, tags=["Cart"])
app.include_router(home.router, tags=["Home"])