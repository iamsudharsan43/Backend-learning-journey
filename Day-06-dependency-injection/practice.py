from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# ---------------- DEPENDENCY ----------------
def get_current_user():
    # Simulating authentication logic
    user = "Sudharsan"  # pretend this came from a token

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    return user

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return {"message": "Public endpoint"}

@app.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {
        "message": "Protected endpoint",
        "user": current_user
    }
