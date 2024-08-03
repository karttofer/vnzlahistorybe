# Deps
from fastapi import APIRouter

# Models
from src.models.getModels import (
    VideoPostModels,
)

get_router = APIRouter()


# Video
@get_router.get("/videos/get-video", tags=["videos"])
async def get_videos():
    return {"message": "Backend is working", "status": 200}


# News
@get_router.get("/news/get", tags=["news"])
async def get_news():
    return {"message": "Backend is working", "status": 200}


# files
@get_router.get("/files/get", tags=["files"])
async def get_news():
    return {"message": "Backend is working", "status": 200}
