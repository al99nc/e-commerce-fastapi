
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models import user
from app.models.order import Order
from app.models.orderLine import OrderLine
from app.models.product import Product
from app.models.sellerProfile import SellerProfile, SellerStatus
from app.models.user import UserRole
from app.models.user import User
from app.schemas.seller import ProductData

class ProductRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
    async def create_product(self, seller: User, product_data: ProductData) -> dict:
        # Placeholder logic to create a product for the seller
        new_product = Product(
            category_id=product_data.categoryId,
            seller_id=seller.id,
            title=product_data.title,
            description=product_data.description,
            price=product_data.price,
            stock_quantity=product_data.stock,
            discount_type=product_data.discount_type,
            discount_value=product_data.discount_value,
            tags=product_data.tags,
            picture=product_data.picture,
            summary=product_data.summary
        )
        self.db.add(new_product)
        await self.db.commit()
        await self.db.refresh(new_product)
        return new_product
    async def update_product(self, seller: User, productId: UUID, updated_product_data: ProductData) -> dict:
        result = await self.db.execute(
            select(Product).where(
                Product.id == productId,
                Product.seller_id == seller.id
            )
        )
        product = result.scalar_one_or_none()

        if not product:
            raise ValueError(f"Product with id {productId} not found for seller {seller.id}")
        
        product.title = updated_product_data.title
        product.category_id = updated_product_data.categoryId
        product.description = updated_product_data.description
        product.price = updated_product_data.price
        product.stock_quantity = updated_product_data.stock 
        product.discount_type = updated_product_data.discount_type
        product.discount_value = updated_product_data.discount_value
        product.tags = updated_product_data.tags
        product.picture = updated_product_data.picture
        product.summary = updated_product_data.summary

        

        await self.db.commit()
        await self.db.refresh(product)
        return product
    
    async def delete_product(self, seller: User, product_id: UUID) -> dict:
        result = await self.db.execute(
            select(Product).where(
                Product.id == product_id,
                Product.seller_id == seller.id
            )
        )
        product = result.scalar_one_or_none()

        if not product:
            raise ValueError(f"Product with id {product_id} not found for seller {seller.id}")
        
        await self.db.delete(product)
        await self.db.commit()
        return {"message": f"Product with id {product_id} deleted successfully"}
    async def get_product_info_by_id(self, product_id: UUID) -> Optional[Product]:
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()