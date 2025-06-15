from fastapi import APIRouter, HTTPException, Query
from typing import Literal
from app.schemas.comment import CommentCreate, CommentUpdate, CommentOut
from app.crud import comment as comment_crud

router = APIRouter(prefix="/comments", tags=["Comments"])

allowed_sort_fields = {"id", "created_at", "updated_at", "post_id"}

@router.get("/", response_model=list[CommentOut])
async def list_comments(
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
    return await comment_crud.get_comments(skip=skip, limit=limit, sort_by=sort_by, order=order)

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