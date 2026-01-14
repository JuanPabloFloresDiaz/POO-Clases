
# =============================================================================
# 10. OTROS CONCEPTOS IMPORTANTES
# =============================================================================


# -------------------- Sets (sin duplicados) --------------------
print("\n--- SETS (sin elementos duplicados) ---")
numeros_set = {1, 2, 3, 3, 3, 4, 5}
print("numeros_set = {1, 2, 3, 3, 3, 4, 5}")
print("Resultado ->", numeros_set, "(duplicados eliminados)")

# Ejemplo de uso de sets utilizando input
print("\n--- Crear set con input ---")
valores = []
n = int(input("¿Cuántos valores quieres agregar al set? "))
for i in range(n):
    valor = input(f"Valor {i + 1}: ")
    valores.append(valor)
mi_set = set(valores)
print("Set resultante (duplicados eliminados):", mi_set)

# -------------------- Conversión de tipos --------------------
print("\n--- CONVERSIÓN DE TIPOS ---")
print("int('123') ->", int("123")) # String a int
print("float('3.14') ->", float("3.14")) # String a float
print("str(123) ->", str(123)) # Int a string
print("list('abc') ->", list("abc")) # String a lista

# Ejemplo de conversión con input
print("\n--- Conversión con input ---")
edad_str = input("Introduce tu edad: ")
edad_int = int(edad_str)
print(f"Tienes {edad_int} años (tipo: {type(edad_int)})")


# -------------------- Try-Except (manejar errores) --------------------
print("\n--- MANEJO DE ERRORES (try-except) ---")
print("try:")
print("    numero = int('abc')  # Esto da error")
print("except ValueError:")
print("    print('Error: no es un número')")
print("\nResultado:")
try:
    numero = int("abc")
except ValueError:
    print("Error: no es un número")
    
# Ejemplo de manejo de errores con input
print("\n--- Manejo de errores con input ---")
while True:
    entrada = input("Introduce un número entero: ")
    try:
        numero = int(entrada)
        print(f"Has introducido el número {numero}")
        break
    except ValueError:
        print("Error: eso no es un número entero. Inténtalo de nuevo.")
# En conclusión, los sets eliminan duplicados, la conversión de tipos es sencilla
# y el manejo de errores con try-except es esencial para entradas de usuario.