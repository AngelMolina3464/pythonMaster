import pandas as pd
import requests
import os

archivo_excel = 'db.xlsx'
folder = "imagenes"

if not os.path.exists(folder):
    os.makedirs(folder)

ruta_archivo = os.path.join(folder, 'imagen_descargada.jpg')
df = pd.read_excel(archivo_excel)
columna_seleccionada = df['Rutas'].to_numpy()

url_imagen = 'https://www.megaaudio.com.mx/cdn/shop/files/85A6N_01.jpg?width=500'  
respuesta = requests.get(url_imagen)
