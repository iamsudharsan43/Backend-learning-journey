from fastapi import FastAPI

app = FastAPI()

# ---------------- GET ROUTE ----------------
@app.get("/")
def home():
    return {
        "message": "Welcome to Expense Tracker API"
    }

# ---------------- GET ROUTE ----------------
@app.get("/expenses")
def get_expenses():
    return {
        "expenses": [
            {"category": "Food", "amount": 500},
            {"category": "Travel", "amount": 1200}
        ]
    }

# ---------------- POST ROUTE ----------------
@app.post("/expenses")
def add_expense(expense: dict):
    return {
        "message": "Expense received",
        "data": expense
    }
