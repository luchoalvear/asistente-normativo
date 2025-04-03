
import os
import shutil

def limpiar_storage():
    carpeta = "./storage"
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            archivo_path = os.path.join(carpeta, archivo)
            if os.path.isfile(archivo_path):
                os.remove(archivo_path)
                print(f"Archivo eliminado: {archivo_path}")
            elif os.path.isdir(archivo_path):
                shutil.rmtree(archivo_path)
                print(f"Directorio eliminado: {archivo_path}")

if __name__ == "__main__":
    limpiar_storage()
