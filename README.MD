# Fleet Management System 🚛

A full-stack fleet and transport management system designed to manage vehicles, drivers, fuel usage, and operational workflows.

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite (initially, PostgreSQL later)
- JWT Authentication

### Frontend (Planned)
- React + Vite + TypeScript

---

## Features (Current)

- User Registration
- User Login (JWT Authentication)
- Password Hashing (bcrypt)
- API Documentation via Swagger

---

## Running the Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API available at:

http://127.0.0.1:8000/docs

## Project Structure

```bash
backend/
└── app/
    ├── api/
    ├── core/
    ├── db/
    ├── models/
    ├── schemas/
    ├── services/
    └── main.py
```

## Author

### Muhammed Yaseen Ismail