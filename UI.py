import tkinter as tk
from tkinter import filedialog, messagebox
import os
from organizador import contar_extensiones, mostrar_resumen, organizar_archivos

class OrganizadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Organizador de Archivos")
        master.geometry("400x300")
        self.ruta = ""

        self.label = tk.Label(master, text="Organizador de Archivos por Extensión", font=("Arial", 14))
        self.label.pack(pady=10)

        self.texto = tk.Text(master, height=10, width=45)
        self.texto.pack(pady=5)
        self.texto.config(state=tk.DISABLED)
        
        self.btn_seleccionar = tk.Button(master, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        self.btn_seleccionar.pack(pady=5)

        self.btn_resumen = tk.Button(master, text="Analizar", command=self.ver_resumen)
        self.btn_resumen.pack(pady=5)
        self.btn_resumen.config(state=tk.DISABLED)

        self.btn_ordenar = tk.Button(master, text="Ordenar", command=self.ordenar_archivos)
        self.btn_ordenar.pack(pady=5)
        self.btn_ordenar.config(state=tk.DISABLED)

    def seleccionar_carpeta(self):
        ruta = filedialog.askdirectory(title="Selecciona una carpeta")
        if ruta:
            self.ruta = ruta
            messagebox.showinfo("Carpeta seleccionada", f"Ruta:\n{ruta}")
            self.btn_resumen.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Sin selección", "No seleccionaste ninguna carpeta.")

    def ver_resumen(self):
        if not self.ruta:
            messagebox.showerror("Error", "Primero debes seleccionar una carpeta.")
            return
        contador = contar_extensiones(self.ruta)
        resumen = mostrar_resumen(contador)
        self.texto.config(state=tk.NORMAL)
        self.texto.delete(1.0, tk.END)
        self.texto.insert(tk.END, resumen)
        self.texto.config(state=tk.DISABLED)
        self.btn_ordenar.config(state=tk.NORMAL)
        messagebox.showinfo("Resumen", resumen)

    def ordenar_archivos(self):
        if not self.ruta:
            messagebox.showerror("Error", "Primero debes seleccionar una carpeta.")
            return
        organizar_archivos(self.ruta)
        messagebox.showinfo("Éxito", "Archivos organizados con éxito.")

def main():
    root = tk.Tk()
    app = OrganizadorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
