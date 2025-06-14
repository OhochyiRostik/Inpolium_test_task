from fastapi import APIRouter, HTTPException
from app.schemas.comment import CommentCreate, CommentUpdate, CommentOut
from app.crud import comment as comment_crud

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.get("/", response_model=list[CommentOut])
async def list_comments(skip: int = 0, limit: int = 10):
    return await comment_crud.get_comments(skip, limit)

@router.get("/{comment_id}", response_model=CommentOut)
async def read_comment(comment_id: int):
    comment = await comment_crud.get_comment(comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.post("/", response_model=CommentOut)
async def create(comment: CommentCreate):
    return await comment_crud.create_comment(comment)

@router.put("/{comment_id}", response_model=CommentOut)
async def update(comment_id: int, comment: CommentUpdate):
    return await comment_crud.update_comment(comment_id, comment)

@router.delete("/{comment_id}")
async def delete(comment_id: int):
    await comment_crud.delete_comment(comment_id)
    return {"ok": True}