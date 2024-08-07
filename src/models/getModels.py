# Deps
from pydantic import BaseModel
import uuid
from typing import List
from pydantic import BaseModel, Field


class VideoPostModels(BaseModel):
    video_name: str
    video_date: str
    video_source: str
    video_tag: str


class GetVideoModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    description: str
    upload_date: str
    sources: str
    video_link: str

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "The title of the video",
                "description": "The description of the video",
                "upload_date": "The date the video was uploaded",
                "sources": "The source of the video",
                "video_link": "The link to the video",
            }
        }


class GetNewsModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(..., title="Title", description="The title of the video")
    description: str = Field(..., description="The description of the video")
    upload_date: str = Field(..., description="The date the video was uploaded")
    update_date: str = Field(..., description="The date the video was updated")
    tags: List[str] = Field(..., description="A list of tags related to the video")
    sources: List[str] = Field(..., description="A list of sources for the video")
    img_url: str = Field(..., description="The link to the video")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "The title of the video",
                "description": "The description of the video",
                "upload_date": "2023-08-02T00:00:00Z",
                "update_date": "2023-08-02T00:00:00Z",
                "tags": ["news", "video", "update"],
                "sources": ["source1", "source2"],
                "img_url": "https://example.com/video",
            }
        }
