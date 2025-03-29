
from src.tools.cositas import avanceCursoFastAPI
from src.tools.data.programasDbs import programas, programasIng
from src.models.moviesModel import Movie
from src.models.timerModel import Timer

# Fast Api Backend # 
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import FastAPI, Body, Path

# Routers # 
from src.router.lenguajesRouter import lenguajes_router
from src.router.pokemonRouter import pokemon_router

# MiddleWares # 
## from src.utils.http_error import HTTPErrorHandler

app = FastAPI()

## app.add_middleware(HTTPErrorHandler)
app.include_router(router=lenguajes_router)
app.include_router(router=pokemon_router)

app.title = "Master Python"
app.version = "0.0.1"

@app.get("/", tags=["Inicio"])
def home (): 
    return {"pagina" : "Inicio ", "Python": "FastApi"}       


@app.put("/avance", tags=["Avance Curso"])
def get_avance (tiempo : Timer): 
    selected = {"LenguajeSeleccionado": avanceCursoFastAPI(tiempo.moduleNumber) }
    return selected   


@app.post("/programas", tags=["Programas"])
def post_programas (tipo: str, nombre: str, nivel: str): 
    addProgram = {"tipo": tipo, "nombre": nombre, "nivel": nivel  }
    programasIng.append(addProgram)
    return {"programa agregado": programasIng} 
   
@app.post("/pelicula", tags=["Peliculas"])
def post_pelicula (pelicula : Movie): 
    movies = []
    movies.append(pelicula.model_dump())
    return {"programa agregado": movies}    