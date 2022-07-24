""" Este modulo define la clase NoTripulada, la cual hereda  los métodos y atributos de la clase Nave y tambien, define nuevos métodos y atributos propios """

from clases.nave import Nave  # Importar la clase Nave


class NoTripulada(Nave):  # Definir la clase
    def __init__(
        self,
        pais=None,
        peso=None,
        anio=None,
        nombre=None,
        velocidad=None,
        empuje=None,
        combustible=None,
        planeta_exploracion=None,
        cantidad_motores=None,
    ):  # Inicializar la clase
        super().__init__(
            pais, peso, anio, nombre, velocidad
        )  # Llamar al constructor de la clase padre
        self.__empuje = empuje
        self.__combustible = combustible
        self.__planeta_exploracion = planeta_exploracion
        self.__cantidad_motores = cantidad_motores

    # =============== Métodos getters =============== #
    def obtener_empuje(self):
        return self.__empuje

    def obtener_combustible(self):
        return self.__combustible

    def obtener_planeta_exploracion(self):
        return self.__planeta_exploracion

    def obtener_cantidad_motores(self):
        return self.__cantidad_motores

    # =============== Métodos abstractos heredados =============== #
    def despegar(self):  # Despegar la nave
        nombre = self.obtener_nombre()
        return f"La nave {nombre} ha despegado"

    def cuenta_regresiva(self):  # Cuenta regresiva para el despegue
        nombre = self.obtener_nombre()
        return f"Lanzamiento de la nave {nombre}, en 3,2,1..."

    def chequeo_general(self):  # Chequeo general de la nave
        nombre = self.obtener_nombre()
        return f"Chequeo general de la nave {nombre} fue realizado con éxito"

    # =============== Métodos propios =============== #
    def explorar(self):  # Explorar el planeta
        nombre = self.obtener_nombre()
        return f"La nave {nombre} esta lista para iniciar exploración"

    def amartizar(self):  # Amartizar la nave
        nombre = self.obtener_nombre()
        return f"El amartizaje de la nave {nombre} fue un éxito"

    def corregir_trayectoria(self):  # Corregir la trayectoria
        nombre = self.obtener_nombre()
        return f"La trayectoria de la nave {nombre}, ha sido corregida con éxito"
