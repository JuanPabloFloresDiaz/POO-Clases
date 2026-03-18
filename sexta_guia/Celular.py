class Celular:
    # JUAN PABLO FLORES DÍAZ | Reto 7
    # Crear una clase Celular con:
    # Atributos:
    # - marca
    # - bateria (inicia en 100)
    # Metodos:
    # - usar(cantidad) -> Resta bateria (no permitir valores negativos)
    # - cargar() -> Vuelve la bateria a 100
    # - mostrar_bateria()
    def __init__(self, marca):
        self.marca = marca
        self.bateria = 100

    def usar(self, cantidad):
        if cantidad > 0:
            self.bateria -= cantidad
            if self.bateria < 0:
                self.bateria = 0

    def cargar(self):
        self.bateria = 100

    def mostrar_bateria(self):
        return self.bateria
