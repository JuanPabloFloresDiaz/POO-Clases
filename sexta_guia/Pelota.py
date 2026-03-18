class Pelota:
    # JUAN PABLO FLORES DÍAZ | Reto 8
    # Crear una clase Pelota con:
    # Atributos:
    # - color
    # - tamano
    # Metodo:
    # - descripcion() -> Imprime: "Pelota color {color} de tamano {tamano}"
    def __init__(self, color, tamano):
        self.color = color
        self.tamano = tamano

    def descripcion(self):
        return f"Pelota color {self.color} de tamano {self.tamano}"
