from bson import ObjectId
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Group(BaseModel):
    _id: Optional[ObjectId] = None
    title: str
    description: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None