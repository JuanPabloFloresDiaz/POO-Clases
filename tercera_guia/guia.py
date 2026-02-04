### Ejercicio 1
# Crea una lista vacía llamada beatles
# Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison
# Emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best
# Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista
# Usa el método insert() para agregar a Ringo Starr al principio de la lista
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 1")
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("Entrada inválida. Por favor, ingresa un texto válido.")

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(f"Lista inicial: {beatles}")

miembros_adicionales = ["Stu Sutcliffe", "Pete Best"]
for miembro in miembros_adicionales:
    nombre = validar_texto(f"Agrega a {miembro}: ")
    beatles.append(nombre)
print(f"Lista después de agregar: {beatles}")

del beatles[3]
del beatles[3]
print(f"Lista después de eliminar: {beatles}")

beatles.insert(0, "Ringo Starr")
print(f"Lista final: {beatles}") """


### Ejercicio 2
# Crear una función para calcular el perímetro de un triángulo
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 2")
def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("El número debe ser mayor a 0. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

def calcular_perimetro(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

lado1 = validar_numero("Ingresa el lado 1 del triángulo: ")
lado2 = validar_numero("Ingresa el lado 2 del triángulo: ")
lado3 = validar_numero("Ingresa el lado 3 del triángulo: ")
perimetro = calcular_perimetro(lado1, lado2, lado3)
print(f"El perímetro del triángulo es: {perimetro}") """


### Ejercicio 3
# Que el usuario ingrese dos números y que decida que operación quiere realizar: suma, resta, multiplicación o división
# Utilizar funciones para cada operación
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 3")
def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

num1 = validar_numero("Ingresa el primer número: ")
num2 = validar_numero("Ingresa el segundo número: ")

print("\nOperaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

while True:
    try:
        opcion = int(input("Elige una operación (1-4): "))
        if 1 <= opcion <= 4:
            break
        else:
            print("Opción inválida. Elige entre 1 y 4.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")

if opcion == 1:
    print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
elif opcion == 2:
    print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
elif opcion == 3:
    print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
elif opcion == 4:
    resultado = division(num1, num2)
    print(f"Resultado: {num1} / {num2} = {resultado}") """


### Ejercicio 4
# Crear una tupla que sea el registro de una auditoría, que solicite los valores:
# Producto, Código, Fecha, Auditor, Estado, Comentarios
# Y luego imprima la tupla
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 4")
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("Entrada inválida. Por favor, ingresa un texto válido.")

producto = validar_texto("Ingresa el nombre del producto: ")
codigo = validar_texto("Ingresa el código: ")
fecha = validar_texto("Ingresa la fecha (DD/MM/AAAA): ")
auditor = validar_texto("Ingresa el nombre del auditor: ")
estado = validar_texto("Ingresa el estado: ")
comentarios = validar_texto("Ingresa los comentarios: ")

auditoria = (producto, codigo, fecha, auditor, estado, comentarios)
print("\nRegistro de Auditoría:")
print(f"Producto: {auditoria[0]}")
print(f"Código: {auditoria[1]}")
print(f"Fecha: {auditoria[2]}")
print(f"Auditor: {auditoria[3]}")
print(f"Estado: {auditoria[4]}")
print(f"Comentarios: {auditoria[5]}")
print(f"\nTupla completa: {auditoria}") """


### Ejercicio 5
# Crear un inventario solicitando al usuario: Código, Nombre, Cantidad en stock, Precio
# Nota: Se debe crear el diccionario inventario vacío al iniciar
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 5")
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("Entrada inválida. Por favor, ingresa un texto válido.")

def validar_numero(mensaje, tipo="float"):
    while True:
        try:
            if tipo == "int":
                numero = int(input(mensaje))
                if numero >= 0:
                    return numero
                else:
                    print("El número debe ser mayor o igual a 0.")
            else:
                numero = float(input(mensaje))
                if numero >= 0:
                    return numero
                else:
                    print("El número debe ser mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

inventario = {}

codigo = validar_texto("Ingresa el código del producto: ")
nombre = validar_texto("Ingresa el nombre del producto: ")
cantidad = validar_numero("Ingresa la cantidad en stock: ", tipo="int")
precio = validar_numero("Ingresa el precio: ")

inventario[codigo] = {
    "nombre": nombre,
    "cantidad": cantidad,
    "precio": precio
}

print("\nInventario creado:")
print(f"Código: {codigo}")
print(f"Nombre: {inventario[codigo]['nombre']}")
print(f"Cantidad en stock: {inventario[codigo]['cantidad']}")
print(f"Precio: ${inventario[codigo]['precio']:.2f}")
print(f"\nDiccionario completo: {inventario}") """


### Ejercicio 6
# Crear una lista con 5 números enteros ingresados por el usuario
# Luego: Muestra la lista completa, Muestra el número mayor y el número menor de la lista
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 6")
def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

numeros = []
for i in range(5):
    num = validar_numero(f"Ingresa el número {i+1}: ")
    numeros.append(num)

print(f"\nLista completa: {numeros}")
print(f"Número mayor: {max(numeros)}")
print(f"Número menor: {min(numeros)}") """


### Ejercicio 7
# Crear una tupla que contenga los días de la semana
# Luego: Muestra el primer día, Muestra el último día, Indica cuántos días tiene la tupla (len)
### JUAN PABLO FLORES DÍAZ
""" print("EJERCICIO 7")
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

print(f"Tupla de días de la semana: {dias_semana}")
print(f"Primer día: {dias_semana[0]}")
print(f"Último día: {dias_semana[-1]}")
print(f"Cantidad de días en la tupla: {len(dias_semana)}") """


### Ejercicio 8
# Crea una función llamada calcular_promedio que:
# Reciba 3 números como parámetros ingresados por el usuario
# Calcule el promedio y Retorne el resultado
# Después, llamar a la función y mostrar el promedio en pantalla
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 8")
def validar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

numero1 = validar_numero("Ingresa el primer número: ")
numero2 = validar_numero("Ingresa el segundo número: ")
numero3 = validar_numero("Ingresa el tercer número: ")

promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio de {numero1}, {numero2} y {numero3} es: {promedio:.2f}")
