# Day 13 – Pagination & Performance Awareness

## Why pagination with databases is different
In real applications, data is stored in databases, not lists.
Fetching all records:
- Is slow
- Consumes memory
- Does not scale

Pagination limits how much data is fetched.

## Offset & Limit (MOST IMPORTANT)
Databases use:
- OFFSET → skip records
- LIMIT → number of records

Example SQL:
SELECT * FROM jobs LIMIT 10 OFFSET 20;

This fetches records 21–30.

## Why backend controls pagination
- Frontend should not decide data volume
- Backend protects database
- Prevents performance issues

## Bad vs Good API
Bad:
GET /jobs → returns 100k rows ❌

Good:
GET /jobs?skip=0&limit=20 ✅

## Performance mindset
Backend developers must:
- Control data size
- Avoid unnecessary queries
- Think about scaling early

## What I learned today
- Why pagination is mandatory with DBs
- How OFFSET & LIMIT work
- How backend protects performance
