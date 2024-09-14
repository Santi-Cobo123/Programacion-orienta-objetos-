import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = campo_texto.get()  # Obtener el texto del campo
    if info:  # Verificar que no esté vacío
        lista_datos.insert(tk.END, info)  # Agregar a la lista
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese información.")  # Mensaje de advertencia

# Función para limpiar el campo de texto y la lista
def limpiar_info():
    campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    lista_datos.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")  # Título de la ventana

# Crear componentes
etiqueta = tk.Label(ventana, text="Ingrese información:")  # Etiqueta
etiqueta.pack(pady=10)  # Añadir la etiqueta a la ventana

campo_texto = tk.Entry(ventana, width=40)  # Campo de texto
campo_texto.pack(pady=5)  # Añadir el campo a la ventana

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)  # Botón "Agregar"
boton_agregar.pack(pady=5)  # Añadir el botón a la ventana

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)  # Botón "Limpiar"
boton_limpiar.pack(pady=5)  # Añadir el botón a la ventana

lista_datos = tk.Listbox(ventana, width=50, height=10)  # Lista para mostrar datos
lista_datos.pack(pady=10)  # Añadir la lista a la ventana

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

