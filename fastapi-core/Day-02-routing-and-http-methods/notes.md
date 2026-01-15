# Day 2 – FastAPI Routing & HTTP Methods

## What is a Route?
A route (or endpoint) is a specific URL path where the backend listens for requests.

Example:
GET /users
GET /expenses

Each route performs a specific task.

## What are HTTP Methods?
HTTP methods define what action the client wants to perform.

Common methods:
- GET    → Read data
- POST   → Create data
- PUT    → Update data
- DELETE → Remove data

## GET vs POST (Important Difference)

GET:
- Used to fetch data
- Data is NOT sent in the body
- Safe and read-only

POST:
- Used to send data to server
- Data is sent in request body
- Used for creating resources

## Why Backend Developers Care
- Correct method usage = clean APIs
- APIs are contracts between frontend and backend
- Wrong method usage causes security and logic issues

## What I learned today
- How routing works in FastAPI
- Difference between GET and POST
- How backend receives data
