# Day 19 – SQLAlchemy Introduction (ORM)

## What is an ORM?
ORM = Object Relational Mapper

It allows us to:
- Work with databases using Python classes
- Avoid writing raw SQL for common operations
- Keep code cleaner and safer

Instead of SQL:
SELECT * FROM jobs;

We write Python:
session.query(Job).all()

---

## Why ORMs are used in real projects
- Cleaner code
- Less SQL repetition
- Easier maintenance
- Database-agnostic (SQLite → PostgreSQL)

---

## SQL vs ORM (Mindset Shift)

SQL:
INSERT INTO jobs (company, role, status) VALUES (...)

ORM:
job = Job(company="Google", role="Backend", status="Applied")

---

## SQLAlchemy
SQLAlchemy is the most popular ORM in Python.

It has two parts:
1. Core → SQL expression language
2. ORM → Class-based models (we use this)

---

## Key ORM concepts (VERY IMPORTANT)

### Engine
- Connects to the database

### Model
- Python class mapped to a table

### Session
- Handles transactions (add, commit, rollback)

### Base
- Parent class for all models

---

## What I learned today
- What an ORM is
- Why SQLAlchemy is used
- Core components of SQLAlchemy
