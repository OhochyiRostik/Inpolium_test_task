from fastapi import APIRouter, HTTPException, Query
from typing import Literal
from app.schemas.topic import TopicCreate, TopicOut
from app.crud import topic as topic_crud

router = APIRouter(prefix="/topics", tags=["Topics"])

allowed_sort_fields = {"id", "name"}

@router.get("/", response_model=list[TopicOut])
async def list_topics(
    skip: int = 0,
    limit: int = 10,
    sort_by: str = Query("id", description="Field to sort by"),
    order: Literal["asc", "desc"] = Query("asc", description="Sort order")
):
    if sort_by not in allowed_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort_by field. Allowed fields: {', '.join(allowed_sort_fields)}"
        )
    return await topic_crud.get_topics(skip=skip, limit=limit, sort_by=sort_by, order=order)

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