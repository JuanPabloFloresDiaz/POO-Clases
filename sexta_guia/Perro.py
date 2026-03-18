class Perro:
    # JUAN PABLO FLORES DÍAZ | Reto 6
    # Crear una clase Perro con:
    # Atributos:
    # - nombre
    # - raza
    # Metodos:
    # - ladrar() -> Imprime: "Guau! Soy {nombre}"
    # - mostrar_info() -> Muestra nombre y raza
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        return f"Guau! Soy {self.nombre}"

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}"
