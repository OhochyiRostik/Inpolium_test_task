from pydantic import BaseModel

class TopicCreate(BaseModel):
    name: str

class TopicOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True