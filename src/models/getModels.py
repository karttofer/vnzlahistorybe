# Deps
from pydantic import BaseModel

class VideoPostModels(BaseModel):
    video_name: str
    video_date: str
    video_source: str
    video_tag: str