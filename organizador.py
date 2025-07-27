import os      # Módulo para interactuar con el sistema de archivos
import shutil  # Módulo para mover y copiar archivos

def obtener_extension(archivo):
    """
    Obtiene la extensión de un archivo.
    Si el archivo no tiene extensión, devuelve 'sin_extension'.
    """
    return archivo.split('.')[-1] if '.' in archivo else 'sin_extension'

def contar_extensiones(ruta):
    """
    Cuenta cuántos archivos hay de cada extensión en la carpeta dada.
    Devuelve un diccionario con la extensión como clave y la cantidad como valor.
    """
    contador = {}
    for archivo in os.listdir(ruta):  # Recorre todos los elementos en la carpeta
        ruta_archivo = os.path.join(ruta, archivo)  # Obtiene la ruta completa
        if os.path.isfile(ruta_archivo):  # Solo cuenta archivos, no carpetas
            ext = obtener_extension(archivo) #Extrae la extensión del archivo
            contador[ext] = contador.get(ext, 0) + 1  # Suma uno al contador de esa extensión
    return contador

def mostrar_resumen(contador):
    """
    Muestra por pantalla un resumen de cuántos archivos hay por cada extensión.
    """
    print("\nResumen por tipo de archivo:")
    for ext, cantidad in contador.items():
        print(f"  - .{ext}: {cantidad} archivos")

def organizar_archivos(ruta):
    """
    Mueve los archivos de la carpeta a subcarpetas según su extensión.
    Crea la carpeta si no existe.
    """
    for archivo in os.listdir(ruta): #Recorre todos los elementos en la carpeta
        ruta_archivo = os.path.join(ruta, archivo) #Une el nombre de la ruta con el nombre del archivo para obtener la ruta del archivo
        if os.path.isfile(ruta_archivo): # Verifica que sea un archivo (no una carpeta)
            ext = obtener_extension(archivo) #obtiene la extensión del archivo
            carpeta_destino = os.path.join(ruta, ext.upper())  # Prepara el nombre de la carpeta destino, siendo la extensión en mayúsculas
            os.makedirs(carpeta_destino, exist_ok=True)        # Crea la carpeta si no existe
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))  # Mueve el archivo

def resumen_a_texto(contador):
    if not contador:
        return "No se encontraron archivos en la carpeta seleccionada."
    texto = ""
    for ext, cantidad in contador.items():
        texto += f"  - .{ext}: {cantidad} archivos\n"
    return texto

