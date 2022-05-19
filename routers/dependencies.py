from db.config import async_session
from db.dals.func_dto import FuncDTO

async def get_func_dto():
    async with async_session() as session:
        async with session.begin():
            yield FuncDTO(session)