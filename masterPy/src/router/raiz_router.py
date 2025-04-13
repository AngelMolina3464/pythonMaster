from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, FileResponse
import os

raiz_router = APIRouter()

path_root = os.path.join(os.path.dirname(__file__))
path_templetes = path_root.replace('src', "static")
path_templetes = path_templetes.replace("router", "templates")

@raiz_router.get("/", tags=["Inicio"])
def home (): 
    html_name = "index.html"
    html_file = f"{path_templetes}/{html_name}"
    return FileResponse (html_file)


@raiz_router.get("/rebuild", tags=["Inicio"])
def home (): 
    html_name = "abe.html"
    html_file = f"{path_templetes}/{html_name}"
    return FileResponse (html_file)


@raiz_router.get("/pasarela", tags=["Inicio"])
def home (): 
    html_name = "pasarela.html"
    html_file = f"{path_templetes}/{html_name}"
    return FileResponse (html_file)

@raiz_router.get("/tech", tags=["Inicio"])
def home (): 
    html_name = "tech.html"
    html_file = f"{path_templetes}/{html_name}"
    return FileResponse (html_file)

@raiz_router.get("/contacto", tags=["Inicio"])
def home (): 
    html_name = "contacto.html"
    html_file = f"{path_templetes}/{html_name}"
    return FileResponse (html_file)
