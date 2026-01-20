# Day 23 – Database Relationships & Foreign Keys

## Why relationships matter
Real applications store related data in separate tables.
Examples:
- User → Jobs
- User → Expenses
- Order → OrderItems

This avoids data duplication and keeps data consistent.

## What is a Foreign Key?
A foreign key is a column that references the primary key
of another table.

Example:
jobs.user_id → users.id

## One-to-Many relationship
One user can have many jobs.
But one job belongs to only one user.

users (1) -------- (many) jobs

## Why we don't put everything in one table
- Avoid duplicate data
- Easier updates
- Better performance
- Cleaner design

## ORM relationship concept
SQLAlchemy lets us define relationships using:
- ForeignKey
- relationship()

This allows:
user.jobs
job.user

## What I learned today
- Why relational databases use relationships
- How foreign keys work
- How to model one-to-many relationships in ORM
