from fastapi import FastAPI, Request
import time
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Middleware Demo API")

class name_details(BaseModel):
    name:str
    age:int

details=[]

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

    print("The Code:",response.status_code)

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

@app.put("/name", response_model=List[name_details])
def deta(info:name_details):
    time.sleep(2.5)
    de={
        "id":len(details)+1,
        "name":info.name,
        "age":info.age
    }
    details.append(de)
    return details