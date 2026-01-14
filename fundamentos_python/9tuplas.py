
# =============================================================================
# 9. Tuplas
# =============================================================================
# -------------------- Tuplas (listas inmutables) --------------------
print("\n--- TUPLAS (no se pueden modificar) ---")
coordenadas = (10, 20)
print("coordenadas = (10, 20)")
print("coordenadas[0] ->", coordenadas[0])
print("\nNOTA: Las tuplas NO permiten append, remove, etc.")

# Ejemplo práctico de uso de tuplas
print("\n--- Ejemplo práctico de tuplas ---")
def obtener_coordenadas():
    return (15, 30)
x, y = obtener_coordenadas()
print(f"Coordenadas obtenidas: x={x}, y={y}")
# Las tuplas son útiles para devolver múltiples valores de una función
# o para agrupar datos que no deben cambiar.
# Ejemplo básico de crear una tupla con input
print("\n--- Crear tupla con input ---")
valores = []
n = int(input("¿Cuántos valores quieres en la tupla? "))
for i in range(n):
    valor = input(f"Valor {i + 1}: ")
    valores.append(valor)
mi_tupla = tuple(valores)
print("Tupla resultante:", mi_tupla)