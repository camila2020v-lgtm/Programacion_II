"""
Laboratorio 2 - Programación II
EJERCICIO 2: ALGEBRA VECTORIAL (POLIMORFISMO COMPLETO)
Docente: Lic. Jhonny Roberto Felípez Andrade
Estudiante: Aracely Camila Quispe Vallejos
"""
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2)

    def suma(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def resta(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def producto_punto(self, v):
        return self.x*v.x + self.y*v.y

    def producto_cruz(self, v):
        return self.x*v.y - self.y*v.x

    def perpendicular_a(self, v):
        return round(self.suma(v).modulo(),5) == round(self.resta(v).modulo(),5)

    def perpendicular_b(self, v):
        return round(self.resta(v).modulo(),5) == round(v.resta(self).modulo(),5)

    def perpendicular_c(self, v):
        return self.producto_punto(v) == 0

    def perpendicular_d(self, v):
        izquierda = self.suma(v).modulo()**2
        derecha = self.modulo()**2 + v.modulo()**2
        return round(izquierda,5) == round(derecha,5)

    def paralela_e(self, v):
        if v.x != 0:
            r = self.x / v.x
            return round(self.y,5) == round(r * v.y,5)
        return False

    def paralela_f(self, v):
        return self.producto_cruz(v) == 0

    def proyeccion(self, v):
        escalar = self.producto_punto(v) / (v.modulo()**2)
        return Vector(escalar*v.x, escalar*v.y)

    def componente(self, v):
        return self.producto_punto(v) / v.modulo()

a = Vector(2, 3)
b = Vector(-3, 2)

print("EJERCICIO 2: ALGEBRA VECTORIAL\n")
print("Vectores definidos:")
print("Vector a = (2, 3)")
print("Vector b = (-3, 2)\n")
print("PERPENDICULARIDAD")
print("|a + b| = |a - b|")
print("Resultado:", a.perpendicular_a(b))
print("|a - b| = |b - a|")
print("Resultado:", a.perpendicular_b(b))
print("a · b = 0")
print("Resultado:", a.perpendicular_c(b))
print("|a + b|² = |a|² + |b|²")
print("Resultado:", a.perpendicular_d(b))
print("\nPARALELISMO")
print("a = r b")
print("Resultado:", a.paralela_e(b))
print("a × b = 0")
print("Resultado:", a.paralela_f(b))
print("\nPROYECCION")
p = a.proyeccion(b)
print("Proyección de a sobre b:")
print("Resultado: Proy_b(a) =", (round(p.x,3), round(p.y,3)))
print("\nCOMPONENTE")
print("Componente de a sobre b:")
print("Resultado: Comp_b(a) =", round(a.componente(b),3))
