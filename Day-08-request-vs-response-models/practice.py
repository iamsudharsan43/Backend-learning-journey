from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Optional

app = FastAPI(title="Job Tracker API")

# ---------------- REQUEST MODEL ----------------
class JobCreate(BaseModel):
    company: str
    role: str
    status: Optional[str] = "Applied"
 
# ---------------- RESPONSE MODEL ----------------
class JobResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str

# Fake database
jobs = [
    {"id": 1, "company": "Google", "role": "Backend Intern", "status": "Applied"},
    {"id": 2, "company": "Amazon", "role": "SDE Intern", "status": "Interview"},
]

# ---------------- GET ALL JOBS ----------------
@app.get("/jobs", response_model=List[JobResponse])
def get_jobs():
    return jobs

# ---------------- CREATE JOB ----------------
@app.post("/jobs", response_model=JobResponse)
def create_job(job: JobCreate):
    new_job = {
        "id": len(jobs) + 1,
        "company": job.company,
        "role": job.role,
        "status": job.status
    }
    jobs.append(new_job)
    return new_job
