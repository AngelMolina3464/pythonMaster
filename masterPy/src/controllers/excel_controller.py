from pathlib import Path
from src.models.productos_model import Producto
import pandas as pd
from typing import List
import os


ruta_script = os.path.abspath(__file__)
ruta_completa = Path(ruta_script)
ruta_raiz = ruta_completa.parents[2]
ruta_raiz= os.path.join(ruta_raiz, 'data')
ruta_fichero= os.path.join(ruta_raiz, 'productosBD.xlsx')
nombre_archivo = ruta_fichero
df = pd.read_excel(nombre_archivo)

def obtenerDatos (): 
    df = pd.read_excel(nombre_archivo)
    df.columns = df.columns.str.strip()
    productos: List[Producto] = [Producto(**fila) for fila in df.to_dict(orient='records')]
    productos_dict = [producto.model_dump() for producto in productos]
    return productos_dict    

def obtenerDato (idSearched): 
    df = pd.read_excel(nombre_archivo)
    df.columns = df.columns.str.strip()
    productos: List[Producto] = [Producto(**fila) for fila in df.to_dict(orient='records')]
    productos_dict = [producto.model_dump() for producto in productos]
    producto_encontrado = next((producto for producto in productos_dict if producto['id'] == idSearched), None)
    return producto_encontrado    


def crear_nuevo__producto (datos_entrada: dict): 
    df = pd.read_excel(nombre_archivo)
    df.columns = df.columns.str.strip()
    productos: List[Producto] = [Producto(**fila) for fila in df.to_dict(orient='records')]
    productos_dict = [producto.model_dump() for producto in productos]
    # Cuenta todos las filas
    counter = len(productos_dict)
    
    # Agregar Nueva Fila 
    for columna, valor in datos_entrada.items():
        df.at[counter + 1, columna] = valor
    df.to_excel(nombre_archivo, index=False)
    return {"producto Nuevo": "Agregado"} 