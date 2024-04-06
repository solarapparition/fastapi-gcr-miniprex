"""Minimal API."""

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Hello(BaseModel):
    """Request structure for hello world function."""

    message: str


def hello_world() -> str:
    """Hello World function."""
    return "Hello, World!"


app = FastAPI(title="Deploy FastAPI App")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.post(
    "/api/hello", summary="Hello world function.", tags=["hello"], response_model=Hello
)
async def hello():
    """Hello world function."""
    return Hello(message=hello_world())

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=7860)

# To test:
# python main.py
# curl -X POST http://127.0.0.1:7860/api/hello
