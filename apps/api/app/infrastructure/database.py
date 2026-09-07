import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


load_dotenv()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://hms:hms_dev_password@localhost:5432/hms",
)


engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)