from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request

class HTTPErrorHandler (BaseHTTPMiddleware): 
    def __init__(self, app: FastAPI, ) -> None:
        super().__init__(app)

async def dispatch(self, request: Request, call_next)-> Response : 
    try: 
        return await  call_next(request)
    except Exception as e: 
        content = f"Exc: {str(e)}"

        return JSONResponse(content=content, 
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)