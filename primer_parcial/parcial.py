#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 1
# Crear una función para calcular el perímetro de un triangulo
""" def calcular_perimetro_triangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
    
try:
    lado1 = validar_numero("Ingrese la longitud del primer lado del triángulo: ")
    lado2 = validar_numero("Ingrese la longitud del segundo lado del triángulo: ")
    lado3 = validar_numero("Ingrese la longitud del tercer lado del triángulo: ")
    perimetro = calcular_perimetro_triangulo(lado1, lado2, lado3)
    print(f"El perímetro del triángulo es: {perimetro}")
except ValueError as error:
    print(error) """
    
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 2
# Que el usuario ingrese dos números y que decida qué operación quiere realizar, suma, resta, 
# multiplicación o división, utilizar funciones para cada operación
""" def sumar(valor1, valor2):
    return valor1 + valor2
def restar(valor1, valor2):
    return valor1 - valor2
def multiplicar(valor1, valor2):
    return valor1 * valor2
def dividir(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Error: División por cero no permitida."
def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
def menu():
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    while True:
        opcion = input("Ingrese el número de la operación (1-4): ")
        if opcion in ['1', '2', '3', '4']:
            return opcion
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")
try:
    valor1 = validar_numero("Ingrese el primer número: ")
    valor2 = validar_numero("Ingrese el segundo número: ")
    opcion = menu()
    if opcion == '1':
        resultado = sumar(valor1, valor2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        resultado = restar(valor1, valor2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        resultado = multiplicar(valor1, valor2)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == '4':
        resultado = dividir(valor1, valor2)
        print(f"El resultado de la división es: {resultado}")
except ValueError as error:
    print(error) """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 3    
# Crear una lista con 5 números enteros ingresados por el usuario.
# Luego:
# •	Muestra la lista completa
# •	Muestra el número mayor y el número menor de la lista
""" numeros = []
def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
for i in range(5):
    while True:
        try:
            numero = validar_numero(f"Ingrese el número entero {i+1}: ")
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero válido.")
print("La lista completa de números es:", numeros)
print("El número mayor de la lista es:", max(numeros))
print("El número menor de la lista es:", min(numeros)) """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 4
#Crea una función llamada calcular_promedio que:
# •	Reciba 3 números como parámetros ingresados por el usuario
# •	Calcule el promedio
# •	Retorne el resultado
#Después, llamar a la función y mostrar el promedio en pantalla.
""" def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio
def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
numero1 = validar_numero("Ingrese el primer número: ")
numero2 = validar_numero("Ingrese el segundo número: ")
numero3 = validar_numero("Ingrese el tercer número: ")
promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio de los números ingresados es: {promedio}") """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 5
# Crea un programa que pida al usuario un número entero y determine si es par o impar.
""" def determinar_paridad(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
numero = validar_numero("Ingrese un número entero: ")
paridad = determinar_paridad(numero)
print(f"El número {numero} es {paridad}.") """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 6
# Crea un programa que determine el precio de un boleto de cine según la edad del usuario. 
# Si la persona es menor de 12 años o mayor de 65, el boleto cuesta $5. 
# Si tiene entre 12 y 65 años, el boleto cuesta $10.
""" def determinar_precio_boleto(edad):
    if edad < 12 or edad > 65:
        return 5
    else:
        return 10
def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
edad = validar_numero("Ingrese su edad: ")
precio_boleto = determinar_precio_boleto(edad)
print(f"El precio del boleto de cine es: ${precio_boleto}") """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 7
# Crear un bucle que solicite ingresar una palabra y que salga del bucle hasta ingresar la palabra 
# “Python” e imprimir “Saliste del bucle”
""" while True:
    palabra = input("Ingresa una palabra (ingresa 'Python' para salir): ")
    if not palabra.strip():
        print("Por favor, ingresa una palabra válida (no puede estar vacía).")
    elif palabra == "Python":
        print("Saliste del bucle")
        break
    else:
        print("Palabra incorrecta, intenta de nuevo.") """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 8
# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:
# 1. toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# 2. si es par, evalúa un nuevo c0 como c0 ÷ 2;
# 3. de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# 4. si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
""" def obtener_numero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo y mayor que cero. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
c0 = obtener_numero_positivo("Ingresa un número entero positivo mayor que cero: ")
secuencia = [c0]
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    secuencia.append(c0)
print("La secuencia de Collatz es:" + " -> ".join(map(str, secuencia))) """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 9
# Solicitar ingresar grados Celsius y devolver su equivalente en Fahrenheit
# F = (C * 9/5) + 32
""" def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
celsius = validar_numero("Ingresa la temperatura en grados Celsius: ")
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit") """
#Parcial 1
#Nombre: Juan Pablo Flores Díaz
#Carne: FD100125
# Ejercicio 10
# Solicitar ingresar el número de horas y entregar su equivalente en minutos y segundos
def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
horas = validar_numero("Ingresa el número de horas: ")
minutos = horas * 60
segundos = horas * 3600
print(f"{horas} horas son {minutos} minutos y {segundos} segundos")