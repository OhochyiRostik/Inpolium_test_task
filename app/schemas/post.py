from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    topic_id: int

class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    topic_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True