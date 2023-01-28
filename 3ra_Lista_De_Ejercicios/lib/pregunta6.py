import sys
import os

def imprimirNombreDelArchivoEnEjecucion():
    print(f"\nEl nombre del archivo (y no ruta) en ejecucion es: {os.path.basename(sys.argv[0])}")

