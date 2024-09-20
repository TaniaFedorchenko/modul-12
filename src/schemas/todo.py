from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from src.schemas.user import UserResponse


#  валідація для вхідних даних
class TodoSchema(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=250)
    completed: Optional[bool] = False

class TodoUpdateSchema(TodoSchema):
    completed: bool


class TodoResponse(BaseModel):
    id: int = 1
    title: str
    description: str
    completed: bool
    created_at: datetime | None
    updated_at: datetime | None
    user: UserResponse | None

    model_config = ConfigDict(from_attributes=True)

    # з допомогою цієї властивості ( останній рядок ) ми домоглися того, що при виводі в фастапі  з даними кота показуються дані його власника

    #class Config:
     #   from_attributes = True