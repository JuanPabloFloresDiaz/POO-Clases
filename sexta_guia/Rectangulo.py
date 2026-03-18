class Rectangulo:
    # JUAN PABLO FLORES DÍAZ | Reto 2
    # Crear la clase Rectangulo con:
    # Atributos:
    # - base
    # - altura
    # Metodos:
    # - calcular_area()
    # - calcular_perimetro()
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
