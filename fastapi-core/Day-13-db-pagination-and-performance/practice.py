from fastapi import FastAPI, Query
from typing import List
from pydantic import BaseModel

app = FastAPI(title="DB Pagination Demo API")

# ---------------- MODEL ----------------
class Job(BaseModel):
    id: int
    company: str
    role: str

# Simulated database (pretend 1000 rows)
fake_db = [
    {"id": i, "company": f"Company-{i}", "role": "Backend Engineer"}
    for i in range(1, 101)
]

# ---------------- DB STYLE PAGINATION ----------------
@app.get("/jobs", response_model=List[Job])
def get_jobs(
    skip: int = Query(0, start=0),
    limit: int = Query(10, minimum=0, maximum=50)
):
    """
    Simulates:
    SELECT * FROM jobs LIMIT limit OFFSET skip
    """
    return fake_db[skip : skip + limit]
