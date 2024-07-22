from fastapi import APIRouter, Depends, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from app.api.dependencies.auth import get_current_user_auth
from app.api.dependencies.database import get_repository
from app.database.repositories.segments import SegmentRepository  
from app.models.user import User
from app.schemas.segment import SegmentCreate, SegmentUpdate, SegmentResponse  
from app.models.segment import Segment  
from app.utils import handle_result
from pydantic import BaseModel, ConfigDict

router = APIRouter()

@router.post(
    "/",
    status_code=HTTP_201_CREATED,
    response_model=SegmentResponse,
    name="segment:create",
)
async def create_segment(
    *,
    segment_in: SegmentCreate,
    current_user: User = Depends(get_current_user_auth()),
    segment_repo: SegmentRepository = Depends(get_repository(SegmentRepository)),
) -> SegmentResponse:
    segment_in.user_id = current_user.id
    segment = await segment_repo.create_segment(segment_in=segment_in)
    return await handle_result(segment)

@router.get(
    "/{segment_id}",
    response_model=SegmentResponse,
    name="segment:read",
)
async def read_segment(
    *,
    segment_id: int = Path(..., gt=0),
    segment_repo: SegmentRepository = Depends(get_repository(SegmentRepository)),
) -> SegmentResponse:
    segment = await segment_repo.get_segment(segment_id=segment_id)
    if not segment:
        raise HTTPException(status_code=404, detail="Segment not found")
    return segment

@router.put(
    "/{segment_id}",
    response_model=SegmentResponse,
    name="segment:update",
)
async def update_segment(
    *,
    segment_id: int = Path(..., gt=0),
    segment_in: SegmentUpdate,
    segment_repo: SegmentRepository = Depends(get_repository(SegmentRepository)),
) -> SegmentResponse:
    segment = await segment_repo.update_segment(segment_id=segment_id, segment_in=segment_in)
    if not segment:
        raise HTTPException(status_code=404, detail="Segment not found")
    return segment

@router.delete(
    "/{segment_id}",
    status_code=HTTP_204_NO_CONTENT,
    name="segment:delete",
)
async def delete_segment(
    *,
    segment_id: int = Path(..., gt=0),
    segment_repo: SegmentRepository = Depends(get_repository(SegmentRepository)),
) -> None:
    success = await segment_repo.delete_segment(segment_id=segment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Segment not found")
