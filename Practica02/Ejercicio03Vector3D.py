"""
Laboratorio 2 - Programación II
EJERCICIO 3: VECTORES 3D (SOBRECARGA DE OPERADORES)
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""

import math
class Vector3D:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, v):
        return Vector3D(self.a1 + v.a1,
                        self.a2 + v.a2,
                        self.a3 + v.a3)

    def __sub__(self, v):
        return Vector3D(self.a1 - v.a1,
                        self.a2 - v.a2,
                        self.a3 - v.a3)

    def escalar(self, r):
        return Vector3D(self.a1 * r,
                        self.a2 * r,
                        self.a3 * r)

    def producto_escalar(self, v):
        return (self.a1*v.a1 +
                self.a2*v.a2 +
                self.a3*v.a3)

    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normal(self):
        m = self.magnitud()
        return Vector3D(self.a1/m, self.a2/m, self.a3/m)

    def producto_vectorial(self, v):
        return Vector3D(
            self.a2*v.a3 - self.a3*v.a2,
            self.a3*v.a1 - self.a1*v.a3,
            self.a1*v.a2 - self.a2*v.a1
        )
print("=== PRUEBA EJERCICIO 3 ===")
a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)
suma = a + b
esc = a.escalar(2)
mag = a.magnitud()
n = a.normal()
prod_escalar = a.producto_escalar(b)
prod_vectorial = a.producto_vectorial(b)
print("Suma:", suma.a1, suma.a2, suma.a3)
print("Escalar:", esc.a1, esc.a2, esc.a3)
print("Magnitud:", round(mag,4))
print("Normal:", round(n.a1,3), round(n.a2,3), round(n.a3,3))
print("Producto escalar:", prod_escalar)
print("Producto vectorial:", prod_vectorial.a1, prod_vectorial.a2, prod_vectorial.a3)

