from sqlalchemy.orm import Session
from . import models, schemas

def get_photos(db: Session, skip: int = 0, limit: int = 100, search: str = ""):
    query = db.query(models.Photo)
    if search: # [cite: 41]
        query = query.filter(models.Photo.title.contains(search))
    return query.offset(skip).limit(limit).all()

def create_user_photo(db: Session, photo: schemas.PhotoCreate, image_path: str, user_id: int):
    db_photo = models.Photo(**photo.dict(), image_url=image_path, user_id=user_id) # [cite: 36]
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

def delete_photo(db: Session, photo_id: int):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first() # [cite: 39]
    if db_photo:
        db.delete(db_photo)
        db.commit()
    return db_photo