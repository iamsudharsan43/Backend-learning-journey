from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------------- DATABASE SETUP ----------------
DATABASE_URL = "sqlite:///jobs_orm.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

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

# ---------------- SESSION ----------------
session = SessionLocal()

# ---------------- INSERT DATA ----------------
job1 = Job(company="Google", role="Backend Engineer", status="Applied")
job2 = Job(company="Amazon", role="SDE", status="Interview")

session.add(job1)
session.add(job2)
session.commit()

# ---------------- READ DATA ----------------
jobs = session.query(Job).all()

print("📌 Job Records (ORM):")
for job in jobs:
    print(job.id, job.company, job.role, job.status)

# ---------------- CLOSE SESSION -------------
# ---
session.close()
