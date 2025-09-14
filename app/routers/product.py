from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db


router = APIRouter()
@router.get("/products/")
async def get_products(
        db: AsyncSession = Depends(get_db)
):
    product_service = ProductServices(db)
    return await product_service.get_all_products() 