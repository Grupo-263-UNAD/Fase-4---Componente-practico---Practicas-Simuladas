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
from abc import ABC, abstractmethod
import datetime

LOG_FILE = "logs_software_fj.txt"

def log_event(msg):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time}] {msg}\n")

class ClienteError(Exception):
    pass

class ReservaError(Exception):
    pass

class ServicioError(Exception):
    pass

class Entidad(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def descripcion(self):
        pass

class Cliente(Entidad):
    def __init__(self, nombre, documento):
        super().__init__(documento)
        try:
            if not nombre or len(nombre) < 3:
                raise ClienteError("Nombre inválido")

            if not str(documento).isdigit():
                raise ClienteError("Documento inválido")

            self.__nombre = nombre
            self.__documento = documento

            log_event(f"Cliente creado: {nombre}")

        except Exception as e:
            log_event(f"Error cliente: {e}")
            raise ClienteError(str(e)) from e

    def get_nombre(self):
        return self.__nombre

    def descripcion(self):
        return f"Cliente: {self.__nombre}"

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, horas, **kwargs):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass

class ReservaSala(Servicio):
    def __init__(self, tipo_sala):
        super().__init__("Reserva de Sala")
        self.tipo_sala = tipo_sala

    def calcular_costo(self, horas, **kwargs):
        tarifa = 50000 if self.tipo_sala == "premium" else 30000
        return tarifa * horas

    def descripcion(self):
        return f"Sala tipo {self.tipo_sala}"

    def validar_parametros(self, **kwargs):
        if self.tipo_sala not in ["normal", "premium"]:
            raise ServicioError("Tipo de sala inválido")

class AlquilerEquipo(Servicio):
    def __init__(self, equipo):
        super().__init__("Alquiler de Equipo")
        self.equipo = equipo

    def calcular_costo(self, horas, **kwargs):
        precios = {"pc": 20000, "proyector": 15000}
        if self.equipo not in precios:
            raise ServicioError("Equipo no disponible")
        return precios[self.equipo] * horas

    def descripcion(self):
        return f"Alquiler de {self.equipo}"

    def validar_parametros(self, **kwargs):
        if not self.equipo:
            raise ServicioError("Equipo inválido")

class Asesoria(Servicio):
    def __init__(self, especialidad):
        super().__init__("Asesoría")
        self.especialidad = especialidad

    def calcular_costo(self, horas, **kwargs):
        return 80000 * horas

    def descripcion(self):
        return f"Asesoría en {self.especialidad}"

    def validar_parametros(self, **kwargs):
        if not self.especialidad:
            raise ServicioError("Especialidad requerida")

class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")

            if horas <= 0:
                raise ReservaError("Horas inválidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

            log_event("Reserva creada")

        except Exception as e:
            log_event(f"Error creando reserva: {e}")
            raise

    def confirmar(self):
        try:
            if self.estado != "Pendiente":
                raise ReservaError("No se puede confirmar")

            self.servicio.validar_parametros()
            costo = self.servicio.calcular_costo(self.horas)

            self.estado = "Confirmada"
            log_event(f"Reserva confirmada - Costo: {costo}")

        except Exception as e:
            log_event(f"Error al confirmar reserva: {e}")
            raise

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ReservaError("Ya está cancelada")

            self.estado = "Cancelada"
            log_event("Reserva cancelada")

        except Exception as e:
            log_event(f"Error cancelando reserva: {e}")

    def procesar(self):
        try:
            self.confirmar()
        except Exception as e:
            log_event(f"Fallo en procesamiento: {e}")
        finally:
            log_event("Proceso de reserva finalizado")

def main():
    clientes = []
    reservas = []

    try:
        c1 = Cliente("Luis", "12345")
        clientes.append(c1)
    except:
        pass

    try:
        c2 = Cliente("Lu", "abc")
    except:
        pass

    s1 = ReservaSala("premium")

    try:
        s2 = ReservaSala("vip")
        s2.validar_parametros()
    except:
        log_event("Servicio inválido detectado")

    try:
        r1 = Reserva(c1, s1, 2)
        r1.procesar()
        reservas.append(r1)
    except:
        pass

    try:
        r2 = Reserva(c1, s1, -1)
    except:
        pass

    s3 = AlquilerEquipo("pc")

    try:
        r3 = Reserva(c1, s3, 3)
        r3.procesar()
    except:
        pass

    try:
        s4 = AlquilerEquipo("tablet")
        s4.calcular_costo(2)
    except:
        log_event("Error equipo no disponible")

    try:
        s5 = Asesoria("software")
        r5 = Reserva(c1, s5, 1)
        r5.procesar()
    except:
        pass

    print("Simulación finalizada sin detener el sistema")

if __name__ == "__main__":
    main()
