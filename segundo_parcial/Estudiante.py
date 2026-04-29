class Estudiante:
    # JUAN PABLO FLORES DÍAZ
    # Crear la clase Estudiante:
    # Atributos:
    # - nombre
    # - nota1
    # - nota2
    # - nota3
    # Metodos:
    # - calcular_promedio()
    # - mostrar_estado()
    #   - Aprobado si promedio >= 6
    #   - Reprobado si promedio < 6
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def mostrar_estado(self):
        if self.calcular_promedio() >= 6:
            return "Aprobado"
        return "Reprobado"
