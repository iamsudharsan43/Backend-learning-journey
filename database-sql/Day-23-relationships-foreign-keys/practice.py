from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Job

# ---------------- DATABASE ----------------
engine = create_engine("sqlite:///relationships.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

session = SessionLocal()

# ---------------- CREATE USER ----------------
user = User(name="Sudharsan")
session.add(user)
session.commit()

# ---------------- CREATE JOBS ----------------
job1 = Job(company="Google", role="Backend Engineer", user_id=user.id)
job2 = Job(company="Amazon", role="SDE", user_id=user.id)

session.add_all([job1, job2])
session.commit()

# ---------------- READ RELATIONSHIP ----------------
print("\n📌 User and their jobs")
db_user = session.query(User).first()

print("User:", db_user.name)
for job in db_user.jobs:
    print("-", job.company, job.role)

# ---------------- CLOSE ----------------
session.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Job

# ---------------- DATABASE ----------------
engine = create_engine("sqlite:///relationships.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

session = SessionLocal()

# ---------------- CREATE USER ----------------
user = User(name="Sudharsan")
session.add(user)
session.commit()

# ---------------- CREATE JOBS ----------------
job1 = Job(company="Google", role="Backend Engineer", user_id=user.id)
job2 = Job(company="Amazon", role="SDE", user_id=user.id)

session.add_all([job1, job2])
session.commit()

# ---------------- READ RELATIONSHIP ----------------
print("\n📌 User and their jobs")
db_user = session.query(User).first()

print("User:", db_user.name)
for job in db_user.jobs:
    print("-", job.company, job.role)

# ---------------- CLOSE ----------------
session.close()
