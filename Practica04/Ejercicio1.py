class Pagina:
    def __init__(self, numero_pagina, contenido_pagina):

        self.numero_pagina = numero_pagina
        self.contenido_pagina = contenido_pagina
    def mostrarInfo(self):

        print("Pagina", self.numero_pagina, ":",
              self.contenido_pagina)
class Horario:
    def __init__(self,
                 dias_apertura,
                 hora_apertura,
                 hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
    def mostrarHorario(self):
        print("Dias apertura:", self.dias_apertura)
        print("Hora apertura:", self.hora_apertura)
        print("Hora cierre:", self.hora_cierre)
    def __str__(self):

        return (self.dias_apertura +
                " | " +
                self.hora_apertura +
                " - " +
                self.hora_cierre)
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def mostrarInfo(self):
        print("Autor:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
    def __str__(self):
        return (self.nombre +
                " (" +
                self.nacionalidad +
                ")")
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def mostrarInfo(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
    def __str__(self):
        return (self.nombre +
                " [" +
                self.codigo +
                "]")
class Libro:
    def __init__(self,
                 titulo,
                 isbn,
                 contenido_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        for i in range(len(contenido_paginas)):
            pagina = Pagina(
                i + 1,
                contenido_paginas[i]
            )
            self.paginas.append(pagina)
        print("Libro '" + titulo +
              "' creado correctamente")
    def leer(self):
        print("\nLEYENDO LIBRO")
        print("Libro:", self.titulo)
        for pagina in self.paginas:
            pagina.mostrarInfo()
    def __str__(self):
        return (self.titulo +
                " - ISBN: " +
                self.isbn)
class Prestamo:
    def __init__(self,
                 fecha_prestamo,
                 fecha_devolucion,
                 estudiante,
                 libro):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estudiante = estudiante
        self.libro = libro
    def mostrarInfo(self):
        print("\nPRESTAMO")
        print("Fecha prestamo:",
              self.fecha_prestamo)
        print("Fecha devolucion:",
              self.fecha_devolucion)
        print("Estudiante:",
              self.estudiante)
        print("Libro:",
              self.libro)
    def __str__(self):
        return (str(self.estudiante) +
                " -> " +
                str(self.libro))
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
        print("Biblioteca '" +
              nombre +
              "' creada")
    def agregarLibro(self, libro):
        self.libros.append(libro)
        print("Libro agregado:",
              libro)
    def agregarAutor(self, autor):
        self.autores.append(autor)
        print("Autor agregado:",
              autor)
    def prestarLibro(self,
                     estudiante,
                     libro):
        prestamo = Prestamo(
            "01/06/2026",
            "10/06/2026",
            estudiante,
            libro
        )
        self.prestamos.append(prestamo)
        print("Prestamo realizado correctamente")
    def mostrarEstado(self):
        print("\nESTADO DE LA BIBLIOTECA")
        print("\nNombre:",
              self.nombre)
        print("\nHORARIO")
        self.horario.mostrarHorario()
        print("\nLIBROS")
        for libro in self.libros:
            print(libro)
        print("\nAUTORES")
        for autor in self.autores:
            print(autor)
        print("\nPRESTAMOS")
        for prestamo in self.prestamos:
            prestamo.mostrarInfo()
    def cerrarBiblioteca(self):
        print("\nCerrando biblioteca...")
        self.prestamos.clear()
        print("Todos los prestamos fueron eliminados")
biblioteca = Biblioteca(
    "Biblioteca Central UMSA"
)
autor1 = Autor(
    "Cormac McCarthy",
    "Estadounidense"
)
autor2 = Autor(
    "Peter Heller",
    "Estadounidense"
)
autor3 = Autor(
    "Steve Amsterdam",
    "Australiano"
)
autor4 = Autor(
    "Walter Miller",
    "Estadounidense"
)
biblioteca.agregarAutor(autor1)
biblioteca.agregarAutor(autor2)
biblioteca.agregarAutor(autor3)
biblioteca.agregarAutor(autor4)
paginas_libro1 = [
    "El mundo estaba destruido...",
    "Padre e hijo caminaban...",
    "La carretera seguia vacia..."
]
libro1 = Libro(
    "La carretera",
    "ISBN-111",
    paginas_libro1
)
paginas_libro2 = [
    "El avion habia caido...",
    "El perro observaba el bosque...",
    "Las estrellas brillaban..."
]
libro2 = Libro(
    "Las estrellas caninas",
    "ISBN-222",
    paginas_libro2
)
paginas_libro3 = [
    "El futuro era incierto...",
    "Nadie sabia que ocurriria...",
    "El mundo habia cambiado..."
]
libro3 = Libro(
    "Cosas que no vimos venir",
    "ISBN-333",
    paginas_libro3
)
paginas_libro4 = [
    "Los monjes guardaban libros...",
    "La humanidad intentaba renacer...",
    "El conocimiento era importante..."
]
libro4 = Libro(
    "Un cantico por Leibowitz",
    "ISBN-444",
    paginas_libro4
)
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)
biblioteca.agregarLibro(libro3)
biblioteca.agregarLibro(libro4)
estudiante1 = Estudiante(
    "2025001",
    "Carlos Perez"
)
biblioteca.prestarLibro(
    estudiante1,
    libro1
)
biblioteca.mostrarEstado()
libro1.leer()
biblioteca.cerrarBiblioteca()
