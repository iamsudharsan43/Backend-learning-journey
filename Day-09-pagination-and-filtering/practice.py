from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Job Tracker API")

# ---------------- RESPONSE MODEL ----------------
class Job(BaseModel):
    id: int
    company: str
    role: str
    status: str

# Fake database
jobs = [
    {"id": 1, "company": "Google", "role": "Backend Intern", "status": "Applied"},
    {"id": 2, "company": "Amazon", "role": "SDE Intern", "status": "Interview"},
    {"id": 3, "company": "Microsoft", "role": "Backend Engineer", "status": "Applied"},
    {"id": 4, "company": "Netflix", "role": "API Developer", "status": "Rejected"},
    {"id": 5, "company": "Uber", "role": "Backend Engineer", "status": "Applied"},
]

# ---------------- GET JOBS WITH PAGINATION & FILTERING ----------------
@app.get("/jobs", response_model=List[Job])
def get_jobs(
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = None
):
    result = jobs

    # Filtering
    if status:
        result = [job for job in result if job["status"] == status]

    # Pagination
    return result[skip : skip + limit]
