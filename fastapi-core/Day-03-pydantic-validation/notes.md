# Day 3 – Request Body Validation with Pydantic

## Why validation is important
Backend APIs receive data from users, frontend apps, and external systems.
Invalid data can break the application or cause security issues.

## Problem with using dict
When we use a plain dict:
- No validation
- Any data type is accepted
- Missing fields are not detected

Example:
{
  "category": 123,
  "amount": "abc"
}

This should not be allowed.

## What is Pydantic?
Pydantic is a data validation library used by FastAPI.
It ensures:
- Correct data types
- Required fields exist
- Automatic error responses

## How FastAPI uses Pydantic
FastAPI automatically:
- Validates incoming request body
- Converts types
- Returns meaningful error messages

## Benefits for backend developers
- Cleaner code
- Safer APIs
- Less manual validation
- Production-ready APIs

## What I learned today
- Why dict is unsafe for request bodies
- How Pydantic models work
- How FastAPI validates input automatically
