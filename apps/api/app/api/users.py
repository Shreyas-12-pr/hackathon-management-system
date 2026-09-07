from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.api.schemas.user import UserResponse
from app.domain.models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "",
    response_model=list[UserResponse],
)
async def list_users(
    db: AsyncSession = Depends(get_db),
) -> list[User]:
    result = await db.execute(
        select(User).order_by(User.created_at.desc())
    )

    return list(result.scalars().all())