# Fase-4---Componente-practico---Practicas-Simuladas
# Grupo : 263
# Integrantes:
# Jhonier Alexander Maquilon Miranda 
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
        
        

    # implemento excepción para errores de cliente.
class ClienteError(Exception):
    pass

    # implemento excepción para errores de servicio.
class ServicioError(Exception):
    pass
    # implemento excepción para errores de reserva.
class ReservaError(Exception):
    pass

class Entidad(ABC):

    # constructor general con id para todas las entidades del sistema, lo que permite una identificación única y facilita la gestión de datos.
    def __init__(self, id):
    # Guardo  id para identificar la entidad de forma única, lo que facilita la gestión y búsqueda dentro del sistema.
        self.id = id
    # método obligatorio para describir la entidad.
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
    
# Creo la clase servicio .
class Servicio(ABC): 
    # Constructor que recibe el nombre del servicio
    def __init__(self, nombre):
    # Guardo el nombre del servicio en un atributo de la clase 
        self.nombre = nombre  
    # Indico que este método debe ser obligatorio en las clases hijas
    @abstractmethod  
    def calcular_costo(self, horas, **kwargs):
        pass
    # Método obligatorio para calcular el costo del servicio
    @abstractmethod 
    # Devuelve una descripción del servicio
    def descripcion(self):
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
        
    # Clase que representa alquiler de equipos como servicio.
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
        
# clase que representa servicio de asesoría especializado
class Asesoria(Servicio):
    # implemento el constructor que recibe especialida y asigna el nombre del servicio
    def __init__(self, especialidad):
    # llmo al constructor padre para asignar el nombre del servicio y guardo la especialidad para cálculos y validaciones posteriores
        super().__init__("Asesoría")
    # guardo la especialidad del servicio para su uso en cálculos de costo y descripción del servicio
        self.especialidad = especialidad
    #articulo metodo para calcular el costo de la asesoría según horas y aplicando un posible descuento
    def calcular_costo(self, horas, **kwargs):
    # obtengo el descuento del diccionario de argumentos, si no se especifica, se asume 0
        descuento = kwargs.get("descuento", 0)
    # calculo el costo total multiplicando la tarifa fija por las horas y aplicando el descuento si es mayor a 0
        total = 80000 * horas
        # si hay un descuento, lo aplico al total restando el porcentaje correspondiente
        if descuento > 0:
        # aplico el descuento al total, reduciendo el costo según el porcentaje indicado
            total -= total * (descuento / 100)

        return total

    def descripcion(self):
        return f"Asesoría en {self.especialidad}"

    def validar_parametros(self, **kwargs):
        if not self.especialidad:
            raise ServicioError("Especialidad requerida")

# clase que representa una reserva en el sistema
class Reserva:
    # constructor de la reserva
    def __init__(self, cliente, servicio, horas):
        self.costo = None  # inicializo el costo como None para que se calcule al confirmar la reserva
        try:
    # valido que el cliente sea una instancia válida de la clase Cliente
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")
    # valido que el servicio sea una instancia válida de Servicio
            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")
    # valido que las horas sean mayores a 0
            if horas <= 0:
                raise ReservaError("Horas inválidas")
    # guardo el cliente dentro de la reserva
            self.cliente = cliente
    # guardo el servicio contratado
            self.servicio = servicio
    # guardo la cantidad de horas de la reserva
            self.horas = horas
    # estado inicial de la reserva
            self.estado = "Pendiente"
    # registro en el archivo de logs la creación de la reserva
            log_event("Reserva creada correctamente")
        except Exception as e:
    # registro cualquier error ocurrido en la creación
            log_event(f"Error creando reserva: {e}")
    # relanzo el error para que sea manejado externamente
            raise
    # método para confirmar la reserva
    def confirmar(self):
        try:
    # verifico que la reserva esté en estado pendiente
            if self.estado != "Pendiente":
                raise ReservaError("No se puede confirmar")
    # valido los parámetros del servicio antes de usarlo
            self.servicio.validar_parametros()
    # calculo el costo total del servicio según las horas
            costo = self.servicio.calcular_costo(self.horas)
    # cambio el estado de la reserva a confirmada
            self.estado = "Confirmada"
    # guardo el costo calculado dentro del objeto reserva
            self.costo = costo
    # registro la confirmación en logs con el costo
            log_event(f"Reserva confirmada - Costo: {costo}")
        except Exception as e:
    # registro el error ocurrido durante la confirmación
            log_event(f"Error al confirmar reserva: {e}")
    # relanzo el error para ser mas específico y permitir control externo
            raise
    # método para cancelar la reserva
    def cancelar(self):
        try:
    # verifico si la reserva ya está cancelada
            if self.estado == "Cancelada":
                raise ReservaError("Ya está cancelada")
    # cambio el estado a cancelada
            self.estado = "Cancelada"
    # registro la cancelación en logs
            log_event("Reserva cancelada")
        except Exception as e:
    # registro el error de cancelación
            log_event(f"Error cancelando reserva: {e}")
    # relanzo el error para control externo
            raise   # importante mantenerlo para que quien use el método pueda manejar la excepción si lo desea
    # método que ejecuta el proceso completo de la reserva
    def procesar(self):
        try:
    # intento confirmar la reserva automáticamente
            self.confirmar()
        except Exception as e:
    # registro cualquier fallo en el procesamiento
            log_event(f"Fallo en procesamiento: {e}")
        finally:
    # este bloque siempre se ejecuta pase lo que pase
            log_event("Proceso de reserva finalizado")
    # método que devuelve un resumen de la reserva
    def obtener_resumen(self):
        return {
            "cliente": self.cliente.get_nombre(),
            "servicio": self.servicio.descripcion(),
            "horas": self.horas,
            "estado": self.estado,
            "costo": getattr(self, "costo", None)
        }
        
    
    # clase que representa el sistema de reservas, gestionando clientes, servicios y reservas.
class Sistema:
    # constructor del sistema que inicializa listas para clientes, servicios y reservas
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
    # método para agregar un cliente al sistema con validación para evitar duplicados
    def agregar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)
            log_event("Cliente agregado al sistema")
    # método para agregar un servicio al sistema con validación para evitar duplicados
    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        log_event("Reserva agregada al sistema")
    # método para agregar un servicio al sistema con validación para evitar duplicados
    def agregar_servicio(self, servicio):
        if servicio not in self.servicios:
            self.servicios.append(servicio)
            log_event("Servicio agregado al sistema")
    # método para crear una reserva a partir de un cliente, servicio y horas, con validación y registro en logs
    def crear_reserva(self, cliente, servicio, horas):
        reserva = Reserva(cliente, servicio, horas)
        self.reservas.append(reserva)
        log_event("Reserva creada desde sistema")
        return reserva
    # metodo para listar todas las reservas en el sistema, devolviendo un resumen de cada una
    def listar_reservas(self):
        return [r.obtener_resumen() for r in self.reservas]
    # método para buscar un cliente por su documento, lo que facilita la gestión de clientes dentro del sistema
    def buscar_cliente(self, documento):
        for cliente in self.clientes:
            if cliente.id == documento:
                return cliente
        return None