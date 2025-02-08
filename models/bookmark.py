from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Bookmark(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    tags: list[str] = []
    group: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
