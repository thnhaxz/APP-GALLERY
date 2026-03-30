# 📸 Gallery App

## 📌 Giới thiệu

Gallery App là một ứng dụng web cho phép người dùng:

* Đăng ký / đăng nhập
* Upload ảnh
* Xem danh sách ảnh
* Xem chi tiết ảnh
* Chỉnh sửa thông tin ảnh
* Xóa ảnh
* Tìm kiếm ảnh theo tên

---

## 🛠 Công nghệ sử dụng

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* ReactJS
* Axios

---

## 📂 Cấu trúc project

```
APP-GALLERY/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │
│   ├── uploads/
│   ├── gallery.db
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│
└── README.md
```

---

## 🚀 Cài đặt & chạy project

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

👉 Backend chạy tại:

```
http://127.0.0.1:8000
```

👉 API docs:

```
http://127.0.0.1:8000/docs
```

---

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

👉 Frontend chạy tại:

```
http://localhost:5173
```

---

## 📡 API chính

### Auth

* POST `/auth/register` → đăng ký
* POST `/auth/login` → đăng nhập

### Photos

* GET `/photos/` → lấy danh sách ảnh
* POST `/photos/` → upload ảnh
* GET `/photos/{id}` → xem chi tiết
* PUT `/photos/{id}` → cập nhật
* DELETE `/photos/{id}` → xóa
* GET `/photos/search/{keyword}` → tìm kiếm

---

## ⚠️ Lưu ý

* Thư mục `uploads/` phải tồn tại để lưu ảnh
* Không push:

  * `venv/`
  * `node_modules/`
  * `gallery.db`
  * `uploads/`

---

## 👨‍💻 Tác giả

* Student Project (FastAPI + React)

---

## ⭐ Ghi chú

Project phục vụ mục đích học tập và thực hành xây dựng web fullstack.
