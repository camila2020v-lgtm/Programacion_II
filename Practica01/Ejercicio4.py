"""
Laboratorio 1 - Programación II
Ejercicio 4: Estadísticas - Parte Estructurada y Orientada a Objetos
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""


import math

# PARTE 1 - PROGRAMACION ESTRUCTURADA

def promedio(valores):
    suma = 0
    for i in range(len(valores)):
        suma += valores[i]
    return suma / len(valores)


def desviacion(valores):
    prom = promedio(valores)
    suma = 0

    for i in range(len(valores)):
        suma += (valores[i] - prom) ** 2

    return math.sqrt(suma / (len(valores) - 1))

# PARTE 2 - PROGRAMACION ORIENTADA A OBJETOS

class Estadistica:

    # CONSTRUCTOR
    def __init__(self, valores):
        self.__valores = valores

    # Metodo promedio()
    def promedio(self):
        suma = 0
        for i in range(len(self.__valores)):
            suma += self.__valores[i]
        return suma / len(self.__valores)

    # Metodo desviacion()
    def desviacion(self):
        prom = self.promedio()
        suma = 0

        for i in range(len(self.__valores)):
            suma += (self.__valores[i] - prom) ** 2

        return math.sqrt(suma / (len(self.__valores) - 1))

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    print("Ingrese 10 numeros:")
    numeros = list(map(float, input().split()))

    print("\n--- PROGRAMACION ESTRUCTURADA ---")
    print("El promedio es", promedio(numeros))
    print("La desviacion estandar es", desviacion(numeros))

    print("\n--- PROGRAMACION ORIENTADA A OBJETOS ---")

    # AQUI SE USA EL CONSTRUCTOR
    estadistica = Estadistica(numeros)

    print("El promedio es", estadistica.promedio())
    print("La desviacion estandar es", estadistica.desviacion())
