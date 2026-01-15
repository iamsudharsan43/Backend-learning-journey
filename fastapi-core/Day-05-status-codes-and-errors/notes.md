# Day 5 – HTTP Status Codes & Error Handling

## Why status codes matter
HTTP status codes tell the client whether a request succeeded or failed.
Frontend applications rely on status codes to decide what to do next.

## Common HTTP Status Codes

### Success
- 200 OK → Request successful
- 201 Created → Resource created successfully

### Client Errors
- 400 Bad Request → Invalid input
- 401 Unauthorized → Not logged in
- 403 Forbidden → No permission
- 404 Not Found → Resource does not exist
- 422 Unprocessable Entity → Validation error (from Pydantic)

### Server Errors
- 500 Internal Server Error → Backend failure

## Why backend developers must use correct codes
- Frontend logic depends on it
- APIs become predictable and clean
- Easier debugging and monitoring

## Error handling in FastAPI
FastAPI provides HTTPException to:
- Stop execution
- Return a proper status code
- Send a clear error message

## What I learned today
- Meaning of important HTTP status codes
- How to raise errors in FastAPI
- How to build professional API responses
