from sqlmodel import SQLModel, Field


class Producto(SQLModel): 
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: str
    precio: float
    stock: int = Field(default=0)
    categoria: str

"""
Modelo antiguo de productos

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)
    stock = Column(Integer, default=0)
    categoria = Column(String)

"""