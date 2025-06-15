from fastapi import APIRouter, HTTPException
from app.schemas.topic import TopicCreate, TopicOut
from app.crud import topic as topic_crud

router = APIRouter(prefix="/topics", tags=["Topics"])

@router.get("/", response_model=list[TopicOut])
async def list_topics(skip: int = 0, limit: int = 10):
    return await topic_crud.get_topics(skip, limit)

@router.get("/{topic_id}", response_model=TopicOut)
async def read_topic(topic_id: int):
    topic = await topic_crud.get_topic(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic

@router.post("/", response_model=TopicOut)
async def create(topic: TopicCreate):
    return await topic_crud.create_topic(topic)

@router.put("/{topic_id}", response_model=TopicOut)
async def update(topic_id: int, topic: TopicCreate):
    return await topic_crud.update_topic(topic_id, topic)

@router.delete("/{topic_id}")
async def delete(topic_id: int):
    await topic_crud.delete_topic(topic_id)
    return {"ok": True}