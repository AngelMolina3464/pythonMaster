from helpers.cositas import avanceCurso
from helpers.excel.controller import  run, runDev
from fastapi import FastAPI
from helpers.data.programasDbs import programas, programasTop, programasIng

## run()

app = FastAPI()

app.title = "Master Python"
app.version = "0.0.1"

@app.get("/", tags=["Inicio"])
def home (): 
    return {"pagina" : "Inicio ", "Python": "FastApi"}       

@app.get("/lenguajes", tags=["Lenguaje"])
def get_lenguajes (): 
    return programas      

@app.get("/lenguajes/{id}", tags=["Lenguaje"])
def get_lenguaje (id : int): 
    selected = {"LenguajeSeleccionado": programasTop[id] }
    return selected      

@app.get("/lenguajeModulo/", tags=["Lenguaje"])
def get_lenguajeModulo (modulo : str): 
    selected = {"Nivel de Lenguaje": programas[modulo] }
    return selected      

@app.post("/programas", tags=["Programas"])
def post_programas (tipo: str, nombre: str, nivel: str): 
    addProgram = {"tipo": tipo, "nombre": nombre, "nivel": nivel  }
    programasIng.append(addProgram)
    return {"programa agregado": programasIng}    