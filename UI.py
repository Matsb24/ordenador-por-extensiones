import tkinter as tk
from tkinter import filedialog

def seleccionar_ruta():
    """
    Muestra una ventana emergente para seleccionar una carpeta.
    """
    root = tk.Tk()
    root.withdraw()
    ruta = filedialog.askdirectory(title="Selecciona una carpeta")
    return ruta

def preguntar_si_ordenar():
    """
    Muestra una ventana emergente con botones para preguntar si ordenar.
    Devuelve True si el usuario elige 'Sí', False si elige 'No' o cierra la ventana.
    """
    respuesta = {"valor": None}

    def elegir_si():
        respuesta["valor"] = True
        ventana.destroy()

    def elegir_no():
        respuesta["valor"] = False
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Confirmación")
    ventana.geometry("300x100")
    ventana.resizable(False, False)

    etiqueta = tk.Label(ventana, text="¿Quieres ordenar los archivos por extensión?", padx=10, pady=10)
    etiqueta.pack()

    botones = tk.Frame(ventana)
    botones.pack()

    btn_si = tk.Button(botones, text="Sí", width=10, command=elegir_si)
    btn_si.pack(side="left", padx=10)

    btn_no = tk.Button(botones, text="No", width=10, command=elegir_no)
    btn_no.pack(side="right", padx=10)

    ventana.mainloop()
    return respuesta["valor"]
