from fastapi import FastAPI, Request
import logging
import time

# ---------------- LOGGING CONFIG ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Logging Demo API")

# ---------------- MIDDLEWARE ----------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(f"Incoming request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}")
        raise

    process_time = time.time() - start_time
    logger.info(
        f"Completed {request.method} {request.url.path} "
        f"Status={response.status_code} "
        f"Time={process_time:.4f}s"
    )

    return response

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    logger.debug("Home endpoint accessed")
    return {"message": "Logging is active"}

@app.get("/jobs")
def get_jobs():
    logger.info("Fetching jobs list")
    time.sleep(0.4)
    return [
        {"company": "Google", "status": "Applied"},
        {"company": "Amazon", "status": "Interview"}
    ]

@app.get("/error")
def error_demo():
    logger.warning("Error endpoint was called")
    raise ValueError("This is a demo error")
