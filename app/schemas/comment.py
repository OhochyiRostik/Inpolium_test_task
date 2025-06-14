from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str
    post_id: int

class CommentUpdate(BaseModel):
    content: str | None = None

class CommentOut(BaseModel):
    id: int
    content: str
    post_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
