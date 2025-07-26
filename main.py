import os
from organizador import contar_extensiones, mostrar_resumen, organizar_archivos
from UI import seleccionar_ruta, preguntar_si_ordenar

def main():
    ruta = seleccionar_ruta()
    if not ruta:
        print("No seleccionaste ninguna carpeta.")
        return

    if not os.path.exists(ruta):
        print("Esa ruta no existe.")
        return

    contador = contar_extensiones(ruta)
    mostrar_resumen(contador)

    if not preguntar_si_ordenar():
        print("Operación cancelada.")
        return

    organizar_archivos(ruta)
    print("\nArchivos organizados con éxito.")

if __name__ == "__main__":
    main()
