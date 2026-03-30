const API_BASE = "http://127.0.0.1:8000";

// Hàm lấy danh sách ảnh để hiện lên trang web
async function fetchPhotos(search = "") {
    const res = await fetch(`${API_BASE}/photos?search=${search}`);
    return res.json();
}

// Hàm gửi ảnh lên server
async function uploadPhoto(formData) {
    const res = await fetch(`${API_BASE}/upload`, {
        method: "POST",
        body: formData
    });
    return res.json();
}

// Hàm xóa ảnh
async function deletePhoto(id) {
    const res = await fetch(`${API_BASE}/photos/${id}`, {
        method: "DELETE"
    });
    return res.json();
}