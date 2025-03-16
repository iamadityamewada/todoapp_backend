from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    missing_fields = [err["loc"][-1] for err in errors if err["type"] == "missing"]

    return JSONResponse(
        status_code=400,
        content={
            "error": True,
            "message": "All Fields required",
            "missingField": missing_fields,
        },
    )
