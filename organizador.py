import os    
import shutil  

# Función para obtener la extensión de un archivo
def obtener_extension(archivo):
    return archivo.split('.')[-1] if '.' in archivo else 'sin_extension'

# Función para contar archivos por extensión
def contar_extensiones(ruta):
    contador = {}
    for archivo in os.listdir(ruta): # Itera sobre los archivos en la ruta dada
        ruta_archivo = os.path.join(ruta, archivo) # Construye la ruta completa del archivo
        if os.path.isfile(ruta_archivo): # Verifica si es un archivo
            ext = obtener_extension(archivo) # Obtiene la extensión del archivo
            contador[ext] = contador.get(ext, 0) + 1 # Incrementa el contador para esa extensión
    return contador

# Función para mostrar el resumen de la cantidad de archivo por extensión
def mostrar_resumen(contador):
    print("\nResumen por tipo de archivo:")
    for ext, cantidad in contador.items(): # Itera sobre el diccionario de conteo
        print(f"  - .{ext}: {cantidad} archivos") # Muestra la extensión y la cantidad de archivos

# Función para organizar archivos en carpetas según su extensión
def organizar_archivos(ruta, extensiones_filtradas=None):
    archivos = os.listdir(ruta) 
    for archivo in archivos: # Itera sobre los archivos en la ruta dada
        nombre, extension = os.path.splitext(archivo) # Divide el nombre y la extensión

        if extension == "":
            continue

        ext_limpia = extension[1:].lower() # Limpia el punto y convierte a minúsculas

        if extensiones_filtradas and ext_limpia not in extensiones_filtradas:
            continue

        carpeta_destino = os.path.join(ruta, ext_limpia.upper()) # Carpeta basada en la extensión
        if not os.path.exists(carpeta_destino): # Crea la carpeta si no existe
            os.makedirs(carpeta_destino) 

        origen = os.path.join(ruta, archivo) # Ruta completa del archivo original
        destino = os.path.join(carpeta_destino, archivo) # Ruta completa del archivo destino
        os.rename(origen, destino) # Mueve el archivo a la carpeta correspondiente

# Función para generar un resumen en formato texto
def resumen_a_texto(contador):
    if not contador:
        return "No se encontraron archivos en la carpeta seleccionada."
    texto = ""
    for ext, cantidad in contador.items():
        texto += f"  - .{ext}: {cantidad} archivos\n"
    return texto

