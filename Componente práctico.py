# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Integrantes:
# Jhonier Alexander Maquilon Miranada 
# Luis Angel Savedra
# Tutor: Juan Pablo Arango Cardona

# importo ABC para crear clases abstractas
from abc import ABC, abstractmethod

# importo datetime para manejar fechas en logs
import datetime
# defino el archivo donde se guardarán los eventos del sistema
LOG_FILE = "logs_software_fj.txt"

# creo función para registrar eventos en el sistema
def log_event(msg):

    # obtengo la fecha y hora actual
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # abro el archivo de logs en modo escritura acumulativa
    with open(LOG_FILE, "a", encoding="utf-8") as f:

        # escribo el mensaje con la fecha
        f.write(f"[{time}] {msg}\n")

# excepción para errores de cliente
class ClienteError(Exception):
    pass

# excepción para errores de servicio
class ServicioError(Exception):
    pass

# excepción para errores de reserva
class ReservaError(Exception):
    pass