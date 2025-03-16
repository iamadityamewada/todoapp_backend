from fastapi import APIRouter
from src.api.controllers.Task import task_router


router = APIRouter(prefix="/api/v1")


router.include_router(task_router, prefix="/task")

