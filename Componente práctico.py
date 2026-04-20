# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Programacion de Software FJ
# Integrantes del grupo:
# -Jhonier Alexander Maquilon Miranada 
# -Luis Angel Savedra





# importar la biblioteca de tkinter para crear la interfaz gráfica
import tkinter as tk 
# importo loa funcion messagebox para mostrar mensajes emergentes
from tkinter import messagebox
# importo la biblioteca datetime para trabajar con fechas y horas
from abc import ABC, abstractmethod
# implemento la clase abstracta Software_FJ con un metodo abstracto mostrar_mensaje
import datetime


# defino la funcion para mostrar el mensaje de bienvenida, recibe como parametro el nombre del software
def mostrar_mensaje(Software_FJ ):
    # utilizo la funcion para mostrar un mensaje emergente con el nombre del software
    messagebox.showinfo("Mensaje", f"¡Hola, {Software_FJ}! Bienvenido al componente práctico de Software FJ.")

# Creo la ventana principal de la apliacion y le asigno un titulo y un tamaño
ventana = tk.Tk()   
# asigno el titulo de la ventana y su tamaño
ventana.title("Componente Práctico - Software FJ")
# asigno el tamaño de la ventana
ventana.geometry("300x200")  
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def calcular_costo(self, impuesto=0.19):
        return self.servicio.calcular_costo(self.duracion) * (1 + impuesto)

    def calcular_costo(self, impuesto=0.19, descuento=0):  # método sobrecargado
        base = self.servicio.calcular_costo(self.duracion)
        return base * (1 + impuesto) * (1 - descuento)

    def confirmar(self):
        try:
            self.cliente.validar()
            if self.duracion <= 0:
                raise ErrorReserva("Duración inválida para reserva")
            self.estado = "confirmada"
            logging.info(f"Reserva confirmada para {self.cliente._Cliente__nombre}")
        except ErrorReserva as e:
            logging.error(f"Error en confirmación: {e}")
            raise

class Spa(Servicio):
    def calcular_costo(self, duracion):
        if duracion < 45: raise ErrorReserva("Mínimo 45 min en Spa")
        return duracion * 65000

class Yoga(Servicio):
    def calcular_costo(self, duracion):
        return duracion * 35000

# Simulación de operaciones (continuación)
try:
    c2 = Cliente("Maria Lopez", "maria@gmail.com", "3001234567")
    c2.validar()
    r1 = Reserva(c2, Spa(), 60)
    r1.confirmar()
    print("Reserva confirmada correctamente")
except Exception as e:
    logging.error(f"Error grave controlado: {e}")
    print("Aplicación sigue estable")
