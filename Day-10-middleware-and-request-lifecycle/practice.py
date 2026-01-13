from fastapi import FastAPI, Request
import time

app = FastAPI(title="Middleware Demo API")

# ---------------- MIDDLEWARE ----------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Before request reaches route
    print(f"➡️ Incoming request: {request.method} {request.url.path}")

    response = await call_next(request)

    # After response is generated
    process_time = time.time() - start_time
    print(f"⬅️ Completed in {process_time:.4f} seconds")

    return response

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return {"message": "Middleware is working"}

@app.get("/jobs")
def get_jobs():
    time.sleep(0.5)  # simulate slow processing
    return [
        {"company": "Google", "status": "Applied"},
        {"company": "Amazon", "status": "Interview"}
    ]
