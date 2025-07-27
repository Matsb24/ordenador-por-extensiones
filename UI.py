import tkinter as tk
from tkinter import filedialog, messagebox
import os
from organizador import contar_extensiones,  organizar_archivos, resumen_a_texto
from PIL import Image, ImageTk

class OrganizadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Organizador de Archivos")
        master.geometry("500x320")
        
# Cargar la imagen de fondo
        fondo_img = Image.open("img/fondo.jpg") 
        fondo_img = fondo_img.resize((500, 320))
        fondo_tk = ImageTk.PhotoImage(fondo_img)
        self.fondo_label = tk.Label(master, image=fondo_tk)
        self.fondo_label.image = fondo_tk
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configurar el grid
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

        self.ruta = ""
#titulo
        self.label = tk.Label(master, text="Organizador de Archivos", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)
#Area de texto para mostrar el analisis
        self.AreaTexto = tk.Text(master, height=10, width=57)
        self.AreaTexto.grid(row=1, column=0, columnspan=3, pady=5, padx=20, sticky="we")
        self.AreaTexto.config(state=tk.DISABLED)
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
        contador = contar_extensiones(self.ruta)
        resumen = resumen_a_texto(contador)
        self.AreaTexto.config(state=tk.NORMAL)
        self.AreaTexto.delete(1.0, tk.END)
        self.AreaTexto.insert(tk.END, resumen)
        self.AreaTexto.config(state=tk.DISABLED)
        self.btn_ordenar.config(state=tk.NORMAL)

    def ordenar_archivos(self):
        if not self.ruta:
            messagebox.showerror("Error", "Primero debes seleccionar una carpeta.")
            return
        organizar_archivos(self.ruta)
        messagebox.showinfo("Éxito", "Archivos Ordenados")

def main():
    root = tk.Tk()
    root.resizable(False, False) 
    app = OrganizadorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
