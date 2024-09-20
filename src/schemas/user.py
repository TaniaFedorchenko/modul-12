from typing import Optional

from pydantic import BaseModel, Field, EmailStr, ConfigDict

from src.entity.models import Role


#  валідація для вхідних даних
class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password:  str = Field(min_length=3, max_length=8)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    avatar: str |  None
    role: Role

    model_config = ConfigDict(from_attributes=True)

    # з допомогою цієї властивості ( останній рядок ) ми домоглися того, що при виводі в фастапі  з даними кота показуються дані його власника

    #class Config:
        #from_attributes = True

class TokenSchema(BaseModel):

    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RequestEmail(BaseModel):
    email: EmailStr

