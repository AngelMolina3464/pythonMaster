from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request
import time

class HTTPErrorHandler (BaseHTTPMiddleware): 
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        print({"Ejecucion del Midleware 404": start_time})
        return response