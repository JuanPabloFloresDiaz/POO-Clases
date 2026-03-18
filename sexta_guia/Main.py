from CuentaBancaria import CuentaBancaria
from Rectangulo import Rectangulo
from Estudiante import Estudiante
from Producto import Producto
from Libro import Libro
from Perro import Perro
from Celular import Celular
from Pelota import Pelota
from Computadora import Computadora


# Reto 1
# JUAN PABLO FLORES DÍAZ
# Cree una clase CuentaBancaria con:
# Atributos:
# - titular
# - saldo (inicia en 0)
# Metodos:
# - depositar(cantidad)
# - retirar(cantidad) (no permitir retirar mas del saldo)
# - mostrar_saldo()
print("=" * 60)
print("RETO 1: CuentaBancaria")
print("=" * 60)
cuenta = CuentaBancaria("Ana Perez")
cuenta.depositar(500)
retiro_exitoso = cuenta.retirar(200)
print(f"Titular: {cuenta.titular}")
print(f"Retiro exitoso: {retiro_exitoso}")
print(f"Saldo actual: {cuenta.mostrar_saldo()}")
print()


# Reto 2
# JUAN PABLO FLORES DÍAZ
# Crear la clase Rectangulo con:
# Atributos:
# - base
# - altura
# Metodos:
# - calcular_area()
# - calcular_perimetro()
print("=" * 60)
print("RETO 2: Rectangulo")
print("=" * 60)
rectangulo = Rectangulo(8, 4)
print(f"Base: {rectangulo.base}")
print(f"Altura: {rectangulo.altura}")
print(f"Area: {rectangulo.calcular_area()}")
print(f"Perimetro: {rectangulo.calcular_perimetro()}")
print()


# Reto 3
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
print("=" * 60)
print("RETO 3: Estudiante")
print("=" * 60)
estudiante = Estudiante("Luis", 7, 5, 8)
print(f"Nombre: {estudiante.nombre}")
print(f"Promedio: {estudiante.calcular_promedio():.2f}")
print(f"Estado: {estudiante.mostrar_estado()}")
print()


# Reto 4
# JUAN PABLO FLORES DÍAZ
# Crear la clase Producto:
# Atributos:
# - nombre
# - precio
# - cantidad
# Metodo:
# - calcular_total() -> precio x cantidad
print("=" * 60)
print("RETO 4: Producto")
print("=" * 60)
producto = Producto("Cuaderno", 3.5, 6)
print(f"Producto: {producto.nombre}")
print(f"Precio: {producto.precio}")
print(f"Cantidad: {producto.cantidad}")
print(f"Total: {producto.calcular_total()}")
print()


# Reto 5
# JUAN PABLO FLORES DÍAZ
# Crear la clase Libro:
# Atributos:
# - titulo
# - disponible (True)
# Metodos:
# - prestar()
# - devolver()
# Crear 2 libros
# Prestar uno
# Mostrar cuales estan disponibles
print("=" * 60)
print("RETO 5: Libro")
print("=" * 60)
libro1 = Libro("Python Basico")
libro2 = Libro("Ciberseguridad 101")

print(libro1.prestar())

print("Libros disponibles:")
if libro1.disponible:
	print(f"- {libro1.titulo}")
if libro2.disponible:
	print(f"- {libro2.titulo}")
print()


# Reto 6
# JUAN PABLO FLORES DÍAZ
# Crear una clase Perro con:
# Atributos:
# - nombre
# - raza
# Metodos:
# - ladrar() -> Imprime: "Guau! Soy {nombre}"
# - mostrar_info() -> Muestra nombre y raza
print("=" * 60)
print("RETO 6: Perro")
print("=" * 60)
perro = Perro("Rocky", "Labrador")
print(perro.ladrar())
print(perro.mostrar_info())
print()


# Reto 7
# JUAN PABLO FLORES DÍAZ
# Crear una clase Celular con:
# Atributos:
# - marca
# - bateria (inicia en 100)
# Metodos:
# - usar(cantidad) -> Resta bateria (no permitir valores negativos)
# - cargar() -> Vuelve la bateria a 100
# - mostrar_bateria()
print("=" * 60)
print("RETO 7: Celular")
print("=" * 60)
celular = Celular("Samsung")
print(f"Marca: {celular.marca}")
print(f"Bateria inicial: {celular.mostrar_bateria()}%")
celular.usar(30)
print(f"Bateria luego de usar 30: {celular.mostrar_bateria()}%")
celular.cargar()
print(f"Bateria despues de cargar: {celular.mostrar_bateria()}%")
print()


# Reto 8
# JUAN PABLO FLORES DÍAZ
# Crear una clase Pelota con:
# Atributos:
# - color
# - tamano
# Metodo:
# - descripcion() -> Imprime: "Pelota color {color} de tamano {tamano}"
print("=" * 60)
print("RETO 8: Pelota")
print("=" * 60)
pelota = Pelota("rojo", "mediano")
print(pelota.descripcion())
print()


# Reto 9
# JUAN PABLO FLORES DÍAZ
# Crear una clase Computadora con:
# Atributos:
# - marca
# - memoria_ram
# - encendida (False por defecto)
# Metodos:
# - encender()
# - apagar()
# - estado() -> Indica si esta encendida o apagada
print("=" * 60)
print("RETO 9: Computadora")
print("=" * 60)
pc = Computadora("Lenovo", "16GB")
print(f"Marca: {pc.marca}")
print(f"Memoria RAM: {pc.memoria_ram}")
print(f"Estado inicial: {pc.estado()}")
pc.encender()
print(f"Estado despues de encender: {pc.estado()}")
pc.apagar()
print(f"Estado despues de apagar: {pc.estado()}")
