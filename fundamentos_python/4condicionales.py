# =============================================================================
# 4. CONDICIONALES (if, elif, else)
# =============================================================================
print("\n" + "=" * 60)
print("4. CONDICIONALES (Tomar decisiones)")
print("=" * 60)

print("\nPermiten ejecutar código según condiciones:")

edad = 18
print("edad = 18")
print("\nif edad < 18:")
print("print('Menor de edad')")
print("elif edad == 18:")
print("print('Acabas de ser mayor')")
print("else:")
print("print('Mayor de edad')")
if edad < 18:
    print("\nResultado: Menor de edad")
elif edad == 18:
    print("\nResultado: Acabas de ser mayor")
else:
    print("\nResultado: Mayor de edad")

print("\n--- Operadores de comparación ---")
print("== igual a")
print("!= diferente de")
print("> mayor que")
print("< menor que")
print(">= mayor o igual")
print("<= menor o igual")
print("\n--- Operadores lógicos ---")
print("and (y) - Ambas condiciones deben ser True")
print("or (o) - Al menos una debe ser True")
print("not (no) - Invierte el valor")

# Ahora ejemplo con input
edad_usuario = int(input("\n¿Cuántos años tienes? "))
if edad_usuario < 18:
    print("Eres menor de edad.")
elif edad_usuario == 18:
    print("Acabas de ser mayor de edad.")
else:
    print("Eres mayor de edad.")