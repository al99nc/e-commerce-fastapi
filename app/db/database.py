import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Debug: Print what we got (remove this later)
print(f"DATABASE_URL from env: {DATABASE_URL}")

# Validate and convert
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")

# Convert postgresql:// to postgresql+asyncpg:// for async
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

print(f"Final DATABASE_URL: {DATABASE_URL}")

# Now create engine
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Dependency function to get database session
async def get_db():
    async with SessionLocal() as session:
        yield session

