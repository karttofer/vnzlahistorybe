# Deps
from fastapi import APIRouter

# Models
from src.models.getModels import (
    VideoPostModels,
)

post_router = APIRouter()


# Video Routes
@post_router.get("/videos/upload-video", tags=["videos"])
async def post_upload_vide():
    return {"message": "Backend is working", "status": 200}


@post_router.get("/videos/upload-video", tags=["videos"])
async def post_edit_video():
    return {"message": "Backend is working", "status": 200}


# News
@post_router.get("/news/create", tags=["news"])
async def post_news_create():
    return {"message": "Backend is working", "status": 200}


@post_router.get("/news/edit", tags=["news"])
async def post_news_edit():
    return {"message": "Backend is working", "status": 200}


# Files
@post_router.get("/files/upload", tags=["files"])
async def post_upload_file():
    return {"message": "Backend is working", "status": 200}


@post_router.get("/files/edit", tags=["files"])
async def post_edit_file():
    return {"message": "Backend is working", "status": 200}
