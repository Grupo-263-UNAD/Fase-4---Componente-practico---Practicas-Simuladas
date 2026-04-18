# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Integrantes del grupo:
# -Jhonier Alexander Maquilon Miranada 
# -Luis Angel Savedra

# importar la biblioteca de tkinter para crear la interfaz gráfica
import tkinter as tk 
# importo loa funcion messagebox para mostrar mensajes emergentes
from tkinter import messagebox

# defino la funcion para mostrar el mensaje de bienvenida, recibe como parametro el nombre del software
def mostrar_mensaje(Software_FJ ):
    # utilizo la funcion para mostrar un mensaje emergente con el nombre del software
    messagebox.showinfo("Mensaje", f"¡Hola, {Software_FJ}! Bienvenido al componente práctico de Software FJ.")

# Creo la ventana principal de la apliacion y le asigno un titulo y un tamaño
ventana = tk.Tk()   
ventana.title("Componente Práctico - Software FJ")
ventana.geometry("300x200")