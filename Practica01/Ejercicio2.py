"""
Laboratorio 1 - Programación II
Ejercicio 2: Ecuación Lineal 2x2
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""

class EcuacionLineal:

    # Constructor
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # Método tieneSolucion()
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    # Método getX()
    def getX(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / determinante

    # Método getY()
    def getY(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / determinante

    # Método __str__
    def __str__(self):
        return f"EcuacionLineal[{self.__a},{self.__b},{self.__c},{self.__d},{self.__e},{self.__f}]"

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    print("Ingrese a, b, c, d, e, f:")
    a, b, c, d, e, f = map(float, input().split())

    ecuacion = EcuacionLineal(a, b, c, d, e, f)  # USO DEL CONSTRUCTOR

    if ecuacion.tieneSolucion():
        print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
    else:
        print("La ecuacion no tiene solucion")
