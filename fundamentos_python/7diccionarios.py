
# =============================================================================
# 7. DICCIONARIOS (Clave-Valor)
# =============================================================================
print("\n" + "=" * 60)
print("7. DICCIONARIOS (Pares clave-valor)")
print("=" * 60)

print("\nLos diccionarios guardan datos con una 'clave' para acceder:")

# -------------------- Crear y acceder --------------------
print("\n--- Crear diccionario ---")
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

print("persona =", persona)
print("\nAcceder por clave:")
print("persona['nombre'] ->", persona["nombre"])
print("persona['edad']   ->", persona["edad"])

# -------------------- Modificar diccionarios --------------------
print("\n--- Modificar diccionarios ---")
persona["edad"] = 26
print("Cambiar edad:", persona)

persona["profesion"] = "Ingeniero"
print("Agregar clave:", persona)

del persona["ciudad"]
print("Eliminar 'ciudad':", persona)

# -------------------- Iterar diccionarios --------------------
print("\n--- Recorrer diccionario ---")
print("for clave, valor in persona.items():")
print("    print(clave, ':', valor)")
print("\nResultado:")
for clave, valor in persona.items():
    print(clave, ":", valor)

# Ejemplo basico de agregar pares clave-valor a un diccionario con input
print("\n--- Agregar pares clave-valor con input ---")
mi_diccionario = {}
n = int(input("¿Cuántos pares clave-valor quieres agregar? "))
for i in range(n):
    clave = input(f"Clave {i + 1}: ")
    valor = input(f"Valor {i + 1}: ")
    mi_diccionario[clave] = valor
print("\nDiccionario resultante:", mi_diccionario)