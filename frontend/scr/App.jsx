import React, { useState, useEffect } from 'react';
import { fetchPhotos, uploadPhoto } from './api';
import './App.css';

function App() {
  const [photos, setPhotos] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    loadPhotos();
  }, [search]);

  const loadPhotos = async () => {
    const res = await fetchPhotos(search);
    setPhotos(res.data);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('title', e.target.title.value);
    formData.append('file', e.target.file.files[0]);
    await uploadPhoto(formData);
    loadPhotos();
  };

  return (
    <div className="container">
      <h1>My Photo Gallery</h1>
      <input type="text" placeholder="Tìm kiếm ảnh..." onChange={(e) => setSearch(e.target.value)} />
      
      <form onSubmit={handleUpload}>
        <input name="title" placeholder="Tên ảnh" required />
        <input name="file" type="file" required />
        <button type="submit">Tải lên</button>
      </form>

      <div className="grid">
        {photos.map(p => (
          <div key={p.id} className="card">
            <img src={`http://localhost:8000/${p.image_url}`} width="200" alt={p.title} />
            <p>{p.title}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
export default App;