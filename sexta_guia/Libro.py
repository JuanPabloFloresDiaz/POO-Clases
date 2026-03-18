class Libro:
    # JUAN PABLO FLORES DÍAZ | Reto 5
    # Crear la clase Libro:
    # Atributos:
    # - titulo
    # - disponible (True)
    # Metodos:
    # - prestar()
    # - devolver()
    # Crear 2 libros, prestar uno y mostrar cuales estan disponibles.
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        return f"El libro '{self.titulo}' no esta disponible."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        return f"El libro '{self.titulo}' ya estaba disponible."
