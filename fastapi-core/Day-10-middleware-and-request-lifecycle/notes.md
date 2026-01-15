# Day 10 – Middleware & Request Lifecycle

## What is a request lifecycle?
When a client sends a request:
1. Request enters the backend
2. Middleware runs
3. Route logic executes
4. Response is generated
5. Middleware runs again
6. Response is sent to client

This entire flow is called the request lifecycle.

## What is Middleware?
Middleware is code that runs:
- Before a request reaches the route
- After a response is returned

It applies to ALL requests globally.

## Why middleware is important
Middleware is used for:
- Logging requests
- Measuring response time
- Authentication checks
- Adding headers
- Error handling

## Middleware vs Dependencies
Middleware:
- Runs for every request
- Global behavior

Dependencies:
- Run per route
- Reusable logic for specific endpoints

## Real-world examples
- Log request method & URL
- Track API performance
- Block unauthorized requests
- Add security headers

## What I learned today
- How FastAPI handles request lifecycle
- What middleware is and why it is used
- Difference between middleware and dependencies
