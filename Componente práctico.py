# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Integrantes:
# -Jhonier Alexander Maquilon Miranada 
# -L Luis Angel Savedra

# importar la biblioteca de tkinter para crear la interfaz gráfica
import tkinter as tk 
# importo loa funcion messagebox para mostrar mensajes emergentes
from tkinter import messagebox

# defino la funcion para mostrar el mensaje de bienvenida, recibe como parametro el nombre del software
def mostrar_mensaje(Software_FJ ):
    messagebox.showinfo("Mensaje", f"¡Hola, {Software_FJ}! Bienvenido al componente práctico de Software FJ.")

# Crear la ventana principal
ventana = tk.Tk()   
ventana.title("Componente Práctico - Software FJ")
ventana.geometry("300x200")