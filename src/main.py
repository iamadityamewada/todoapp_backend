from src.router import router
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from src.middleware.exception_handler import validation_exception_handler
from src.models.Task import Base
from src.config.db import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Taskimise",
    version="1.0.0",
    docs_url="/docs",  # Custom path for Swagger documentation
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(router)

@app.exception_handler(RequestValidationError)
async def validation_exception(request: Request, exc: RequestValidationError):
    return validation_exception_handler(request, exc)

# Create data base
Base.metadata.create_all(bind=engine)

@app.get("/")
async def Main():
    return {"message": "Taskimise is Live"}