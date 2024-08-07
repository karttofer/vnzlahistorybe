# Deps
from fastapi import APIRouter

get_welcome = APIRouter()


# Video
@get_welcome.get("/", tags=["videos"])
async def welcome():
    return {
        "message": "Backend is working, welcome to our API. FREE VENEZUELA",
        "status": 200,
    }
