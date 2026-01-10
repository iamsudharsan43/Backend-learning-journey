from fastapi import APIRouter

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

jobs=[
        {"id": 1, "company": "Google", "status": "Applied"},
        {"id": 2, "company": "Amazon", "status": "Interview"}
    ]

@router.get("/")
def get_jobs():
    return [
        {"id": 1, "company": "Google", "status": "Applied"},
        {"id": 2, "company": "Amazon", "status": "Interview"}
    ]

@router.post("/")
def add_job(job: dict):
    return {
        "message": "Job application added",
        "job": job
    }

@router.get("/job/{job_id}")
def details(job_id:int):
    for search in jobs:
        if search["id"]==job_id:
            return {
                "job": search
            }