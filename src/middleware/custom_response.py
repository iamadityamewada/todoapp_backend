from typing import Any, Dict, List, Union

from fastapi.responses import JSONResponse, ORJSONResponse
from fastapi.encoders import jsonable_encoder


class HttpStatusCodes:
    STATUS_CODES: dict[int, str] = {
        200: "Ok",
        201: "Created",
        202: "Accepted",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
    }

    @classmethod
    def get_status_message(cls, status_code: int) -> str:
        return cls.STATUS_CODES.get(status_code, "Unknown Status Code")


def send_success(
    status_code: int = 200,
    message: str = "",
    content: Any = None,
    metadata: Any = None,
):
    default_msg = HttpStatusCodes.get_status_message(status_code)
    message = message or default_msg

    return ORJSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "message": message,
            "data": jsonable_encoder(content),
            "metadata": metadata,
        },
    )


def send_error(
    status_code: int = 500,
    message: str = "Internal Server Error",
    content: Union[Dict[str, Any], List[Any], str, None] = None,
):
    return JSONResponse(
        content={"status_code": status_code, "message": message, "data": content}
    )
