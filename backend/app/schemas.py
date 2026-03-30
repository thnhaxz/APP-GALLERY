from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PhotoBase(BaseModel):
    title: str
    description: Optional[str] = None

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    image_url: str
    uploaded_at: datetime
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str