import json
import os

def cargar_json(nombre_archivo):
    """Lee un archivo JSON y devuelve su contenido convertido en un objeto de Python (diccionario o lista)"""
    try:
        ruta_actual = os.path.dirname(__file__)
        ruta_archivo = os.path.join(ruta_actual, nombre_archivo)
        
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"Aviso: El archivo '{nombre_archivo}' no fue encontrado. Se iniciara vacio")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' tiene un formato JSON invalido")
        return []

def guardar_json(nombre_archivo, datos):
    """Recibe un objeto de Python (lista o diccionario) y lo guarda en formato JSON con sangria y codificacion UTF-8"""
    try:
        ruta_actual = os.path.dirname(__file__)
        ruta_archivo = os.path.join(ruta_actual, nombre_archivo)
        
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Archivo '{nombre_archivo}' guardado correctamente.")
    except Exception as e:
        print(f"Ocurrio un error al guardar el archivo '{nombre_archivo}': {e}")