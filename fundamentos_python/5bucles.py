
# =============================================================================
# 5. BUCLES (Repetir código)
# =============================================================================
print("\n" + "=" * 60)
print("5. BUCLES (Repetir código)")
print("=" * 60)

# -------------------- FOR --------------------
print("\n--- FOR (repetir N veces) ---")
print("Se usa cuando sabes cuántas veces repetir")

print("\nfor i in range(5):")
print("print('Iteración', i)")
print("\nResultado:")
# Recordando los argumentos que pide el for de manera general: 
# for (palabra reservada) variable (índice) in (palabra reservada) rango (función que genera una secuencia de números):
for i in range(5):
    print("Iteración", i)

print("\nrange(inicio, fin, paso):")
print("for i in range(0, 10, 2):  # 0, 2, 4, 6, 8")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Ejemplo con input:
n = int(input("\n¿Cuántas veces quieres saludar? "))
saludo = input("¿Qué saludo quieres usar? ")
print(f"\nRepetir saludo '{saludo}' {n} veces:")
for i in range(n):
    print(f"{saludo} {i + 1}!")

# -------------------- WHILE --------------------
print("\n--- WHILE (repetir mientras se cumpla condición) ---")
print("Se usa cuando no sabes cuántas veces repetir")

print("\ncontador = 0")
print("while contador < 3:")
print("    print('Contador:', contador)")
print("    contador += 1")
print("\nResultado:")
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Ejemplo con input:
print("\nContador personalizado:")
limite = int(input("¿Hasta qué número contar? "))
contador = 0
while contador < limite:
    print("Contador:", contador)
    contador += 1

# -------------------- BREAK y CONTINUE --------------------
print("\n--- BREAK (salir del bucle) y CONTINUE (saltar iteración) ---")
print("\nfor i in range(10):")
print("    if i == 3:")
print("        break  # Sale del bucle")
print("\nResultado:")
for i in range(10):
    if i == 3:
        print("¡Break en", i, "!")
        break
    print(i, end=" ")
print()

# Ahora con continue
print("\nfor i in range(10):")
print("    if i % 2 == 0:")
print("        continue  # Salta a la siguiente iteración")
print("\nResultado:")
for i in range(10):
    if i % 2 == 0:
        print("¡Continue en", i, "!")
        continue
    print(i, end=" ")
print()
print("\n¡FIN DE LOS BUCLES!")