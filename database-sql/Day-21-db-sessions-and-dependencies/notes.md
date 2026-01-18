# Day 21 – Database Sessions & Dependency Pattern

## Why session management matters
In backend APIs:
- Multiple users hit the API at the same time
- Each request needs its own DB session
- Sessions must be closed after the request

Improper session handling causes:
- Memory leaks
- Database locks
- App crashes

## The correct backend pattern
FastAPI uses Dependency Injection to:
- Create a DB session per request
- Automatically close it after response

## Dependency pattern for DB
1. Create SessionLocal
2. Create get_db() dependency
3. Inject db session into routes using Depends()

## Why this pattern is important
- Safe for concurrent users
- Clean separation of concerns
- Production-ready design

## Bad vs Good

Bad:
db = SessionLocal()
Use everywhere ❌

Good:
def get_db():
    yield db
    db.close() ✅

## What I learned today
- How DB sessions should be handled in APIs
- Why Depends(get_db) is required
- How FastAPI manages request lifecycle with DBs
