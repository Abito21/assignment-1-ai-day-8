# Books Library API

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green.svg)](https://fastapi.tiangolo.com/)

## Deskripsi Proyek

Ini adalah API sederhana yang dibangun menggunakan **FastAPI** dan **SQLModel** untuk mengelola koleksi buku di sebuah perpustakaan. Proyek ini menyediakan endpoint RESTful untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada entitas buku.

## Fitur Utama

* **Manajemen Buku**:
    * `GET /books/`: Mendapatkan daftar semua buku.
    * `GET /books/{book_id}`: Mengambil detail buku spesifik.
    * `POST /books/`: Menambahkan buku baru.
    * `PATCH /books/{book_id}`: Memperbarui informasi buku.
    * `DELETE /books/{book_id}`: Menghapus buku.

* **Database**: Menggunakan SQLite sebagai database lokal, dengan **Alembic** untuk mengelola migrasi skema.

* **Validasi Data**: Menggunakan `Pydantic` melalui `SQLModel` untuk memastikan integritas data.

* **Dokumentasi API Otomatis**: Dokumentasi interaktif tersedia secara otomatis, memudahkan pengujian endpoint.


## Struktur Proyek

```
├── app/
│   ├── database.py       # Konfigurasi database dan model SQLModel.
│   ├── main.py           # Inisialisasi aplikasi FastAPI dan router.
│   ├── routes/
│   │   └── books.py      # Definisi endpoint API untuk buku.
│   └── schema.py         # Definisi model Pydantic untuk request/response.
├── alembic/
│   └── versions/         # Folder untuk file migrasi database.
├── Dockerfile            # File untuk membuat image Docker.
├── Makefile              # Skrip untuk otomatisasi task.
└── pyproject.toml        # Definisi dependensi dan konfigurasi proyek.
```

## Instalasi dan Setup

### Prasyarat

* [Python 3.13+](https://www.python.org/downloads/)
* [uv](https://github.com/astral-sh/uv)

### Langkah-langkah

1.  **Kloning repositori:**
    ```bash
    git clone [https://github.com/Abito21/assignment-1-ai-day-8.git](https://github.com/Abito21/assignment-1-ai-day-8.git)
    cd assignment-1-ai-day-8
    ```

2.  **Instal dependensi:**
    ```bash
    uv sync
    ```

3.  **Jalankan migrasi database:**
    Gunakan `Makefile` untuk mempermudah migrasi database.
    ```bash
    uv run alembic upgrade head
    ```

## Penggunaan

Anda dapat menjalankan server pengembangan menggunakan `uvicorn` melalui `Makefile`.

```bash
uv run uvicorn app.main:app --reload

Aplikasi akan berjalan di https://vps .

Dokumentasi API
Setelah server berjalan, Anda dapat melihat dokumentasi API interaktif pada URL berikut:

Scalar API Reference: https://vps/scalar