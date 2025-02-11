from bson import ObjectId
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Bookmark(BaseModel):
    _id: Optional[ObjectId] = None
    title: str
    url: str
    description: Optional[str] = None
    tags: list[str] = []
    group_id: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None

