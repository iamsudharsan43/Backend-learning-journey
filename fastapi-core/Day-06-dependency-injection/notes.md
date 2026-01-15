# Day 6 – Dependency Injection & Depends()

## What is Dependency Injection?
Dependency Injection (DI) means:
Instead of writing the same logic again and again,
we write it once and reuse it everywhere.

FastAPI provides this using the `Depends()` function.

## Why Dependency Injection is important
Without DI:
- Code duplication
- Hard to maintain
- Difficult to add authentication later

With DI:
- Clean code
- Reusable logic
- Easy authentication & database access
- Professional backend structure

## Real-world example
Checking if a user is logged in should not be written in every route.
It should be written once and reused.

## How Depends() works
- FastAPI calls the dependency function
- Gets its return value
- Injects it into the route function

## Common use cases
- Authentication
- Database session
- Common validation
- Configuration access

## What I learned today
- What dependency injection is
- Why backend APIs use it
- How FastAPI implements it using Depends()
