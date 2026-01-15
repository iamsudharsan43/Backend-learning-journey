# Day 8 – Request Models vs Response Models

## What is a Request Model?
A request model defines:
- What data the client is allowed to send
- Required and optional fields
- Data types

It protects the backend from invalid or unwanted input.

## What is a Response Model?
A response model defines:
- What data the backend sends back
- Which fields are exposed to the client
- How the output is structured

It protects internal data from being leaked.

## Why we should separate them
In real applications:
- Input data ≠ Output data
- Backend may store more data than it returns
- Sensitive fields should not be exposed

Example:
- Client sends: company, role
- Backend stores: id, timestamps
- Client receives: id, company, role

## How FastAPI helps
FastAPI allows:
- Request validation using Pydantic models
- Response shaping using response_model

## Why this matters in real jobs
- Clean API contracts
- Better security
- Easier frontend integration
- Interviewers expect this knowledge

## What I learned today
- Difference between request and response models
- Why separating them is important
- How FastAPI controls API input and output
