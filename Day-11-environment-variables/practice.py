from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "Default API"),
    debug=os.getenv("DEBUG")
)

@app.get("/")
def home():
    if os.getenv("DEBUG") == "True":
        return {
            "app_name": os.getenv("APP_NAME"),
            "debug": os.getenv("DEBUG"),
            "secret_key_exists": os.getenv("SECRET_KEY") is not None,
            "Environment":"development"
        }
    else:
        return{
            "app_name": os.getenv("APP_NAME"),
            "debug": os.getenv("DEBUG"),
            "secret_key_exists": os.getenv("SECRET_KEY") is not None,
            "Environment":"production"
        }