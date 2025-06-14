from fastapi import FastAPI
from app.routers import post, comment, topic
from app.database import create_db_and_tables

app = FastAPI(title="Blog API")

app.include_router(post.router)
app.include_router(comment.router)
app.include_router(topic.router)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()