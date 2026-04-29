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
- Vehicle management (create, list, assign driver)
- Driver management (create, list)
- Driver-to-vehicle assignment (one-to-one relationship)
- Relational data modeling using foreign keys
- Nested API responses (vehicle includes driver)
- Data validation and uniqueness constraints
- Role-restricted operations (Admin / Manager access)

---

## Planned Features (In Progress)

### Core System Modules
- Fuel tracking and approvals
- Trip management module
- Expense tracking system

### Advanced Features
- Analytics dashboard (fuel efficiency, cost tracking)
- File uploads (fuel receipts, documents)
- Notifications system
- Audit logs for all transactions

---

## Project Status

Current Phase: **Relational Data Modeling Implemented (Phase 3)**

Implemented:
- JWT Authentication system
- Secure password hashing (bcrypt)
- User registration and login
- Protected route middleware (get_current_user)
- Role-based access control (RBAC)
- Vehicle module (CRUD + RBAC)
- Driver module (CRUD + RBAC)
- Driver-to-vehicle relationship (foreign key + ORM mapping)
- Assignment endpoint for linking drivers and vehicles
- FastAPI dependency injection pattern

---

## Domain Entities

- **User** → Authentication and system access control
- **Vehicle** → Fleet assets with assigned driver and operational status
- **Driver** → Licensed operators linked to vehicles

---

## Data Relationships

- One-to-One: A vehicle can be assigned to one driver
- Drivers can be linked to vehicles via foreign key relationships
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