"""
Laboratorio 1 - Programación II
Ejercicio 1: Cronometro
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""

import time
import random


# Clase Cronometro

class Cronometro:

    # Constructor sin argumentos
    def __init__(self):
        self.__inicia = int(time.time() * 1000)
        self.__finaliza = 0

    # Métodos getters
    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    # Método inicia()
    def inicia(self):
        self.__inicia = int(time.time() * 1000)

    # Método detener()
    def detener(self):
        self.__finaliza = int(time.time() * 1000)

    # Método lapsoDeTiempo()
    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia

    # Método para mostrar información
    def __str__(self):
        return f"Inicia: {self.__inicia}, Finaliza: {self.__finaliza}"

# Método de Ordenación por Selección

def ordenacionSeleccion(lista):

    for i in range(len(lista) - 1):

        minimo = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j

        temp = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temp


# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    print("ORDENANDO 100.000 NUMEROS CON SELECCION\n")

    # Crear lista de 100000 números
    numeros = [random.randint(1, 1000000) for _ in range(100000)]

    # Crear objeto Cronometro (AQUI SE USA EL CONSTRUCTOR)
    cronometro = Cronometro()

    # Reiniciar tiempo
    cronometro.inicia()

    # Ejecutar ordenación
    ordenacionSeleccion(numeros)

    # Detener cronómetro
    cronometro.detener()

    print("Tiempo de ejecución en milisegundos:",
          cronometro.lapsoDeTiempo())
