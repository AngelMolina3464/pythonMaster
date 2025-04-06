import os

# Fast Api Backend # 
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


# Routers # 
from src.router.productos_router  import productos_router
from src.router.usuarios_router import usuarios_router
from src.router.raiz_router import raiz_router

# MiddleWares # 
from src.utils.http_error import HTTPErrorHandler

path_root = os.path.join(os.path.dirname(__file__))
path_master = os.path.dirname(path_root)
path_templetes = os.path.join(path_master, "static")


app = FastAPI()

# Carga de Carpeta eStatica#
app.mount("/static", StaticFiles(directory=path_templetes), name="static")

app.add_middleware(HTTPErrorHandler)
app.include_router(router=productos_router)
app.include_router(router=usuarios_router)
app.include_router(router=raiz_router)

app.title = "Master Python"
app.version = "0.0.2"
 
