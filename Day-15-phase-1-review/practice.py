from fastapi import FastAPI, APIRouter, HTTPException, Depends, Query, Request
from pydantic import BaseModel
from typing import List, Optional
import time
import logging

# ---------------- LOGGING ----------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Phase-1 Review API")

# ---------------- MIDDLEWARE ----------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logger.info(
        f"{request.method} {request.url.path} "
        f"Status={response.status_code} "
        f"Time={duration:.4f}s"
    )
    return response

# ---------------- DEPENDENCY ----------------
def get_current_user(token: str = Query(...)):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return "user"

# ---------------- MODELS ----------------
class JobCreate(BaseModel):
    company: str
    role: str
    status: Optional[str] = "Applied"

class JobResponse(JobCreate):
    id: int

# ---------------- ROUTER ----------------
router = APIRouter(prefix="/api/v1/jobs", tags=["Jobs"])

fake_db: List[dict] = []

@router.post("/", response_model=JobResponse, status_code=201)
def create_job(
    job: JobCreate,
    user: str = Depends(get_current_user)
):
    new_job = {
        "id": len(fake_db) + 1,
        **job.dict()
    }
    fake_db.append(new_job)
    return new_job

@router.get("/", response_model=List[JobResponse])
def list_jobs(
    skip: int = 0,
    limit: int = Query(10, le=50)
):
    return fake_db[skip: skip + limit]

app.include_router(router)

@app.get("/")
def root():
    return {"message": "FastAPI Phase-1 Complete"}
