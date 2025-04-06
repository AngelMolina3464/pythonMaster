from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

# Model #
from src.models.usuario_model import Usuario

# Controllers # 

# Depends
from src.dependencies.productos_depends import Session_depends
from src.database.config import get_db

usuarios_router = APIRouter()

@usuarios_router.get("/usuarios", tags=["Usuarios"])
def obtener_usuarios(db : Session = Depends (get_db)):         
        # Forma Antigua #
    """
        response  = db.query(Usuario).all()
    """  
        # Forma Nueva #
    stmt = select(Usuario)
    result = db.exec(stmt)  
    response = result.all() 
    return response
      

@usuarios_router.post("/usuario", tags=["Usuarios"])
def crear_usuario(usuario : Usuario , db : Session = Depends (get_db)): 
    try:            
        db.add(usuario)
        db.commit()  
        db.refresh(usuario)  
        return usuario
    except Exception as e: 
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")
    
@usuarios_router.put("/usuario/{usuario_id}", tags=["Usuarios"])
def actualizar_usuario (usuario_id : int, usuario : Usuario, db: Session = Depends(get_db)): 
    try: 
        db_usuario = db.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
        if db_usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        db_usuario.nombre = usuario.nombre
        db_usuario.email = usuario.email
        
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        
        return db_usuario
    except Exception as e : 
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(e)}")
    
@usuarios_router.delete("/usuario/{usuario_id}", tags=["Usuarios"])
def eliminar_usuario (usuario_id : int, db: Session = Depends(get_db)):
    try:

        db_usuario = db.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
        if db_usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        db.delete(db_usuario)
        db.commit()

        return {"detail": "Usuario eliminado exitosamente"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {str(e)}")