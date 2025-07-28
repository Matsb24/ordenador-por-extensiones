import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
from organizador import contar_extensiones, mostrar_resumen, organizar_archivos, resumen_a_texto

class OrganizadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Organizador de Archivos")
        master.geometry("500x320")
        
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

        self.ruta = ""
#titulo
        self.label = tk.Label(master, text="Organizador de Archivos", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)
# Contenedor con scroll para los checkboxes
        self.canvas_frame = tk.Frame(master, bd=2, relief="groove", bg="white")
        self.canvas_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=5, sticky="we")

        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(1, weight=0)

        self.canvas = tk.Canvas(self.canvas_frame, height=150, width=420, bg="white")
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview, width=18)  # ancho scrollbar

        self.scrollable_frame = tk.Frame(self.canvas, bg="white", width=420)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.extension_vars = {}
        
#Seleccionar carpeta
        self.btn_seleccionar = tk.Button(master, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        self.btn_seleccionar.grid(row=2, column=0, padx=(20, 5), pady=(15, 5), sticky="w")
#Mostrar ruta de la carpeta
        self.TextoRuta = tk.Text(master, height=1, width=40)
        self.TextoRuta.grid(row=2, column=1, columnspan=2, padx=(0, 20), pady=(15, 5), sticky="we")
        self.TextoRuta.config(state=tk.DISABLED)
#Botones para analizar
        self.btn_resumen = tk.Button(master, text="Analizar", command=self.ver_resumen)
        self.btn_resumen.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.btn_resumen.config(state=tk.DISABLED)
#Boton por si quieres ordenar
        self.btn_ordenar = tk.Button(master, text="Ordenar", command=self.ordenar_archivos)
        self.btn_ordenar.grid(row=3, column=1, columnspan=2, padx=5, pady=10)
        self.btn_ordenar.config(state=tk.DISABLED)

    def seleccionar_carpeta(self):
        ruta = filedialog.askdirectory(title="Selecciona una carpeta")
        if ruta:
            self.ruta = ruta
            self.TextoRuta.config(state=tk.NORMAL)
            self.TextoRuta.delete(1.0, tk.END)
            self.TextoRuta.insert(tk.END, ruta)
            self.TextoRuta.config(state=tk.DISABLED)
            self.btn_resumen.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Sin selección", "No seleccionaste ninguna carpeta.")

    def ver_resumen(self):
        if not self.ruta:
            messagebox.showerror("Error", "Primero debes seleccionar una carpeta.")
            return
        
        # Limpia checkboxes anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.extension_vars.clear()

        contador = contar_extensiones(self.ruta)
        if not contador:
            messagebox.showinfo("Vacío", "No se encontraron archivos para organizar.")
            return

        fila = 0
        for ext, cantidad in contador.items():
            var = tk.BooleanVar(value=True)
            chk = tk.Checkbutton(self.scrollable_frame, text=f"{ext} ({cantidad} archivo(s))", variable=var, bg="white", anchor="w", width=30, padx=8, pady=3)
            chk.grid(row=fila, column=0, sticky="we", padx=5, pady=2)
            self.extension_vars[ext] = var
            fila += 1

        self.btn_ordenar.config(state=tk.NORMAL)

    def ordenar_archivos(self):
        if not self.ruta:
            messagebox.showerror("Error", "Primero debes seleccionar una carpeta.")
            return

# Recolecta extensiones seleccionadas
        extensiones_a_organizar = [ext for ext, var in self.extension_vars.items() if var.get()]
        if not extensiones_a_organizar:
            messagebox.showwarning("Sin selección", "Debes seleccionar al menos una extensión para organizar.")
            return

        organizar_archivos(self.ruta, extensiones_a_organizar)
        messagebox.showinfo("Éxito", "Archivos ordenados.")

def obtener_ruta_icono(nombre_archivo):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "img", nombre_archivo)
    return os.path.join("img", nombre_archivo)

def main():
    root = tk.Tk()
    root.iconbitmap(obtener_ruta_icono("Icono.ico"))
    root.resizable(False, False) 
    app = OrganizadorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()