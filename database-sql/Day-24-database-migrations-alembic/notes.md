# Day 24 – Database Migrations with Alembic

## What is a database migration?
A migration is a controlled way to:
- Create tables
- Modify columns
- Add or remove fields
- Update schema without losing data

## Why create_all() is dangerous
Using:
Base.metadata.create_all()

Problems:
- No version tracking
- Cannot modify existing tables safely
- Risk of data loss
- Not suitable for production

## What is Alembic?
Alembic is the official migration tool for SQLAlchemy.

It allows:
- Version-controlled DB changes
- Upgrade & downgrade support
- Safe schema evolution

## How migrations work
1. Models change
2. Alembic generates migration file
3. Migration is applied to DB
4. DB schema is updated safely

## Key Alembic concepts

### Revision
A migration version file

### upgrade()
Code to apply changes

### downgrade()
Code to revert changes

### Head
Latest migration

## When migrations are required
- Adding new columns
- Renaming fields
- Changing constraints
- Creating relationships

## What I learned today
- Why migrations are critical
- How Alembic manages schema changes
- How professionals update databases
