# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Integrantes:
# Jhonier Alexander Maquilon Miranada 
# Luis Angel Savedra Linares
# Tutor: Juan Pablo Arango Cardona
# Trabajo colaborativo.
# 12 de  mayo de 2026

# importo ABC para crear clases abstractas y abstractmethod para definir métodos que deben ser implementados por las clases que hereden de la clase base
from abc import ABC, abstractmethod

# importo datetime para manejar fechas en logs y facilitar el seguimiento de eventos en el sistema
import datetime
# defino el archivo donde se guardarán los eventos del sistema 
LOG_FILE = "logs_software_fj.txt"

# creo función para registrar eventos en el sistema con formato de fecha y hora para facilitar el seguimiento de acciones y errores
def log_event(msg):

    # obtengo la fecha y hora actual
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # abro el archivo de logs en modo escritura acumulativa y con codificación utf-8 para evitar problemas con caracteres especiales
    with open(LOG_FILE, "a", encoding="utf-8") as f:

        # escribo el mensaje con la fecha y hora en el formato definido
        f.write(f"[{time}] {msg}\n")
        
        

# implemento excepción para errores de cliente
class ClienteError(Exception):
    pass

# implemento excepción para errores de servicio
class ReservaError(Exception):
    pass

class Entidad(ABC):

    # constructor general con id
    def __init__(self, id):
        self.id = id

    # método obligatorio
    @abstractmethod
    def descripcion(self):
        pass
    
# implemento clase Cliente que hereda de Entidad
class Cliente(Entidad):

    # constructor del cliente con validaciones y manejo de errores
    def __init__(self, nombre, documento):
        # identtificador del cliente se asigna al documento para garantizar unicidad y facilitar búsquedas
        super().__init__(documento)  

        try:
            # valido nombre mínimo 3 caracteres
            if not nombre or len(nombre) < 3:
                raise ClienteError("Nombre inválido")

            # valido que documento sea numérico y no esté vacío
            if not str(documento).isdigit():
                raise ClienteError("Documento inválido")

            # guardo nombre atributo privado
            self.__nombre = nombre

            # guardo documento atributo privado
            self.__documento = documento

            # registro la creación del cliente en logs
            log_event(f"Cliente creado: {nombre}")

        except Exception as e:
            # registro error en logs si ocurre una excepción
            log_event(f"Error cliente: {e}")

            # relanzo error para que pueda ser manejado por quien instancie la clase
            raise ClienteError("Error al crear cliente") from e

    # obtengo nombre del cliente con método getter
    def get_nombre(self):
        return self.__nombre

    # implementación de método abstracto descripción para mostrar información del cliente
    def descripcion(self):
        return f"Cliente: {self.__nombre}"