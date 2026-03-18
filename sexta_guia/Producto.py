class Producto:
    # JUAN PABLO FLORES DÍAZ | Reto 4
    # Crear la clase Producto:
    # Atributos:
    # - nombre
    # - precio
    # - cantidad
    # Metodo:
    # - calcular_total() -> precio * cantidad
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        return self.precio * self.cantidad
