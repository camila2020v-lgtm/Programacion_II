"""
Laboratorio 1 - Programación II
Ejercicio 3: Ecuación Cuadrática
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""

import math


class EcuacionCuadratica:

    # Constructor
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # Método getDiscriminante()
    def getDiscriminante(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    # Método getRaiz1()
    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b + math.sqrt(discriminante)) / (2 * self.__a)

    # Método getRaiz2()
    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b - math.sqrt(discriminante)) / (2 * self.__a)

    # Método __str__
    def __str__(self):
        return f"EcuacionCuadratica[{self.__a}, {self.__b}, {self.__c}]"

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    print("Ingrese a, b, c:")
    a, b, c = map(float, input().split())

    # USO DEL CONSTRUCTOR
    ecuacion = EcuacionCuadratica(a, b, c)

    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        print("La ecuacion tiene dos raices",
              ecuacion.getRaiz1(),
              "y",
              ecuacion.getRaiz2())

    elif discriminante == 0:
        print("La ecuacion tiene una raiz",
              ecuacion.getRaiz1())

    else:
        print("La ecuacion no tiene raices reales")
