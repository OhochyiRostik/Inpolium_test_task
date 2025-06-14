from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.post import Post
from app.database import SessionLocal

async def get_posts(skip: int = 0, limit: int = 10):
    async with SessionLocal() as session:
        result = await session.execute(select(Post).offset(skip).limit(limit))
        return result.scalars().all()

async def get_post(post_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Post).where(Post.id == post_id))
        return result.scalar_one_or_none()

async def create_post(post):
    async with SessionLocal() as session:
        db_post = Post(**post.dict())
        session.add(db_post)
        await session.commit()
        await session.refresh(db_post)
        return db_post

async def update_post(post_id: int, post_data):
    async with SessionLocal() as session:
        await session.execute(update(Post).where(Post.id == post_id).values(**post_data.dict(exclude_unset=True)))
        await session.commit()
        return await get_post(post_id)

async def delete_post(post_id: int):
    async with SessionLocal() as session:
        await session.execute(delete(Post).where(Post.id == post_id))
        await session.commit()