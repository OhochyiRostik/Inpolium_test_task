from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.comment import Comment
from app.database import SessionLocal

async def get_comments(skip: int = 0, limit: int = 10):
    async with SessionLocal() as session:
        result = await session.execute(select(Comment).offset(skip).limit(limit))
        return result.scalars().all()

async def get_comment(comment_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Comment).where(Comment.id == comment_id))
        return result.scalar_one_or_none()

async def create_comment(comment):
    async with SessionLocal() as session:
        db_comment = Comment(**comment.dict())
        session.add(db_comment)
        await session.commit()
        await session.refresh(db_comment)
        return db_comment

async def update_comment(comment_id: int, comment_data):
    async with SessionLocal() as session:
        await session.execute(update(Comment).where(Comment.id == comment_id).values(**comment_data.dict(exclude_unset=True)))
        await session.commit()
        return await get_comment(comment_id)

async def delete_comment(comment_id: int):
    async with SessionLocal() as session:
        await session.execute(delete(Comment).where(Comment.id == comment_id))
        await session.commit()