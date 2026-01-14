
# =============================================================================
# 8. FUNCIONES (Reutilizar código)
# =============================================================================
print("\n" + "=" * 60)
print("8. FUNCIONES (Bloques de código reutilizables)")
print("=" * 60)

print("\nLas funciones agrupan código para usarlo múltiples veces")

# -------------------- Función simple --------------------
print("\n--- Función sin parámetros ---")
print("def saludar():")
print("    print('¡Hola!')")
print("\nsaludar()")

def saludar():
    print("¡Hola!")

print("Resultado:")
saludar()

# -------------------- Función con parámetros --------------------
print("\n--- Función con parámetros ---")
print("def saludar_nombre(nombre):")
print("    print('Hola', nombre)")
print("\nsaludar_nombre('Ana')")

def saludar_nombre(nombre):
    print("Hola", nombre)

print("Resultado:")
saludar_nombre("Ana")

# -------------------- Función con return --------------------
print("\n--- Función que devuelve valor (return) ---")
print("def sumar(a, b):")
print("    return a + b")
print("\nresultado = sumar(5, 3)")
print("print(resultado)")

def sumar(a, b):
    return a + b

print("Resultado:", sumar(5, 3))

# -------------------- Función con parámetro por defecto --------------------
print("\n--- Función con valor por defecto ---")
print("def saludar_con_edad(nombre, edad=18):")
print("    print(nombre, 'tiene', edad, 'años')")
print("\nsaludar_con_edad('Luis')")
print("saludar_con_edad('María', 25)")

def saludar_con_edad(nombre, edad=18):
    print(nombre, "tiene", edad, "años")

print("Resultado:")
saludar_con_edad("Luis")
saludar_con_edad("María", 25)

# Ejemplo de funciones para luego usar con input
print("\n--- Ejemplo de función con input ---")
def calcular_area_rectangulo(base, altura):
    return base * altura
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))
area = calcular_area_rectangulo(base, altura)
print(f"El área del rectángulo es: {area}")