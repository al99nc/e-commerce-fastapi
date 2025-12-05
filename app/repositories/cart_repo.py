from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional
from app.models import user
from app.models.cart import Cart
from app.models.cartItem import CartItem
from app.models.order import Order
from app.models.orderLine import OrderLine
from app.models.product import Product
from app.models.sellerProfile import SellerProfile, SellerStatus
from app.models.user import UserRole
from app.models.user import User
from app.schemas.base import BaseSchema
from app.schemas.seller import ProductData, SellerRead, SellerRead

class CartRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_cart(self, user: SellerRead) -> dict:
            # Placeholder logic to create a cart for the user
            new_cart = Cart(
                id=UUID(),
                created_by=user.id,
                status="active",
                created_at=func.now(),
                updated_at=func.now()
                )
            self.db.add(new_cart)
            await self.db.commit()
            await self.db.refresh(new_cart)
            return new_cart
    async def find_price(self, product_id: UUID) -> float:
        # Placeholder logic to find product price
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()
        if product:
            return product.price
        return 0.0
    async def create_cart_items(self, product_id: UUID, quantity: int) -> Cart:
        # Placeholder logic to create cart items
        
        price = await self.find_price(product_id)
        new_cart_item = CartItem(
            cart_id=UUID(),
            product_id=product_id,
            price=price,
            quantity=quantity,
            created_at=func.now(),
        )
        self.db.add(new_cart_item)
        await self.db.commit()
        await self.db.refresh(new_cart_item)
        return new_cart_item
    async def add_to_cart(self, user: User, product_id: UUID, quantity: int) -> dict:
        # Placeholder logic to add a product to the cart for the user
        result = await self.db.execute(
            select(Cart).where(Cart.created_by == user.id)
        )
        cart = result.scalar_one_or_none()

        if not cart:
            cart = await self.create_cart(user)
        req = await self.db.execute(
            select(CartItem).where(CartItem.cart_id == cart.id)
        )
        cart_item = req.scalar_one_or_none()
        if not cart_item:
            cart_item = await self.create_cart_items(product_id, quantity)
            
        add_item_to_cart = CartItem(
            cart_item
            )
        self.db.add(add_item_to_cart)
        await self.db.commit()
        await self.db.refresh(add_item_to_cart)
        return add_item_to_cart