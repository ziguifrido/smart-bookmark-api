from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Group(BaseModel):
    _id: Optional[str] = None
    title: str
    description: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = None