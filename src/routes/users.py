import cloudinary.uploader
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.ext.asyncio import AsyncSession

from src.conf.config import config
from src.database.db import get_db
from src.entity.models import User
from src.schemas.user import UserResponse
from src.services.auth import auth_service
from src.repository import users as repositories_users


router = APIRouter(prefix="/users", tags=["users"])
cloudinary.config(
    cloud_name=config.CLOUDINARY_NANE,
    api_key=config.CLOUDINARY_API_KEY,
    api_secret=config.CLOUDINARY_API_SECRET,
    secure=True,
)


@router.get(
    "/me",
    response_model=UserResponse,
    dependencies=[Depends(RateLimiter(times=1, seconds=20))],
)
# RateLimiter - параметр, що встановлює обмеження на кількість запитів( в д.в. 1 на 20 сек)
async def get_current_user(user: User = Depends(auth_service.get_current_user)):
    return user


@router.patch(
    "/avatar",
    response_model=UserResponse,
    dependencies=[Depends(RateLimiter(times=1, seconds=20))],
)  # RateLimiter - параyh що встановлює обмеження на кількість запитів( в д.в. 1 на 20 сек)
async def get_current_user(
    file: UploadFile = File(),
    user: User = Depends(auth_service.get_current_user),
    db: AsyncSession = Depends(get_db),
):
    public_id = f"Folders/Web16/{user.email}"
    resource = cloudinary.uploader.upload(
        file.file, public_id=public_id, overwrite=True
    )
    print(resource)
    resource_url = cloudinary.CloudinaryImage(public_id).build_url(
        width=250, height=250, crop="fill", version=resource.get("version")
    )
    user = await repositories_users.update_avatar_url(user.email, resource_url, db)
    return user
