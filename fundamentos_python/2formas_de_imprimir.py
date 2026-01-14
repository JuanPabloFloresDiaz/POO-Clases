# =============================================================================
# 2. IMPRIMIR EN PANTALLA (print)
# =============================================================================
print("\n" + "=" * 60)
print("2. FORMAS DE IMPRIMIR (print)")
print("=" * 60)

nombre = "Ana"
edad = 25

print("\n--- Método 1: Print simple ---")
print("print('Hola')")
print("Resultado: Hola")

print("\n--- Método 2: Print con comas (separa con espacios) ---")
print("print('Nombre:', nombre, 'Edad:', edad)")
print("Resultado: Nombre:", nombre, "Edad:", edad)

print("\n--- Método 3: F-STRINGS (más legible pero NO obligatorio) ---")
print("Con f-string: print(f'Hola {nombre}, tienes {edad} años')") 
# La 'f' antes de las comillas indica que es una f-string, la f significa 'formatted' (formateado)
print("Sin f-string: print('Hola', nombre, ', tienes', edad, 'años')")
print("\n¡AMBAS FORMAS FUNCIONAN IGUAL!")
print("\nNOTA IMPORTANTE:")
print("• La 'f' NO es obligatoria")
print("• La 'f' solo hace el código más legible")
print("• Es una característica nueva desde Python 3.6")
print("• Puedes usar la forma que prefieras")

# Ejemplos funcionales:
print("\nEjemplos funcionales:")
print(f"Hola {nombre}, tienes {edad} años")  # Usando f-string
print("Hola", nombre, ", tienes", edad, "años")  # Sin f-string
print("Hola " + nombre + ", tienes " + str(edad) + " años")