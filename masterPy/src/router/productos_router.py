from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

# Model #
from src.models.productos_model import Producto

# Controllers # 

# Depends
from src.dependencies.productos_depends import Session_depends

productos_router = APIRouter()

@productos_router.get("/productos", tags=["Productos"])
def obtener_productos(): 
    return  JSONResponse(content = {"1":"0"}, status_code=200)

@productos_router.post("/productos", tags=["Productos"])
def crear_producto(producto: Producto , session : Session_depends ): 
    db_producto = Producto.model_validate(producto)
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)  
    response = {"Producto Agregado": db_producto}
    return JSONResponse(content=response, status_code=200)

@productos_router.put("/productos", tags=["Productos"])
def editar_productos():   
    response = {"productos": "Metodo GET"}
    return JSONResponse(content=response, status_code=200)

@productos_router.delete("/productos", tags=["Productos"])
def eliminar_productos():   
    response = {"productos": "Metodo GET"}
    return JSONResponse(content=response, status_code=200)