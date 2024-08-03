# Deps
from fastapi import APIRouter

# Models
from src.models.getModels import (
    VideoPostModels,
)

delete_router = APIRouter()


# Videos routes
@delete_router.delete("/videos/delete", tags=["videos"])
async def delete_video():
    return {"message": "Backend is working", "status": 200}


# News
@delete_router.get("/news/delete", tags=["news"])
async def delete_news():
    return {"message": "Backend is working", "status": 200}


# file
@delete_router.get("/file/delete", tags=["file"])
async def deelte_file():
    return {"message": "Backend is working", "status": 200}
