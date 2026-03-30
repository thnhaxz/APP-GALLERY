from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True) # [cite: 48]
    username = Column(String, unique=True) # [cite: 49]
    email = Column(String, unique=True) # [cite: 50]
    password = Column(String) # [cite: 51]
    photos = relationship("Photo", back_populates="owner")

class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, index=True) # [cite: 53]
    title = Column(String) # [cite: 54]
    description = Column(String) # [cite: 55]
    image_url = Column(String) # [cite: 56]
    uploaded_at = Column(DateTime, default=datetime.utcnow) # [cite: 57]
    user_id = Column(Integer, ForeignKey("users.id")) # [cite: 58]
    owner = relationship("User", back_populates="photos")