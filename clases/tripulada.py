""" Este modulo define la clase Tripulada, la cual hereda los métodos y atributos de la clase Nave y tambien, define nuevos métodos y atributos propios """

from clases.nave import Nave  # Importar la clase Nave


class Tripulada(Nave):  # Definir la clase
    def __init__(
        self,
        pais=None,
        peso=None,
        anio=None,
        nombre=None,
        velocidad=None,
        orbita=None,
        tipo_mision=None,
        capacidad=None,
        nombre_mision=None,
    ):  # Inicializar la clase
        super().__init__(
            pais, peso, anio, nombre, velocidad
        )  # Llamar al constructor de la clase padre
        self.__orbita = orbita
        self.__tipo_mision = tipo_mision
        self.__capacidad = capacidad
        self.__nombre_mision = nombre_mision

    # =============== Métodos getters =============== #
    def obtener_orbita(self):
        return self.__orbita

    def obtener_tipo_mision(self):
        return self.__tipo_mision

    def obtener_capacidad(self):
        return self.__capacidad

    def obtener_nombre_mision(self):
        return self.__nombre_mision

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

    def repostar(self):  # Repostar la nave
        nombre = self.obtener_nombre()
        return f"La nave {nombre} ha repostado combustible éxitosamente"

    def acoplamiento(self):  # Abrir paracaidas
        nombre = self.obtener_nombre()
        return f"La nave {nombre}, se ha acoplado a la estación éxitosamente"
