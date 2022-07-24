""" Este modulo define la clase Nave, la cual es la super clase y posee todos los atributos y métodos abstractos que serán heredados por las subclases """

from abc import ABC, ABCMeta, abstractmethod


class Nave(metaclass=ABCMeta):  # Definir la clase
    def __init__(self, pais, peso, anio, nombre, velocidad):  # Inicializar la clase
        self.__pais = pais
        self.__peso = peso
        self.__anio = anio
        self.__nombre = nombre
        self.__velocidad = velocidad

    # =============== Métodos getters =============== #
    def obtener_pais(self):
        return self.__pais

    def obtener_peso(self):
        return self.__peso

    def obtener_anio(self):
        return self.__anio

    def obtener_nombre(self):
        return self.__nombre

    def obtener_velocidad(self):
        return self.__velocidad

    # =============== Métodos setters =============== #

    # =============== Métodos abstractos =============== #
    @abstractmethod
    def despegar(self):  # Despegar la nave
        pass

    @abstractmethod
    def cuenta_regresiva(self):  # Cuenta regresiva para el despegue
        pass

    @abstractmethod
    def chequeo_general(self):  # Chequeo general de la nave
        pass
