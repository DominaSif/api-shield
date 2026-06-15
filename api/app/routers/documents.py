from fastapi import APIRouter, Depends, Request
from app.auth.deps import get_current_user
from app.db.pool import get_db_pool
from app.db.queries import get_user_documents, create_document
from app.models.document import DocumentCreate, DocumentResponse

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/", response_model=list[DocumentResponse])
async def list_documents(
    request: Request,
    user_id: int = Depends(get_current_user)
):
    pool = await get_db_pool(request)
    return await get_user_documents(pool, user_id)

@router.post("/", response_model=DocumentResponse)
async def create_new_document(
    request: Request,
    body: DocumentCreate,
    user_id: int = Depends(get_current_user)
):
    pool = await get_db_pool(request)
    return await create_document(pool, user_id, body.title, body.content)
