# Fleet Management System 🚛

A full-stack fleet and transport management system designed to manage vehicles, drivers, fuel usage, and operational workflows.

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite (initially, PostgreSQL later)
- JWT Authentication

### Frontend (Planned)
- React + Vite + TypeScript

---

## Architecture Overview

This project follows a modular backend architecture:

- API Layer (FastAPI routes)
- Service Layer (business logic)
- Data Layer (SQLAlchemy ORM models)
- Dependency Injection (FastAPI Depends system)
- JWT-based authentication for security

---

## Features (Completed)

### Authentication & Security
- User registration with validation
- Secure login system using JWT
- Password hashing using bcrypt
- Protected API routes using dependency injection
- Token-based authentication flow

### Authorization (RBAC)
- Role-based access control (Admin / Manager / Driver)
- Role stored at database level
- Reusable role validation dependency
- Endpoint-level access restrictions

### Core Modules

#### 🚗 Vehicle Management
- Create and list vehicles
- Assign drivers to vehicles
- Track vehicle status

#### 👨‍✈️ Driver Management
- Create and list drivers
- License validation (expiry tracking)

#### 🔗 Driver-Vehicle Assignment
- One-to-one relationship between driver and vehicle
- Foreign key implementation using SQLAlchemy
- Nested API responses

#### ⛽ Fuel Management (NEW)
- Log fuel entries per vehicle
- Automatic price-per-litre calculation
- Approval workflow:
  - Driver creates fuel entry
  - Manager/Admin approves entry
- Status tracking (pending → approved)
- Role-based access:
  - Drivers → create entries
  - Managers/Admin → approve entries

---

## Planned Features (In Progress)

### Core System Modules
- Fuel analytics (cost per vehicle, consumption tracking)
- Trip management module
- Expense tracking system

### Advanced Features
- Analytics dashboard (fuel efficiency, cost tracking)
- File uploads (fuel receipts, documents)
- Notifications system
- Audit logs for all transactions

---

## Project Status

Current Phase: **Business Logic & Workflow Implementation (Phase 4)**

### Implemented:
- JWT Authentication system
- Secure password hashing (bcrypt)
- User registration and login
- Protected route middleware (get_current_user)
- Role-based access control (RBAC)
- Vehicle module (CRUD + RBAC)
- Driver module (CRUD + RBAC)
- Driver-to-vehicle relationship (foreign key + ORM mapping)
- Fuel module with approval workflow
- Business logic (price-per-litre calculation)
- FastAPI dependency injection pattern

---

## Domain Entities

- **User** → Authentication and system access control
- **Vehicle** → Fleet assets with assigned driver and operational status
- **Driver** → Licensed operators linked to vehicles
- **Fuel Log** → Tracks fuel usage, cost, and approval status

---

## Data Relationships

- One-to-One: A vehicle can be assigned to one driver
- One-to-Many: A vehicle can have multiple fuel logs
- Fuel logs are linked to vehicles via foreign keys
- ORM relationships implemented using SQLAlchemy

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

**Muhammed Yaseen Ismail**
Full Stack Developer (React + Python)  