from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db
from .models import Base, Job

# ---------------- APP ----------------
app = FastAPI(title="Full CRUD API")

# ---------------- CREATE TABLES ---------------
Base.metadata.create_all(bind=engine)

# ---------------- CREATE ----------------
@app.post("/jobs", response_model=dict, status_code=201)
def create_job(
    company: str,
    role: str,
    status: str,
    db: Session = Depends(get_db)
):
    job = Job(company=company, role=role, status=status)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

# ---------------- READ ALL ----------------
@app.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

# ---------------- READ ONE ----------------
@app.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

# ---------------- UPDATE ----------------
@app.put("/jobs/{job_id}")
def update_job(
    job_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job.status = status
    db.commit()
    db.refresh(job)
    return job

# ---------------- DELETE ----------------
@app.delete("/jobs/{job_id}", status_code=204)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(job)
    db.commit()
    return
