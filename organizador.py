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

def organizar_archivos(ruta, extensiones_filtradas=None):
    archivos = os.listdir(ruta)
    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)

        if extension == "":
            continue

        ext_limpia = extension[1:].lower()

        if extensiones_filtradas and ext_limpia not in extensiones_filtradas:
            continue

        carpeta_destino = os.path.join(ruta, ext_limpia.upper())
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        origen = os.path.join(ruta, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        os.rename(origen, destino)

def resumen_a_texto(contador):
    if not contador:
        return "No se encontraron archivos en la carpeta seleccionada."
    texto = ""
    for ext, cantidad in contador.items():
        texto += f"  - .{ext}: {cantidad} archivos\n"
    return texto

