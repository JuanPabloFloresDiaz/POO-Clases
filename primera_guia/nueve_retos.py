## Ejercicio 1
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 1")
print('"Estoy"\n""aprendiendo""\n"""Python"""')

## Ejercicio 2
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 2")
print("1","2","3","4","5", sep="-")

## Ejercicio 3
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 3")
end = ""
print("1","2","3","4","5", "final de la línea", end=end)

## Ejercicio 4
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 4")
end = ""
print("manzana","banana","cereza en la lista de frutas", sep=", ", end=end)

## Ejercicio 5  
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 5")
Victoria = 3
Carlos = 5
Josue = 6
print(f"Victoria tiene {Victoria} manzanas", f"Carlos tiene {Carlos} manzanas", f"Josue tiene {Josue} manzanas", sep=", ")
total_manzanas = Victoria + Carlos + Josue
print(f"En total, tienen {total_manzanas} manzanas")

## Ejercicio 6
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 6")
def validate_number(mensaje, value_min=None, value_max=None):
    while True:
        try:
            number = float(input(mensaje))
            if value_min is not None and number <= value_min:
                print(f"El número debe ser mayor o igual a {value_min}. Inténtalo de nuevo.")
                continue
            if value_max is not None and number >= value_max:
                print(f"El número debe ser menor o igual a {value_max}. Inténtalo de nuevo.")
                continue
            else: return number
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")

num1 = validate_number("Ingresa el primer número: ", value_min=0)
num2 = validate_number("Ingresa el segundo número: ", value_min=0)

print(f"La suma de {num1} y {num2} es {num1 + num2}\n"
      f"La resta de {num1} y {num2} es {num1 - num2}\n"
      f"La multiplicación de {num1} y {num2} es {num1 * num2}\n"
      f"La división de {num1} y {num2} es {num1 / num2}")

## Ejercicio 7
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 7")
horas = validate_number("Ingresa el número de horas: ")
minutos = horas * 60
segundos = horas * 3600
print(f"{horas} horas son {minutos} minutos o {segundos} segundos")

### Ejercicio 8
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 8")
celsius = validate_number("Ingresa la temperatura en grados Celsius: ")
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

### Ejercicio 9
### JUAN PABLO FLORES DÍAZ
print("EJERCICIO 9")
x = validate_number("Ingresa el valor de la entrada de la muestra: ")
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print(f"El resultado de la expresión 1/x + 1/x + 1/x + 1/x para x = {x} es {y}")