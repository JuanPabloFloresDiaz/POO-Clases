class Computadora:
    # JUAN PABLO FLORES DÍAZ | Reto 9
    # Crear una clase Computadora con:
    # Atributos:
    # - marca
    # - memoria_ram
    # - encendida (False por defecto)
    # Metodos:
    # - encender()
    # - apagar()
    # - estado() -> Indica si esta encendida o apagada
    def __init__(self, marca, memoria_ram):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.encendida = False

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def estado(self):
        if self.encendida:
            return "Encendida"
        return "Apagada"