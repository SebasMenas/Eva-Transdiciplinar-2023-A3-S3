import tkinter as tk
from tkinter import ttk

def create_excel_table():
    root = tk.Tk()
    root.title("Tabla Excel")

    # Crear el árbol
    tree = ttk.Treeview(root)

    # Definir las columnas
    tree["columns"] = ("Nombre", "Edad", "Género")

    # Ajustar las columnas
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Nombre", width=100)
    tree.column("Edad", width=50)
    tree.column("Género", width=100)

    # Encabezados de columna
    tree.heading("Nombre", text="Nombre")
    tree.heading("Edad", text="Edad")
    tree.heading("Género", text="Género")

    # Agregar datos a la tabla
    tree.insert("", tk.END, text="1", values=("Juan", 25, "Masculino"))
    tree.insert("", tk.END, text="2", values=("María", 30, "Femenino"))
    tree.insert("", tk.END, text="3", values=("Carlos", 35, "Masculino"))

    # Empacar el árbol
    tree.pack()

    root.mainloop()

# Ejecutar la función para crear la tabla
create_excel_table()
