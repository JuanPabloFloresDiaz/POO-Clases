
# =============================================================================
# 6. LISTAS (Arrays/Arreglos)
# =============================================================================
print("\n" + "=" * 60)
print("6. LISTAS (Colecciones de elementos)")
print("=" * 60)

print("\nLas listas guardan múltiples valores en orden")

# -------------------- Crear y acceder --------------------
print("\n--- Crear listas ---")
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]
mixta = [1, "texto", 3.14, True]

print("numeros =", numeros)
print("frutas =", frutas)
print("mixta =", mixta)

print("\n--- Acceder a elementos (índices empiezan en 0) ---")
print("frutas[0]  ->", frutas[0]) # Primer elemento
print("frutas[1]  ->", frutas[1]) # Segundo elemento
print("frutas[-1] ->", frutas[-1]) # Último elemento
print("frutas[0:2] ->", frutas[0:2]) # Slice (sublista)

# -------------------- Modificar listas --------------------
print("\n--- Métodos para modificar listas ---")
print("\nLista inicial:", frutas)

frutas.append("naranja")
print("append('naranja') ->", frutas)

frutas.insert(1, "kiwi")
print("insert(1, 'kiwi') ->", frutas)

frutas.remove("banana")
print("remove('banana') ->", frutas)

ultimo = frutas.pop()
print("pop() quita último ->", frutas, "(quitó:", ultimo + ")")

print("len(frutas) ->", len(frutas), "elementos")

# -------------------- Iterar listas (FOREACH) --------------------
print("\n--- Recorrer listas (FOREACH en Python es FOR) ---")
colores = ["rojo", "verde", "azul"]

print("\nfor color in colores:")
print("    print(color)")
print("\nResultado:")
for color in colores:
    print(color)

print("\n--- Con índice (enumerate) ---")
print("for i, color in enumerate(colores):")
print("    print(i, color)")
print("\nResultado:")
for i, color in enumerate(colores):
    print(i, color)

# Ejemplo basico de agregar a una lista con input
print("\n--- Agregar elementos a una lista con input ---")
nueva_lista = []
n = int(input("¿Cuántos elementos quieres agregar a la lista? "))
for i in range(n):
    elemento = input(f"Elemento {i + 1}: ")
    nueva_lista.append(elemento)
print("Lista final:", nueva_lista)