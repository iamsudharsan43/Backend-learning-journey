from fastapi import FastAPI
from routes import jobs, users

app = FastAPI(title="Job Application Tracker API")

app.include_router(jobs.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}
