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

from sqlmodel import select

class SellerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, seller_id: UUID) -> Optional[User]:
        """Find a seller by its ID"""
        result = await self.db.execute(
            select(User).where(User.id == seller_id, User.role == 'SELLER')
        )
        return result.scalar_one_or_none()
    async def create_seller(self, user) -> SellerProfile:
        """Create a new seller"""
        # First check if user exists
        existing_user = await self.db.execute(
            select(User).where(User.id == user.id)
        )
        user_exists = existing_user.scalar_one_or_none()
        
        if not user_exists:
            raise ValueError(f"User with id {user.id} does not exist")

        new_seller = SellerProfile(
            id=user.id,
            user_id=user.id,
            business_name=user.business_name,
            business_type=user.business_type,
            tax_id=user.tax_id,
            business_address=user.business_address,
            business_phone=str(user.business_phone) if user.business_phone else None,
            business_email=user.business_email,
            commission_rate=0.05,  # 5% default
            status=SellerStatus.pending,  # Needs approval
            total_sales=0,
            total_orders=0,
            rating=0.0,
            reviews_count=0
        )
        self.db.add(new_seller)
        await self.db.commit()
        await self.db.refresh(new_seller)
        return new_seller
    async def update_user_role(self, user_id: UUID) -> Optional[User]:
        """Update the role of a user"""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        if user:
            user.role = UserRole.SELLER
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
        return user
    async def get_total_products(self, user_id: UUID) -> int:
        # Placeholder logic to count products for the seller
        result = await self.db.execute(
            select(SellerProfile).where(SellerProfile.user_id == user_id)
        )
        
        products = await self.db.execute(
            select(func.count(Product.id)).where(Product.seller_id == result.scalar_one_or_none().id)
        )
        return products.scalar_one()
    async def get_total_sales(self, user_id: UUID) -> float:
        result = await self.db.execute(
            select(SellerProfile.total_sales).where(SellerProfile.user_id == user_id)
        )
        return result.scalar_one() or 0.0
    async def get_seller_rating(self, user_id: UUID) -> float:
        result = await self.db.execute(
            select(SellerProfile.rating).where(SellerProfile.user_id == user_id)
        )
        return result.scalar_one() or 0.0

    async def get_seller_rating_count(self, user_id: UUID) -> int:
        result = await self.db.execute(
            select(SellerProfile.reviews_count).where(SellerProfile.user_id == user_id)
        )
        return result.scalar_one() or 0
    async def get_products(self, user_id: UUID) -> List[Product]:
        # Placeholder logic to count products for the seller
        result = await self.db.execute(
            select(SellerProfile).where(SellerProfile.user_id == user_id)
        )
        
        products = await self.db.execute(
            select(Product).where(Product.seller_id == result.scalar_one_or_none().id)
        )
        return products.scalars().all()
    
    ## read this befor using itttttttttttttttt "
    async def get_recent_orders_list(self, user_id: UUID) -> List[dict]:
        products = await self.get_products(user_id)
        
        recent_orders = []  # Collect all orders here
        
        for product in products:
            # Get order lines for this product
            result = await self.db.execute(
                select(OrderLine).where(OrderLine.product_id == product.id)
            )
            order_lines = result.scalars().all()
            
            for order_line in order_lines:
                # Get the order's user_id
                order_result = await self.db.execute(
                    select(Order.user_id).where(Order.id == order_line.order_id)
                )
                user_id_from_order = order_result.scalar_one_or_none()
                
                if user_id_from_order:
                    # Get user info
                    user_result = await self.db.execute(
                        select(User.name, User.email).where(User.id == user_id_from_order)
                    )
                    user_info = user_result.one_or_none()
                    
                    if user_info:
                        # Build the order dict
                        recent_orders.append({
                            'order_line': order_line,
                            'user_name': user_info.name,
                            'user_email': user_info.email
                        })
        
        return recent_orders
    async def create_product(self, seller: User) -> dict:
        # Placeholder logic to create a product for the seller
        new_product = Product(
            seller_id=seller.id,
            name="New Product",
            description="Product Description",
            price=0.0,
            #here just finish the fields according to your Product model definition so just repo work left like categoryId, tags, picture, summary ,,lovely
            stock=0
        )
        self.db.add(new_product)
        await self.db.commit()
        await self.db.refresh(new_product)
        return new_product