from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Fake in-memory data
expenses = [
    {"id": 1, "category": "Food", "amount": 250},
    {"id": 2, "category": "Travel", "amount": 1200},
]

class Expense(BaseModel):
    category: str
    amount: float

# ---------------- GET ALL ----------------
@app.get("/expenses", status_code=status.HTTP_200_OK)
def get_expenses():
    return expenses

# ---------------- GET BY ID ----------------
@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    # Proper error response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )

# ---------------- CREATE EXPENSE ----------------
@app.post("/expenses", status_code=status.HTTP_201_CREATED)
def create_expense(expense: Expense):
    new_expense = {
        "id": len(expenses) + 1,
        "category": expense.category,
        "amount": expense.amount
    }
    expenses.append(new_expense)
    return new_expense
