from contextlib import asynccontextmanager
from fastapi import FastAPI
from app_insights_logger import log_custom_event  # your custom logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup logic ---
    log_custom_event()   # send a test log/trace when app starts
    yield
    # --- Shutdown logic ---
    # (optional) clean up resources here if needed

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/greet")
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}

