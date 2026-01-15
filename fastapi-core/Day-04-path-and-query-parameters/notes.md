# Day 4 – Path & Query Parameters in FastAPI

## What are Path Parameters?
Path parameters are values passed directly in the URL path.
They usually identify a specific resource.

Example:
GET /expenses/1
Here, 1 is the expense ID.

## Why Path Parameters are important
- Used to fetch/update/delete a specific resource
- Makes APIs clean and readable
- Very common in REST APIs

## What are Query Parameters?
Query parameters are optional values added after ? in the URL.

Example:
GET /expenses?category=Food
GET /expenses?category=Food&min_amount=500

## Why Query Parameters are important
- Used for filtering, searching, pagination
- Do not change the resource path
- Make APIs flexible

## Path vs Query Parameters
Path:
- Mandatory
- Identify a resource
- Part of the URL path

Query:
- Optional
- Used for filtering/searching
- After ? in the URL

## What I learned today
- How to use path parameters in FastAPI
- How to use query parameters
- How APIs are designed in real applications
