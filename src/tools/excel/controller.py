import pandas as pd
import requests
import os
import json

archivo_excel = 'db.xlsx'
folder = "imagenes"
df = pd.read_excel(archivo_excel)
columna_rutas = df['Rutas'].to_numpy()
columna_codigos = df["Codigos"].to_numpy()

## solo para probar el zip de las columnas
def runDev (): 
    for urlPaths, codeName in zip(columna_rutas, columna_codigos ): 
        print("Url: " ,urlPaths, "Codigos: ",codeName)

def run ():
    if not os.path.exists(folder):
            os.makedirs(folder)
        
    for urlPaths, codeName in zip(columna_rutas, columna_codigos ): 
            url_imagen = urlPaths
            
            try:
                respuesta = requests.get(url_imagen)
                
                if respuesta.status_code == 200:

                    nombre_archivo = os.path.basename(url_imagen)
                    ruta_archivo = os.path.join(folder, f"{codeName}.jpg")
                    
                    contador = 1
                    while os.path.exists(ruta_archivo):

                        ruta_archivo = os.path.join(folder, f"{os.path.splitext(nombre_archivo)[0]}_{contador}{os.path.splitext(nombre_archivo)[1]}")
                        contador += 1
                    
                    with open(ruta_archivo, 'wb') as archivo:
                        archivo.write(respuesta.content)
                        print(f"Item Integrado a la Carpeta: {nombre_archivo}")
                else:
                    print(f'Error al descargar la imagen: {url_imagen}. Código de estado: {respuesta.status_code}')
            
            except requests.exceptions.RequestException as e:
                print(f"Error al hacer la solicitud a {url_imagen}: {e}")
            except Exception as e:
                print(f"Error al guardar la imagen {url_imagen}: {e}")
        
    return ""


def responseJsonApiPokeDex (): 
    path = "podex.json"
    try: 
        with open(path, 'r',encoding='utf-8') as file:
          listadeObjetos  = json.load(file)
          return listadeObjetos  
      
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no fue encontrado.")
    except json.JSONDecodeError:
    # Error si el archivo no tiene un formato JSON válido
        print("Error: El archivo no tiene un formato JSON válido.")
    except Exception as e:
    # Captura cualquier otro error
        print(f"Ocurrió un error inesperado: {e}")
    
    