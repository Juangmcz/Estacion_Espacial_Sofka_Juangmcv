""" Este modulo define la clase Lanzadera, la cual hereda los métodos y atributos de la clase Nave y tambien, define nuevos métodos y atributos propios """

from clases.nave import Nave  # Importar la clase Nave


class Lanzadera(Nave):  # Definir la clase
    def __init__(
        self,
        pais=None,
        peso=None,
        anio=None,
        nombre=None,
        velocidad=None,
        altura=None,
        potencia=None,
        carga_util=None,
        autonomia=None,
        combustible=None,
    ):  # Inicializar la clase
        super().__init__(
            pais, peso, anio, nombre, velocidad
        )  # Llamar al constructor de la clase padre
        self.__altura = altura
        self.__potencia = potencia
        self.__carga_util = carga_util
        self.__autonomia = autonomia
        self.__combustible = combustible

    # =============== Métodos getters =============== #
    def obtener_altura(self):
        return self.__altura

    def obtener_potencia(self):
        return self.__potencia

    def obtener_carga_util(self):
        return self.__carga_util

    def obtener_autonomia(self):
        return self.__autonomia

    def obtener_combustible(self):
        return self.__combustible

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
    def aterrizar(self):  # Aterrizar la nave
        nombre = self.obtener_nombre()
        return f"El aterrizaje de la nave {nombre} fue un éxito"

    def separacion(self):  # Separación de la nave
        nombre = self.obtener_nombre()
        return f"La nave {nombre} se ha separado exitosamente"

    def abrir_paracaidas(self):  # Abrir paracaidas
        nombre = self.obtener_nombre()
        return f"El paracaidas de la nave {nombre}, se ha sido liberado"
