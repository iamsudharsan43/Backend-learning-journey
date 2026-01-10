from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/profile")
def get_profile():
    return {
        "name": "Sudharsan",
        "role": "Backend Developer",
        "experience": "Fresher"
    }
