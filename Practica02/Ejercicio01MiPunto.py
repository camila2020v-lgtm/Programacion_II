"""
Laboratorio 2 - Programación II
EJERCICIO 1: CLASE MiPunto
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""

import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancia(self, *args):
        if len(args) == 1:
            punto = args[0]
            return math.sqrt((self.x - punto.x)**2 + (self.y - punto.y)**2)
        elif len(args) == 2:
            x2, y2 = args
            return math.sqrt((self.x - x2)**2 + (self.y - y2)**2)
print("=== PRUEBA EJERCICIO 1 ===")
p1 = MiPunto()           # (0,0)
p2 = MiPunto(10, 30.5)  # (10,30.5)
print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())
print("Distancia (objeto):", p1.distancia(p2))
print("Distancia (x,y):", p1.distancia(10, 30.5))

