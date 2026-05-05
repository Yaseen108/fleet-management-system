# Fleet Management System 🚛

A full-stack fleet and transport management system designed to manage vehicles, drivers, fuel usage, and operational workflows.

---

## 🧰Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite (initially, PostgreSQL later)
- JWT Authentication
- CORS Middleware

### Frontend
- React
- Vite
- TypeScript
- Axios
- React Router
- Tailwind CSS
- Recharts (data visualization)

---

## Architecture Overview

This project follows a modular backend architecture:

### Backend
- API Layer (FastAPI routes)
- Service Layer (business logic)
- Data Layer (SQLAlchemy ORM models)
- Dependency Injection (FastAPI Depends system)
- JWT-based authentication for security

### Frontend
- Component-based architecture (React)
- Context API for authentication state
- Axios for API communication
- Protected routes via JWT
- Reusable UI components (Card, Layout)

---

## ✅Features (Completed)

### 🔐 Authentication & Security
- User registration with validation
- Secure login system using JWT
- Password hashing using bcrypt
- Token-based authentication flow
- Frontend login + token persistence
- Automatic token injection via Axios interceptors

### 🔑 Authorization (RBAC)
- Role-based access control (Admin / Manager / Driver)
- Endpoint-level restrictions
- Role validation via dependency injection

---

## Core Modules

### 🚗 Vehicle Management
- Create and list vehicles
- Assign drivers to vehicles
- Track vehicle status

### 👨‍✈️ Driver Management
- Create and list drivers
- License validation (expiry tracking)

### 🔗 Driver-Vehicle Assignment
- One-to-one relationship between driver and vehicle
- Foreign key implementation using SQLAlchemy
- Nested API responses

### ⛽ Fuel Management
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

## 📊 Analytics & Reporting (NEW)

### Fuel Analytics
- Total fuel cost per vehicle
- Total litres consumed per vehicle
- Average fuel price per litre

### Advanced Query Features
- Aggregation queries (`SUM`, `AVG`, `GROUP BY`)
- Date range filtering (`start_date`, `end_date`)
- Dashboard-ready API responses

---

## 🖥️ Frontend Dashboard

### Features
- JWT-based login system
- Global auth state (Context API)
- Axios interceptor for token handling
- Responsive dashboard layout
- Reusable UI components

### 📈 Data Visualization
- Bar charts using Recharts
- Fuel cost per vehicle
- Fuel litres per vehicle
- Average price per litre

### ⚠️ Note on Authentication
- If charts fail to load, it may be due to an expired or missing JWT token
- Re-login refreshes authentication and restores API access

### API Integration Example
```bash
GET /analytics/fuel-cost-per-vehicle
```
---

## 🌐 Cross-Origin Support

- CORS middleware configured in FastAPI
- Allows frontend (`localhost:5173`) to communicate with backend

---

### Example Endpoints
```bash
GET /analytics/fuel-cost-per-vehicle
GET /analytics/fuel-litres-per-vehicle
GET /analytics/average-price-per-litre

GET /analytics/fuel-cost-per-vehicle?start_date=2026-01-01&end_date=2026-12-31
```

---

## 🚧 Planned Features (In Progress)

### Frontend Enhancements
- Date filtering UI
- Protected routes (frontend auth guards)
- Advanced charts (line, pie)

### Core System Modules
- Trip management module
- Expense tracking system

### Advanced Features
- File uploads (fuel receipts, documents)
- Notifications system
- Audit logs for all transactions

---

## Project Status

### Phase 6: Full-Stack Integration Complete

### ✔Implemented:
- Backend authentication & RBAC
- Relational data modeling (vehicles, drivers, fuel logs)
- Fuel approval workflow
- Analytics & reporting layer
- Date-based filtering
- React frontend with login system
- JWT authentication flow (frontend ↔ backend)
- API integration using Axios
- CORS configuration for cross-origin requests
- Chart-based data visualization

---

## Domain Entities

- **User** → Authentication and system access control
- **Vehicle** → Fleet assets with assigned driver and operational status
- **Driver** → Licensed operators linked to vehicles
- **Fuel Log** → Tracks fuel usage, cost, and approval status

---

## Data Relationships

- One-to-One → Vehicle ↔ Driver
- One-to-Many → Vehicle → Fuel Logs

---

## Running the Project

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Access Points
- Backend API Docs: http://127.0.0.1:8000/docs
- Frontend App: http://localhost:5173

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

frontend/
└── src/
    ├── api/
    ├── pages/
    ├── components/
    ├── context/
    └── App.tsx
```

## Author

**Muhammed Yaseen Ismail**
Full Stack Developer (React + Python)  