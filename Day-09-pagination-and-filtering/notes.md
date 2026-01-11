# Day 9 – Pagination & Filtering

## Why pagination is important
APIs should never return too much data at once.
Large responses:
- Slow down the app
- Waste bandwidth
- Hurt performance

Pagination solves this problem.

## What is pagination?
Pagination means returning data in small chunks.

Common parameters:
- skip → how many records to skip
- limit → how many records to return

Example:
GET /jobs?skip=0&limit=10

## What is filtering?
Filtering allows clients to request only specific data.

Example:
GET /jobs?status=Applied
GET /jobs?company=Google

## Why backend developers must handle this
- Frontend depends on backend filtering
- Backend controls performance
- Almost every real API uses pagination

## Query parameters role
Pagination and filtering are implemented using query parameters.

## What I learned today
- Why pagination is necessary
- How to use skip & limit
- How to filter data using query parameters
- How to design performance-friendly APIs
