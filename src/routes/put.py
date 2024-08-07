from fastapi import APIRouter, File, Request, UploadFile, HTTPException, Depends
from pymongo.errors import PyMongoError
from motor.motor_asyncio import AsyncIOMotorDatabase
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from fastapi.responses import JSONResponse
import logging

put_router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_database(request: Request) -> AsyncIOMotorDatabase:
    return request.app.database


@put_router.put("/videos/upload", tags=["videos"])
async def put_video(
    file: UploadFile = File(...), db: AsyncIOMotorDatabase = Depends(get_database)
):
    try:
        grid_fs = AsyncIOMotorGridFSBucket(db, bucket_name="videos_collection")
        file_id = await grid_fs.upload_from_stream(
            file.filename, file.file, metadata={"content_type": file.content_type}
        )

        logger.info(f"File uploaded successfully with file_id: {file_id}")
        return JSONResponse(
            status_code=200,
            content={
                "message": "Video uploaded successfully",
                "file_id": str(file_id),
            },
        )
    except PyMongoError as e:
        logger.error(f"Failed to upload video: {e}")
        raise HTTPException(status_code=500, detail="Failed to upload video")
