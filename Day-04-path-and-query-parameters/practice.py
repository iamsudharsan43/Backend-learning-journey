from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Fake in-memory data (temporary)
expenses = [
    {"id": 1, "category": "Food", "amount": 250},
    {"id": 2, "category": "Travel", "amount": 1200},
    {"id": 3, "category": "Food", "amount": 500},
]

# ---------------- GET ALL EXPENSES ----------------
@app.get("/expenses")
def get_expenses(category: Optional[str] = None):
    if category:
        return [e for e in expenses if e["category"] == category]
    return expenses

# ---------------- GET EXPENSE BY ID ----------------
@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense
    return {"error": "Expense not found"}
