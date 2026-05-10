from datetime import date
class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido
    def mostrarInfo(self):
        print("Página", self.numero, ":", self.contenido)
class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        numero = 1
        for contenido in contenidos_paginas:
            pagina = Pagina(numero, contenido)
            self.paginas.append(pagina)
            numero += 1
    def leer(self):
        print("Libro:", self.titulo)
        for pagina in self.paginas:
            pagina.mostrarInfo()
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def mostrarInfo(self):
        print("Autor:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def mostrarInfo(self):
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
class Prestamo:
    def __init__(self, estudiante, libro):
        self.fechaPrestamo = date.today()
        self.fechaDevolucion = "Pendiente"
        self.estudiante = estudiante
        self.libro = libro
    def mostrarInfo(self):
        print("Préstamo:")
        print("Estudiante:", self.estudiante.nombre)
        print("Libro:", self.libro.titulo)
        print("Fecha préstamo:", self.fechaPrestamo)
        print("Fecha devolución:", self.fechaDevolucion)
class Horario:
    def __init__(self, dias, horaApertura, horaCierre):
        self.dias = dias
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
    def mostrarHorario(self):
        print("Horario:")
        print(self.dias)
        print(self.horaApertura, "-", self.horaCierre)
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Horario(
            "Lunes a Viernes",
            "08:00",
            "20:00"
        )
    def agregarLibro(self, libro):
        self.libros.append(libro)
    def agregarAutor(self, autor):
        self.autores.append(autor)
    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print("Libro prestado correctamente")
    def mostrarEstado(self):
        print("\nBIBLIOTECA")
        print("Nombre:", self.nombre)
        print("\nLIBROS")
        for libro in self.libros:
            print(libro.titulo)
        print("\nAUTORES")
        for autor in self.autores:
            print(autor.nombre)
        print("\nPRESTAMOS")
        for prestamo in self.prestamos:
            prestamo.mostrarInfo()
        print("\nHORARIO")
        self.horario.mostrarHorario()
    def cerrarBiblioteca(self):
        print("\nLa biblioteca ha cerrado")
        self.prestamos.clear()
autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")
autor2 = Autor("Mario Vargas Llosa", "Peruano")
libro1 = Libro(
    "Cien Años de Soledad",
    "12345",
    [
        "Muchos años despues...",
        "La historia continua..."
    ]
)
libro2 = Libro(
    "La Ciudad y los Perros",
    "67890",
    [
        "Inicio del libro",
        "Final del libro"
    ]
)
estudiante1 = Estudiante("2024001", "Juan Perez")
biblioteca = Biblioteca("Biblioteca Central UMSA")
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)
biblioteca.agregarAutor(autor1)
biblioteca.agregarAutor(autor2)
biblioteca.prestarLibro(estudiante1, libro1)
biblioteca.mostrarEstado()
print("\nLEER LIBRO")
libro1.leer()
biblioteca.cerrarBiblioteca()

