from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---------------- Pydantic Model ----------------
class Expense(BaseModel):
    category: str
    amount: float

# ---------------- GET ----------------
@app.get("/")
def home():
    return {"message": "Pydantic validation example"}

# ---------------- POST ----------------
@app.post("/expenses")
def add_expense(expense: Expense):
    return {
        "status": "success",
        "expense": expense
    }
