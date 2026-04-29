from Teclado import Teclado
from Libro import Libro
from Estudiante import Estudiante
from CuentaBancaria import CuentaBancaria
from Rectangulo import Rectangulo
from Perro import Perro

# Ejercicio 1
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Convertir caracteres a código ASCII 
# Pide al usuario una palabra y muestra el código ASCII del primer carácter.

# print("=" * 50)
# print("Ejercicio 1: Código ASCII de un carácter")
# print("=" * 50)
# palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)
# primer_caracter = palabra[0]
# codigo_ascii = ord(primer_caracter)
# print(f"El código ASCII del primer carácter '{primer_caracter}' es: {codigo_ascii}")
# print()

# Ejercicio 2
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Convertir código ASCII a carácter
# Pide un número al usuario y conviértelo en su carácter correspondiente.
# Usar el manejo errores con try-except.

# print("=" * 50)
# print("Ejercicio 2: Carácter desde código ASCII")
# print("=" * 50)
# try:
#     codigo = Teclado.read_integer("Ingrese un código ASCII:", min_value=0)
#     caracter = chr(codigo)
#     print(f"El carácter correspondiente al código {codigo} es: '{caracter}'")
# except ValueError as e:
#     print(f"Error: {e}")
# print()

# Ejercicio 3
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Pide una frase y muestra:
# •	Los primeros 5 caracteres
# •	Los últimos 4 caracteres

print("=" * 50)
print("Ejercicio 3: Slicing de cadenas")
print("=" * 50)
frase = Teclado.read_text("Ingrese una frase:", min_length=5)
print(f"Frase completa: {frase}")
print(f"Primeros 5 caracteres: {frase[:5]}")
if len(frase) >= 4:
    print(f"Últimos 4 caracteres: {frase[-4:]}")
else:
    print(f"Últimos caracteres: {frase}")
print()

# Ejercicio 4
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Pide un nombre de archivo y verifica si termina en:
# •	.txt
# •	.py

print("=" * 50)
print("Ejercicio 4: Verificar extensión de archivo")
print("=" * 50)
archivo = Teclado.read_text("Ingrese un nombre de archivo:", min_length=1)
if archivo.endswith('.txt'):
    print(f"El archivo '{archivo}' es un archivo de texto (.txt)")
elif archivo.endswith('.py'):
    print(f"El archivo '{archivo}' es un archivo de Python (.py)")
else:
    print(f"El archivo '{archivo}' no es .txt ni .py")
print()

# Ejercicio 5
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Pide una palabra y una letra.
# •	Muestra la posición de esa letra usando index()
# •	Usa try-except para evitar error si no existe

print("=" * 50)
print("Ejercicio 5: Buscar posición con index()")
print("=" * 50)
palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)
letra = Teclado.read_text("Ingrese una letra a buscar:", min_length=1, max_length=1)
try:
    posicion = palabra.index(letra)
    print(f"La letra '{letra}' se encuentra en la posición: {posicion}")
except ValueError:
    print(f"La letra '{letra}' no se encuentra en la palabra '{palabra}'")
print()

# Ejercicio 6
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Cree una clase CuentaBancaria con:
# Atributos:
# •	titular
# •	saldo (inicia en 0)
# Métodos:
# •	depositar(cantidad)
# •	retirar(cantidad) (no permitir retirar más del saldo)
# •	mostrar_saldo()

print("=" * 50)
print("Ejercicio 6: CuentaBancaria")
print("=" * 50)
nombre_cuenta = Teclado.read_text("Ingrese el nombre del titular:", min_length=1)
cuenta = CuentaBancaria(nombre_cuenta)
dinero_depositar = Teclado.read_double("Ingrese la cantidad a depositar:", min_value=0)
cuenta.depositar(dinero_depositar)
dinero_retirar = Teclado.read_double("Ingrese la cantidad a retirar:", min_value=0)
retiro_exitoso = cuenta.retirar(dinero_retirar)
print(f"Titular: {cuenta.titular}")
print(f"Retiro exitoso: {retiro_exitoso}")
print(f"Saldo actual: {cuenta.mostrar_saldo()}")
print()

# Ejercicio 7
# Juan Pablo Flores Díaz
# Carnet: FD100125
# Crear la clase Rectangulo con:
# Atributos:
# •	base
# •	altura
# Métodos:
# •	calcular_area()
# •	calcular_perimetro()

print("=" * 50)
print("Ejercicio 7: Rectangulo")
print("=" * 50)
base = Teclado.read_double("Ingrese la base del rectángulo:", min_value=0)
altura = Teclado.read_double("Ingrese la altura del rectángulo:", min_value=0)
rectangulo = Rectangulo(base, altura)
print(f"Base: {rectangulo.base}")
print(f"Altura: {rectangulo.altura}")
print(f"Area: {rectangulo.calcular_area()}")
print(f"Perimetro: {rectangulo.calcular_perimetro()}")
print()

# Ejercicio 8
# Juan Pablo Flores Díaz
# FD100125
# Crear la clase Estudiante:
# Atributos:
# •	nombre
# •	nota1
# •	nota2
# •	nota3
# Métodos:
# •	calcular_promedio()
# •	mostrar_estado()
# o	Aprobado si promedio >= 6
# o	Reprobado si promedio < 6

print("=" * 50)
print("Ejercicio 8: Estudiante")
print("=" * 50)
nombre_estudiante = Teclado.read_text("Ingrese el nombre del estudiante:", min_length=1)
nota1 = Teclado.read_double("Ingrese la primera nota:", min_value=0, max_value=10)
nota2 = Teclado.read_double("Ingrese la segunda nota:", min_value=0, max_value=10)
nota3 = Teclado.read_double("Ingrese la tercera nota:", min_value=0, max_value=10)
estudiante = Estudiante(nombre_estudiante, nota1, nota2, nota3)
print(f"Nombre: {estudiante.nombre}")
print(f"Promedio: {estudiante.calcular_promedio():.2f}")
print(f"Estado: {estudiante.mostrar_estado()}")
print()

# Ejercicio 9
# Juan Pablo Flores Díaz
# FD100125
# Crear la clase Libro:
# •	titulo
# •	disponible (True)
# Métodos:
# •	prestar()
# •	devolver()
# Crear 2 libros
# Prestar uno
# Mostrar cuáles están disponibles

print("=" * 50)
print("Ejercicio 9: Libro")
print("=" * 50)
libro_1 = Teclado.read_text("Ingrese el título del primer libro:", min_length=1)
libro_2 = Teclado.read_text("Ingrese el título del segundo libro:", min_length=1)
libro1 = Libro(libro_1)
libro2 = Libro(libro_2)

libro_prestado = Teclado.read_text("¿Cuál libro desea prestar? (1 o 2):", min_length=1)
if libro_prestado == '1':
    libro1.prestar()
elif libro_prestado == '2':
    libro2.prestar()

print("Libros disponibles:")
if libro1.disponible:
	print(f"- {libro1.titulo}")
if libro2.disponible:
	print(f"- {libro2.titulo}")
print()

# Ejercicio 10
# Juan Pablo Flores Díaz
# FD100125
# Crear una clase Perro con:
# Atributos:
# •	nombre
# •	raza
# Métodos:
# •	ladrar() → Imprime: "Guau! Soy {nombre}"
# •	mostrar_info() → Muestra nombre y raza


print("=" * 50)
print("Ejercicio 10: Perro")
print("=" * 50)
nombre_perro = Teclado.read_text("Ingrese el nombre del perro:", min_length=1)
raza_perro = Teclado.read_text("Ingrese la raza del perro:", min_length=1)
perro = Perro(nombre_perro, raza_perro)
print(perro.ladrar())
print(perro.mostrar_info())
print()