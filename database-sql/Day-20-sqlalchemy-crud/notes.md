# Day 20 – SQLAlchemy CRUD Operations

## What is CRUD?
CRUD represents the four basic operations on data:
- Create
- Read
- Update
- Delete

Every backend API is mostly CRUD.

## CRUD with ORM
ORM allows CRUD using Python objects instead of raw SQL.

## Mapping CRUD to ORM

CREATE  -> session.add() + commit
READ    -> session.query()
UPDATE  -> modify object + commit
DELETE  -> session.delete() + commit

## Why CRUD matters
- User registration
- Job posting
- Expense tracking
- Any real backend feature

## Important ORM rules
- Always commit changes
- Always close session
- Use filters to avoid modifying all rows

## What I learned today
- Full CRUD using SQLAlchemy
- How backend apps manipulate data
- How ORM maps to database operations
