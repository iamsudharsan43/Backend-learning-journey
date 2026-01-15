# Day 14 – API Versioning

## What is API versioning?
API versioning is a way to release changes to an API
without breaking existing clients.

Once an API is public, you must assume:
- Mobile apps
- Frontend apps
- External users
depend on it.

## Why versioning is important
Without versioning:
- Old clients break
- Users face errors
- Trust in the API is lost

With versioning:
- Old clients keep working
- New features can be added safely
- Backend can evolve

## Common versioning strategies
1. URL versioning (most common)
   /api/v1/jobs
   /api/v2/jobs

2. Header versioning
   Accept-Version: v1

3. Query versioning (less preferred)
   /jobs?version=1

## Why URL versioning is preferred
- Clear and explicit
- Easy to debug
- Easy to maintain
- Widely used in industry

## Backward compatibility
Backward compatibility means:
- v1 keeps working even when v2 is released
- Old behavior is preserved

## When to create a new version
- Response format changes
- Field names change
- Business logic changes
- Breaking changes occur

## What I learned today
- Why APIs need versioning
- How to design backward-compatible APIs
- How FastAPI supports versioned routes
