from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.tools.excel.controller import responseJsonApiPokeDex
pokemon_router = APIRouter()

@pokemon_router.get("/pokemon/", tags=["Pokedex"])
def get_pokemon (): 
    selected = responseJsonApiPokeDex()
    return JSONResponse(content=selected, status_code=200)  