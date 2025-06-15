from sqlalchemy.future import select
from sqlalchemy import update, delete, desc, asc
from app.models.topic import Topic
from app.database import SessionLocal

async def get_topics(skip: int = 0, limit: int = 10, sort_by: str = "id", order: str = "asc"):
    async with SessionLocal() as session:
        stmt = select(Topic)
        if hasattr(Topic, sort_by):
            column_attr = getattr(Topic, sort_by)
            stmt = stmt.order_by(desc(column_attr) if order == "desc" else asc(column_attr))
        stmt = stmt.offset(skip).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

async def get_topic(topic_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Topic).where(Topic.id == topic_id))
        return result.scalar_one_or_none()

async def create_topic(topic):
    async with SessionLocal() as session:
        db_topic = Topic(**topic.dict())
        session.add(db_topic)
        await session.commit()
        await session.refresh(db_topic)
        return db_topic

async def update_topic(topic_id: int, topic_data):
    async with SessionLocal() as session:
        await session.execute(update(Topic).where(Topic.id == topic_id).values(**topic_data.dict(exclude_unset=True)))
        await session.commit()
        return await get_topic(topic_id)

async def delete_topic(topic_id: int):
    async with SessionLocal() as session:
        await session.execute(delete(Topic).where(Topic.id == topic_id))
        await session.commit()