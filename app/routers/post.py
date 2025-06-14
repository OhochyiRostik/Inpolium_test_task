from fastapi import APIRouter, HTTPException
from app.schemas.post import PostCreate, PostOut, PostUpdate
from app.crud import post as post_crud

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=list[PostOut])
async def list_posts(skip: int = 0, limit: int = 10):
    return await post_crud.get_posts(skip, limit)

@router.get("/{post_id}", response_model=PostOut)
async def read_post(post_id: int):
    post = await post_crud.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/", response_model=PostOut)
async def create(post: PostCreate):
    return await post_crud.create_post(post)

@router.put("/{post_id}", response_model=PostOut)
async def update(post_id: int, post: PostUpdate):
    return await post_crud.update_post(post_id, post)

@router.delete("/{post_id}")
async def delete(post_id: int):
    await post_crud.delete_post(post_id)
    return {"ok": True}