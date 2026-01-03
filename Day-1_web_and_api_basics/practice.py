from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Backend API is running"
    }

@app.get("/about")
def about():
    return {
        "purpose": "Learning backend development with FastAPI"
    }
