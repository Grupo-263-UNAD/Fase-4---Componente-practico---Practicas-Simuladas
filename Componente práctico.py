# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Integrantes:
# Jhonier Alexander Maquilon Miranada 
# Luis Angel Savedra Linares
# Tutor: Juan Pablo Arango Cardona
# Trabajo colaborativo.
# 12 de  mayo de 2026

# importo herramientas para clases abstractas
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
# implemento excepción para errores de servicio
class ServicioError(Exception):
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
            raise ClienteError(str(e)) from e

    # obtengo nombre del cliente con método getter
    def get_nombre(self):
        # retorno el nombre del cliente para que pueda ser accedido de forma controlada
        return self.__nombre

    # implementación de método abstracto descripción para mostrar información del cliente
    def descripcion(self):
        # retorno una cadena con el nombre del cliente para cumplir con la interfaz definida en la clase base
        return f"Cliente: {self.__nombre}"
    
    # implementación de clsase Reserva que representa una reserva de servicio realizada por un cliente.
class Reserva:
        
    def __init__(self, cliente, servicio, horas):
    # constructor de la reserva con validaciones y manejo de errore.
        if horas <= 0:
    #log de error si las horas no son válidas.
            log_event("Error horas inválidas")
    #raise de error si las horas no son válidas para que pueda ser manejado por quien instancie la clase.
            raise ReservaError("Horas inválidas")
    # Tutor en esta línea se asigna el cliente a la reserva para establecer la relación entre ambos.
        self.cliente = cliente
    # siguiente línea se asigna el servicio a la reserva para definir qué servicio se ha reservado.
        self.servicio = servicio
    # Consiguiente esta parte se asigna la cantidad de horas a la reserva para especificar la duración del servicio reservado.
        self.horas = horas
    # y por ultimo se asigna el estado inicial de la reserva como "Pendiente".
        self.estado = "Pendiente"
    # Articulo log para registrar la creación de la reserva en el sistema , lo que facilita el seguimiento de las acciones realizadas por los usuarios.
        log_event("Reserva creada") 
    # Defino una clase abstracta llamada Servicio que servirá como base para otros servicios
    
class Servicio(ABC): 
    # Constructor que recibe el nombre del servicio
    def __init__(self, nombre):
    # Guardo el nombre del servicio en un atributo de la clase 
        self.nombre = nombre  
    # Indico que este método debe ser obligatorio en las clases hijas
    @abstractmethod  
    # Utilizo el Método para calcular el costo del servicio según horas
    def calcular_costo(self, horas, **kwargs): 
    # No implemento aquí porque cada servicio lo define diferente
        pass 
    # Método obligatorio para describir el servicio
    @abstractmethod 
    # Devuelve una descripción del servicio
    def descripcion(self):
    # Se implementa en cada clase hija para dar detalles específicos del servicio
        pass 
    # Método obligatorio para validar parámetros del servicio
    @abstractmethod  
    # Valida que los datos del servicio sean correctos
    def validar_parametros(self, **kwargs): 
    # Cada servicio define sus reglas
        pass 
    # Creo la clase ReservaSala que hereda de Servicio
    
class ReservaSala(Servicio):  
    # Constructor que recibe el tipo de sala (ya sea normal o premium)
    def __init__(self, tipo_sala):
    # Llamo al constructor de la clase padre y asigno el nombre del servicio
        super().__init__("Reserva de Sala")  
    # Guardo el tipo de sala (normal o premium)
        self.tipo_sala = tipo_sala  
    #Uso el  Método para calcular el costo según las horas
    def calcular_costo(self, horas, **kwargs): 
        if self.tipo_sala == "premium":
            tarifa = 50000
        elif self.tipo_sala == "normal":
            tarifa = 30000
        else:
        # Defino tarifa según tipo de sala y si el tipo no es válido, lanzo un error para que pueda ser manejado por quien instancie la clase.
            raise ServicioError("Tipo de sala inválido") 
        # Retorno el costo total multiplicando tarifa por horas
        return tarifa * horas  
    # Método que describe el servicio
    def descripcion(self): 
        # Retorno el tipo de sala como texto para dar una descripción clara del servicio reservado
        return f"Sala tipo {self.tipo_sala}"  
    # Método para validar el tipo de sala
    def validar_parametros(self, **kwargs): 
        # Verifico si el tipo de sala es válido
        if self.tipo_sala not in ["normal", "premium"]:  
            # Lanzo error si no es válido
            raise ServicioError("Tipo de sala inválido")  
    # Clase que representa alquiler de equipos
    
class AlquilerEquipo(Servicio): 
    #Uso el Constructor que recibe el equipo
    def __init__(self, equipo):
    # Asigno nombre del servicio y guardo el tipo de equipo para su uso en cálculos y validaciones posteriores  
        super().__init__("Alquiler de Equipo") 
    #Guardo el tipo de equipo 
        self.equipo = equipo  
    # Método para calcular costo según horas y tipo de equipo
    def calcular_costo(self, horas, **kwargs): 
    # Defino precios por tipo de equipo 
        precios = {"pc": 20000, "proyector": 15000}  
    # Verifico si el equipo existe en la lista de precios, si no, lanzo un error para que pueda ser manejado por quien instancie la clase.
        if self.equipo not in precios:  
    #Error si el equipo no está
            raise ServicioError("Equipo no disponible") 
    # Retorno costo total
        return precios[self.equipo] * horas 
    # Método de descripción del servicio
    def descripcion(self):  
    # Devuelvo el nombre del equipo para describir claramente el servicio de alquiler contratado
        return f"Alquiler de {self.equipo}"  
    # Validación de equipo
    def validar_parametros(self, **kwargs):  
        # Si no hay equipo
        if not self.equipo:
        # Error si no se especifica el equipo para alquiler, lo que es necesario para calcular el costo y describir el servicio correctamente.  
            raise ServicioError("Equipo inválido") 
        