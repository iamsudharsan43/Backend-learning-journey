# Day 22 – Full CRUD API with FastAPI + SQLAlchemy

## Goal of Day 22
The goal of today was to build a **complete backend CRUD API**
by combining:
- FastAPI
- SQLAlchemy ORM
- Database session dependency
- Proper HTTP methods and errors

This is the foundation of **real backend applications**.

---

## What is CRUD?
CRUD represents the four core operations performed on data:

- **Create** → Add new data
- **Read** → Fetch existing data
- **Update** → Modify existing data
- **Delete** → Remove data

Almost every backend system is built on CRUD.

---

## Architecture Used Today

The backend was split into logical layers:

1. **database.py**
   - Database connection
   - Session creation
   - Dependency (`get_db()`)

2. **models.py**
   - SQLAlchemy ORM models
   - Table structure mapping

3. **main.py**
   - FastAPI routes
   - CRUD logic
   - Dependency injection
   - Error handling

This structure improves:
- Readability
- Maintainability
- Scalability

---

## Database Session Dependency Pattern

A database session is created **per request** using:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
