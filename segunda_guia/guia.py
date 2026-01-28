### Reto 1
# Crea un programa que pida al usuario un número entero y determine si es par o impar.
### JUAN PABLO FLORES DÍAZ
""" print("RETO 1")
while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.") """


### Reto 2
# Crea un programa que pida tres números al usuario y determine cuál es el mayor de los tres.
### JUAN PABLO FLORES DÍAZ
""" print("RETO 2")
def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
            
numero1 = obtener_numero("Ingresa el primer número: ")
numero2 = obtener_numero("Ingresa el segundo número: ")
numero3 = obtener_numero("Ingresa el tercer número: ")
mayor = max(numero1, numero2, numero3)
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es {mayor}.") """

### Reto 3
#Crea un programa que lea una calificación (número entre 0 y 10) y determine si el estudiante ha aprobado (A y B) o no, y además qué calificación le corresponde (A, B, C, D, E, F).
#9-10     A
#7-8      B
#5-6      C
#3-4      D
#1-2      E
#0        F
### JUAN PABLO FLORES DÍAZ
""" print("RETO 3")
def obtener_calificacion(mensaje):
    while True:
        try:
            calificacion = float(input(mensaje))
            if 0 <= calificacion <= 10:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
            
calificacion = obtener_calificacion("Ingresa la calificación (0-10): ")

match calificacion:
    case calificacion if 9 <= calificacion <= 10:
        letra = "A"
    case calificacion if 7 <= calificacion < 9:
        letra = "B"
    case calificacion if 5 <= calificacion < 7:
        letra = "C"
    case calificacion if 3 <= calificacion < 5:
        letra = "D"
    case calificacion if 1 <= calificacion < 3:
        letra = "E"
    case 0:
        letra = "F" 
if letra in ["A", "B"]:
    estado = "aprobado"
else:
    estado = "no aprobado"
print(f"El estudiante está {estado} con una calificación {letra}.") """

### Reto 4
#Crea un programa que determine el precio de un boleto de cine según la edad del usuario. 
#Si la persona es menor de 12 años o mayor de 65, el boleto cuesta $5. 
#Si tiene entre 12 y 65 años, el boleto cuesta $10.
### JUAN PABLO FLORES DÍAZ
""" print("RETO 4")
def obtener_edad(mensaje):
    while True:
        try:
            edad = int(input(mensaje))
            if edad >= 0:
                return edad
            else:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

edad = obtener_edad("Ingresa tu edad: ")
if edad < 12 or edad > 65:
    precio = 5
else:
    precio = 10
print(f"El precio del boleto de cine es: ${precio}.") """

### Reto 5
#Crea un programa que pida un año y determine si es bisiesto.
#“Un año es bisiesto si es divisible por 4(residuo 0) y no por 100, o si es divisible por 400”. 
### JUAN PABLO FLORES DÍAZ
""" print("RETO 5")
def obtener_año(mensaje):
    while True:
        try:
            año = int(input(mensaje))
            if año >= 0:
                return año
            else:
                print("El año no puede ser negativo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

año = obtener_año("Ingresa un año: ")
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.") """

### Reto 6
#Crear un bucle que solicite ingresar una palabra y que salga del bucle hasta ingresar la palabra “Python” e imprimir “Saliste del bucle”
### JUAN PABLO FLORES DÍAZ
""" print("RETO 6")
while True:
    palabra = input("Ingresa una palabra (ingresa 'Python' para salir): ")
    if palabra == "Python":
        print("Saliste del bucle")
        break
    else:
        print("Palabra incorrecta, intenta de nuevo.") """

### Reto 7
#Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. 
#Están construyendo una pirámide.
#Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. 
#La pirámide se apila de acuerdo con un principio simple:
#Cada capa inferior contiene un bloque más que la capa superior.
#La figura ilustra la regla utilizada por los constructores:
#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
#Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
#Datos de prueba:
#   Bloques –    Capas
#    6             3
#    20            5
#   1000           44
### JUAN PABLO FLORES DÍAZ
""" print("RETO 7")
def obtener_bloques(mensaje):
    while True:
        try:
            bloques = int(input(mensaje))
            if bloques >= 0:
                return bloques
            else:
                print("La cantidad de bloques no puede ser negativa. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
bloques = obtener_bloques("Ingresa la cantidad de bloques disponibles: ")
capas = 0
bloques_necesarios = 1
while bloques >= bloques_necesarios:
    capas += 1
    bloques -= bloques_necesarios
    bloques_necesarios += 1
print(f"La altura máxima de la pirámide que se puede construir es de {capas} capas.") """

### Reto 8
#En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:
#1.	toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
#2.	si es par, evalúa un nuevo c0 como c0 ÷ 2;
#3.	de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
#4.	si c0 ≠ 1, salta al punto 2.
#La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
### JUAN PABLO FLORES DÍAZ
print("RETO 8")
def obtener_numero_positivo(mensaje):
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
print("La secuencia de Collatz es:" + " -> ".join(map(str, secuencia)))
