import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

from routers import func_router
from db.config import engine, Base

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

origins = [
    "http://militarylub.com",
    "https://militarylub.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(func_router.router, prefix="/function", tags=["Function"])

@app.get("/robots.txt", response_class=PlainTextResponse)
async def get_robots():
    robots = ''
    with open('robots.txt', 'r') as file_data:
        for line in file_data:
            robots += line

    return robots

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, workers=3)
