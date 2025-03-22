
def funcion_modulo2(stringDatum ):
    return str(stringDatum).capitalize()

def booleanUse (digit): 
    return  digit <= 0

def booleanUseLamda (digit01, digit02): 
   return lambda x = digit01, y =digit02:  x + y 


persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "correo": "juan@example.com"
}


def avanceCurso(horas , minutos): 
    duracionTotal = {
    "horas": 7,
    "minutos": 50,
    }
    
    tiempoTranscurrido = horas * 60 + minutos
    tiempoTotal = duracionTotal["horas"]*60 + duracionTotal["minutos"]
    relacion = (tiempoTranscurrido / tiempoTotal)*100
    return f"% {round(relacion, 2)}"