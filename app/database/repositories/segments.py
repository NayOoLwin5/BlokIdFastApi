from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.repositories.base import BaseRepository, db_error_handler
from app.models.segment import SegmentCreate
from app.models.segment import Segment


class SegmentRepository(BaseRepository):
    def __init__(self, conn: AsyncSession) -> None:
        super().__init__(conn)

    @db_error_handler
    async def create_post(self, *, post_in: SegmentCreate) -> Segment:
        post = Segment(**post_in.dict())
        self.connection.add(post)
        await self.connection.commit()
        await self.connection.refresh(post)
        return post

    @db_error_handler
    async def get_post_by_id(self, *, post_id: int) -> Segment:
        query = select(Segment).where(Segment.id == post_id)
        result = await self.connection.execute(query)
        return result.scalar_one_or_none()

    @db_error_handler
    async def update_post(self, *, post: Segment, post_in: PostUpdate) -> Segment:
        post_data = post_in.dict(exclude_unset=True)
        for key, value in post_data.items():
            setattr(post, key, value)
        self.connection.add(post)
        await self.connection.commit()
        await self.connection.refresh(post)
        return post

    @db_error_handler
    async def delete_post(self, *, post: Segment) -> Segment:
        await self.connection.delete(post)
        await self.connection.commit()
        return post