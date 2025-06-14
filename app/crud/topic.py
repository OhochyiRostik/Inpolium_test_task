from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.topic import Topic
from app.database import SessionLocal

async def get_topics():
    async with SessionLocal() as session:
        result = await session.execute(select(Topic))
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