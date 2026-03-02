from Teclado import Teclado

#Reto 1
#Utilizando el módulo math pedir al usuario un número y mostrar:
#•	Raíz cuadrada del número (math.sqrt)
#•	Multiplicación del número por valor de π (math.pi)
import math

print("=" * 50)
print("RETO 1: Operaciones con math")
print("=" * 50)
num = Teclado.read_double("Ingrese un número:")
print(f"La raíz cuadrada del número es {math.sqrt(num)}, al multiplicarlo por pi es {num * math.pi}")
print()

# Reto 2
# Generar un número aleatorio entre 1 y 10 utilizando el módulo random.
# Luego pedir al usuario que adivine el número.
import random

print("=" * 50)
print("RETO 2: Juego de adivinanza")
print("=" * 50)
num = random.randint(1, 10)
while True:
    num2 = Teclado.read_integer("Adivine el número (1-10):", min_value=1, max_value=10)
    if num == num2:
        print("¡Felicidades!")
        break
    else:
        print("Debes introducir otro número")
print()

# Reto 3
# Mostrar:
# •	Fecha actual
# •	Hora actual
# •	Solo el año actual
import datetime

print("=" * 50)
print("RETO 3: Fecha y hora actual")
print("=" * 50)
ahora = datetime.datetime.now()
print(f"Fecha y hora completa: {ahora}")
print(f"Solo fecha: {ahora.date()}")
print(f"Solo hora: {ahora.time()}")
print(f"Solo el año: {ahora.year}")
print()

# Reto 4
# Dada una lista de números:
# [10, 20, 30, 40, 50]
# Mostrar:
# •	Promedio
# •	Mediana
# Usar statistics.mean() y statistics.median()
import statistics

print("=" * 50)
print("RETO 4: Estadísticas")
print("=" * 50)
numeros = [10, 20, 30, 40, 50]
promedio = statistics.mean(numeros)
mediana = statistics.median(numeros)
print(f"Lista: {numeros}")
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print()

# Reto 5
# Crear un contador que:
# •	Muestre "Iniciando..."
# •	Espere 3 segundos
# •	Muestre "Finalizado"
# Usar time.sleep().
import time

print("=" * 50)
print("RETO 5: Contador con espera")
print("=" * 50)
print("Iniciando...")
time.sleep(3)
print("Finalizado")
print()

# Reto 6
# Pedir un año al usuario y mostrar el calendario completo de ese año.
# Usa calendar.calendar().
import calendar

print("=" * 50)
print("RETO 6: Calendario del año")
print("=" * 50)
anio = Teclado.read_integer("Ingrese un año:", min_value=1900, max_value=2100)
print(calendar.calendar(anio))
print()

# Reto 7
# Crear módulo propio (ambos archivos deben estar en la misma carpeta)
# Archivo 1
# operaciones.py
import Operaciones

print("=" * 50)
print("RETO 7: Módulo de operaciones")
print("=" * 50)
x = Teclado.read_double("Ingrese el primer número:")
y = Teclado.read_double("Ingrese el segundo número:")
print(f"Suma: {Operaciones.suma(x, y)}")
print(f"Resta: {Operaciones.resta(x, y)}")
print(f"Multiplicación: {Operaciones.multiplicacion(x, y)}")
print(f"División: {Operaciones.division(x, y)}")
print()

# Reto 8
# Crear módulo propio (ambos archivos deben estar en la misma carpeta)
# Archivo 1
# validacion.py
import Validacion

print("=" * 50)
print("RETO 8: Módulo de validación")
print("=" * 50)
num = Teclado.read_integer("Ingrese un número:")
edad = Teclado.read_integer("Ingrese su edad:", min_value=0, max_value=120)
print(f"¿Es par? {Validacion.es_par(num)}")
print(f"¿Es mayor de edad? {Validacion.es_mayor_edad(edad)}")
print()

# Reto 9
# Crear módulo propio (ambos archivos deben estar en la misma carpeta)
# Archivo 1
# conf.py
import Conf

print("=" * 50)
print("RETO 9: Módulo de configuración")
print("=" * 50)
radio = Teclado.read_double("Ingrese el radio:", min_value=0)
print(f"Valor de PI: {Conf.PI}")
print(f"Área del círculo: {Conf.area_circulo(radio)}")
print()
