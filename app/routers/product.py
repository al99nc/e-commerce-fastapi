from fastapi import APIRouter, Depends
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.seller import ProductData, SellerRead
from app.services.product import ProductServices
from app.services.seller import SellerServices


router = APIRouter()
@router.post("/create-product")
async def create_product(
        user: SellerRead,
        product_data: ProductData,
        db: AsyncSession = Depends(get_db)
):
        product_services = ProductServices(db)
        return await product_services.create_product(user, product_data)

@router.patch("/update-product/{productId}")
async def update_product(
        user: SellerRead,
        productId: str,  # <-- typed path param accessible as `productId`
        product_data: ProductData,
        db: AsyncSession = Depends(get_db)
):
        product_services = ProductServices(db)
        # pass the id to your service method
        return await product_services.update_product(user, productId, product_data)

@router.delete("/products/{product_id}")
async def delete_product(
        product_id: str,
        user: SellerRead,
        db: AsyncSession = Depends(get_db)
):
        # Implement delete product logic here
        product_services = ProductServices(db)
        await product_services.delete_product(user, product_id)
        return {"message": f"Product with id {product_id} deleted successfully"}