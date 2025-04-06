
from fastapi.responses import JSONResponse
from src.tools.programasDbs import programas, programasTop
from fastapi import APIRouter

lenguajes_router = APIRouter()

@lenguajes_router.get("/lenguajes", tags=["Lenguaje"])
def get_lenguajes (): 
    return JSONResponse(content=programas)       

@lenguajes_router.get("/lenguajes/{id}", tags=["Lenguaje"])
def get_lenguaje (id : int): 
    selected = {"LenguajeSeleccionado": programasTop[id] }
    return JSONResponse(content=selected)      

@lenguajes_router.get("/lenguajeModulo/", tags=["Lenguaje"])
def get_lenguajeModulo (modulo : str): 
    selected = {"Nivel de Lenguaje": programas[modulo] }
    return JSONResponse(content=selected)      
