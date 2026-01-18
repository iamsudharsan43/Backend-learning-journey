from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------------- DATABASE SETUP ----------------
DATABASE_URL = "sqlite:///jobs_crud.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ---------------- MODEL ----------------
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, nullable=False)

# ---------------- CREATE TABLE ----------------
Base.metadata.create_all(bind=engine)

# ---------------- SESSION ----------------
session = SessionLocal()

# ---------------- CREATE ----------------
print("\n📌 Creating jobs")
job1 = Job(company="Google", role="Backend Engineer", status="Applied")
job2 = Job(company="Amazon", role="SDE", status="Interview")

session.add_all([job1, job2])
session.commit()

# ---------------- READ ----------------
print("\n📌 Reading all jobs")
jobs = session.query(Job).all()
for job in jobs:
    print(job.id, job.company, job.role, job.status)

# ---------------- UPDATE ----------------
print("\n📌 Updating job status (Google → Selected)")
job_to_update = session.query(Job).filter(Job.company == "Google").first()
if job_to_update:
    job_to_update.status = "Selected"
    session.commit()

# ---------------- DELETE ----------------
print("\n📌 Deleting Amazon job")
job_to_delete = session.query(Job).filter(Job.company == "Amazon").first()
if job_to_delete:
    session.delete(job_to_delete)
    session.commit()

# ---------------- FINAL STATE ----------------
print("\n📌 Final job table")
final_jobs = session.query(Job).all()
for job in final_jobs:
    print(job.id, job.company, job.role, job.status)

# ---------------- CLOSE SESSION ----------------
session.close()
