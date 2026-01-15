from fastapi import FastAPI, APIRouter

app = FastAPI(title="Versioned API Demo")

# ---------------- VERSION 1 ----------------
v1_router = APIRouter(prefix="/api/v1", tags=["v1"])

@v1_router.get("/jobs")
def get_jobs_v1():
    return [
        {"company": "Google", "status": "Applied"},
        {"company": "Amazon", "status": "Interview"}
    ]

# ---------------- VERSION 2 ----------------
v2_router = APIRouter(prefix="/api/v2", tags=["v2"])

@v2_router.get("/jobs")
def get_jobs_v2():
    return [
        {
            "company": "Google",
            "status": "Applied",
            "location": "Bangalore"
        },
        {
            "company": "Amazon",
            "status": "Interview",
            "location": "Hyderabad"
        }
    ]

# Register routers
app.include_router(v1_router)
app.include_router(v2_router)
