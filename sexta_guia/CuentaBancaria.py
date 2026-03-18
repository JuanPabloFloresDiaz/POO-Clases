class CuentaBancaria:
    # JUAN PABLO FLORES DÍAZ | Reto 1
    # Cree una clase CuentaBancaria con:
    # Atributos:
    # - titular
    # - saldo (inicia en 0)
    # Metodos:
    # - depositar(cantidad)
    # - retirar(cantidad) (no permitir retirar mas del saldo)
    # - mostrar_saldo()
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def mostrar_saldo(self):
        return self.saldo