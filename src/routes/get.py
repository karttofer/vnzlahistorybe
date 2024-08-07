# Deps
from fastapi import APIRouter, HTTPException, Depends, Request
from pymongo.errors import PyMongoError
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorGridFSBucket
from fastapi.responses import StreamingResponse
from bson import ObjectId
import logging

get_router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_database(request: Request) -> AsyncIOMotorDatabase:
    return request.app.database


# Video
@get_router.get("/videos/{file_id}", tags=["videos"])
async def get_video(file_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    try:
        grid_fs = AsyncIOMotorGridFSBucket(db, bucket_name="videos_collection")
        file_obj = await grid_fs.open_download_stream(ObjectId(file_id))

        headers = {
            "Content-Disposition": f"attachment; filename={file_obj.filename}",
            "Content-Type": file_obj.metadata["content_type"],
        }

        return StreamingResponse(file_obj, headers=headers)

    except PyMongoError as e:
        logger.error(f"Failed to retrieve video: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve video")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Unexpected error occurred")


# News
@get_router.get("/news/get", tags=["news"])
async def get_news():
    return {"message": "Backend is working", "status": 200}


# files
@get_router.get("/files/get", tags=["files"])
async def get_news():
    return {"message": "Backend is working", "status": 200}
