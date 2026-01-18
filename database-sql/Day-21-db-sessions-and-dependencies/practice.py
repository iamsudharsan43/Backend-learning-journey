from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ---------------- DATABASE SETUP ----------------
DATABASE_URL = "sqlite:///jobs_api.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# ---------------- MODEL ----------------
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, nullable=False)

# ---------------- CREATE TABLE ----------------
Base.metadata.create_all(bind=engine)

# ---------------- FASTAPI APP ----------------
app = FastAPI(title="DB Session Dependency Demo")

# ---------------- DB DEPENDENCY ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- ROUTES ----------------
@app.post("/jobs")
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

@app.get("/jobs")
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()
