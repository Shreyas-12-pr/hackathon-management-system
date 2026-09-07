from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.api.users import router as users_router


app = FastAPI(
    title="Hackathon Management System API",
    version="0.1.0",
)


app.include_router(users_router)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "hms-api",
    }


@app.get("/health/db")
async def database_health(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "connected",
        "result": result.scalar(),
    }