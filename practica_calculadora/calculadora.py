print("CALCULADORA")

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
def potencia(a, b):
    return a ** b
def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de número negativo"
    return a ** 0.5
def raiz_cubica(a):
    return a ** (1/3)
def porcentaje(a, b):
    return (a / 100) * b

print("Operaciones disponibles:"
      "\n1. Sumar"
      "\n2. Restar"
      "\n3. Multiplicar"
      "\n4. Dividir"
      "\n5. Potencia"
      "\n6. Raíz Cuadrada"
      "\n7. Raíz Cúbica"
      "\n8. Porcentaje"
      "\n9. Salir")
while True:
    try:
        operacion = int(input("Seleccione una operación (1-9): "))
        if operacion in [1, 2, 3, 4, 5, 8]:
            while True:
                try:
                    a = float(input("Ingrese el primer número: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            while True:
                try:
                    b = float(input("Ingrese el segundo número: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            if operacion == 1:
                print("Resultado:", sumar(a, b))
            elif operacion == 2:
                print("Resultado:", restar(a, b))
            elif operacion == 3:
                print("Resultado:", multiplicar(a, b))
            elif operacion == 4:
                print("Resultado:", dividir(a, b))
            elif operacion == 5:
                print("Resultado:", potencia(a, b))
            elif operacion == 8:
                print("Resultado:", porcentaje(a, b))
        elif operacion == 6:
            while True:
                try:
                    a = float(input("Ingrese el número: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            print("Resultado:", raiz_cuadrada(a))
        elif operacion == 7:
            while True:
                try:
                    a = float(input("Ingrese el número: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            print("Resultado:", raiz_cubica(a))
        elif operacion == 9:
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        else:
            print("Operación no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Debe ingresar un número válido para la operación.")
