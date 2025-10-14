# comment
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/greet")
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}
