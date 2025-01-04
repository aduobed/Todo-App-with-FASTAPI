from pydantic import BaseModel, Field
from typing import Optional


class TodoModel(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(
        gt=0, lt=6, description="Priority should be from 1 to 5")
    complete: bool = False
