# db.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use asyncpg driver for PostgreSQL
DATABASE_URL = "postgresql+asyncpg://postgres:aliila2009@localhost:3000/ecommerce-py"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)
Base = declarative_base()

# Dependency function to get database session
async def get_db():
    async with SessionLocal() as session:
        yield session