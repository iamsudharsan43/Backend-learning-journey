from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # One user → many jobs
    jobs = relationship("Job", back_populates="user")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    # Each job → one user
    user = relationship("User", back_populates="jobs")
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # One user → many jobs
    jobs = relationship("Job", back_populates="user")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    # Each job → one user
    user = relationship("User", back_populates="jobs")
