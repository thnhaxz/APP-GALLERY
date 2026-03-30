from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import shutil
import os
from . import models, database

# Khởi tạo App
app = FastAPI()

# 1. CẤU HÌNH CORS (Bắt buộc để Frontend cổng 5500 gọi được)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các nguồn (bao gồm cổng 5500)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. TỰ ĐỘNG TẠO THƯ MỤC UPLOADS NẾU CHƯA CÓ
# Thư mục này nằm cùng cấp với gallery.db và requirements.txt
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# 3. MOUNT THƯ MỤC ĐỂ TRÌNH DUYỆT XEM ĐƯỢC ẢNH
# Địa chỉ ảnh sẽ là: http://127.0.0.1:8000/uploads/ten_anh.jpg
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

@app.post("/upload")
async def upload_image(
    title: str = Form(...), 
    desc: str = Form(""), 
    file: UploadFile = File(...), 
    db: Session = Depends(database.get_db)
):
    try:
        # Tạo tên file an toàn để không bị trùng hoặc lỗi ký tự
        file_name = file.filename.replace(" ", "_")
        file_path = os.path.join(UPLOAD_DIR, file_name)
        
        # THỰC HIỆN GHI FILE VÀO THƯ MỤC UPLOADS
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Lưu đường dẫn vào Database (Dùng đường dẫn tương đối để dễ hiển thị)
        image_url = f"uploads/{file_name}"
        
        new_photo = models.Photo(
            title=title, 
            description=desc, 
            image_url=image_url, 
            user_id=1 # Giả định ID user mặc định
        )
        db.add(new_photo)
        db.commit()
        db.refresh(new_photo)
        
        return {"message": "Thành công", "data": new_photo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/photos")
def get_photos(search: str = "", db: Session = Depends(database.get_db)):
    # Tìm kiếm ảnh theo tên nếu có yêu cầu
    query = db.query(models.Photo)
    if search:
        query = query.filter(models.Photo.title.contains(search))
    return query.all()

@app.delete("/photos/{id}")
def delete_photo(id: int, db: Session = Depends(database.get_db)):
    photo = db.query(models.Photo).filter(models.Photo.id == id).first()
    if photo:
        # Xóa file vật lý trong thư mục uploads
        if os.path.exists(photo.image_url):
            os.remove(photo.image_url)
        db.delete(photo)
        db.commit()
    return {"message": "Đã xóa"}