# 🧁 Sweet Delight - Aplikasi Manajemen Produk Kue

Sweet Delight adalah aplikasi web sederhana berbasis Django yang memungkinkan pengguna untuk mengelola produk kue—menambah, mengedit, menghapus, dan melihat daftar produk lengkap dengan gambar dan deskripsinya.

## 🚀 Fitur

- Tambah produk kue dengan form isian
- Upload gambar kue
- Tampilkan daftar semua produk
- Edit dan hapus produk
- Kategori kue: Kue Kering, Kue Basah, Roti, Spesial
- Pesan sukses untuk setiap aksi
- Penanganan media file (gambar)

## 🛠️ Teknologi

- Python
- Django 
- HTML Template (Django Template Language)
- SQLite (default)

## 📁 Struktur Direktori

```
tokokue/
├── produk/              # Aplikasi utama
│   ├── templates/       # Template HTML
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── tokokue/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/               # Folder upload gambar
├── manage.py
└── db.sqlite3
```

## ⚙️ Instalasi

1. **Clone repositori**
   ```bash
   git clone https://github.com/firjafny/Praktikum-PPL-Tugas8
   cd tokokue
   ```

2. **Buat virtual environment dan aktifkan**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependensi**
   ```bash
   pip install django
   python -m pip install Pillow
   ```

4. **Migrasi database**
   ```bash
   python manage.py migrate
   ```

5. **Jalankan server**
   ```bash
   python manage.py runserver
   ```

6. **Akses aplikasi**
   Buka browser dan akses `http://127.0.0.1:8000/`

## 🙌 Anggota

- Cut Dahliana (2208107010027)
- Azimah Al-Huda (2208107010069)
- Firjatullah Afny Abus (2208107010059)
