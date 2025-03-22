from helpers.cositas import booleanUse, persona, avanceCurso, booleanUseLamda
from helpers.excel.controller import  columna_seleccionada, respuesta, folder, ruta_archivo

print(columna_seleccionada)

if respuesta.status_code == 200:

    with open(ruta_archivo, 'wb') as archivo:
        archivo.write(respuesta.content)  
    print('Imagen descargada exitosamente.')
else:
    print(f'Error al descargar la imagen. Código de estado: {respuesta.status_code}')