from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy import create_engine
from alembic import context

# Import your models metadata
from app.models.user import User  # Import specific models
from app.models.sellerProfile import SellerProfile
from app.models.product import Product
from app.models.cart import Cart
from app.models.cartItem import CartItem
# Import specific models
from app.db.database import Base, SQLALCHEMY_DATABASE_URL  # Import Base from database.py

# this is the Alembic Config object
config = context.config

# Set the database URL in Alembic configuration
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# add your model's MetaData object here
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Use regular create_engine instead of async
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()
            context.run_migrations()

if context.is_offline_mode():
        

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()