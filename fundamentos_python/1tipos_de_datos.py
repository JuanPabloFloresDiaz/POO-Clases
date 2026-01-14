
# =============================================================================
# 1. TIPOS DE DATOS BÁSICOS
# =============================================================================
print("\n" + "=" * 60)
print("1. TIPOS DE DATOS BÁSICOS")
print("=" * 60)

# -------------------- STRINGS (Cadenas de texto) --------------------
print("\n--- STRINGS (Texto) ---")
print("Los strings son cadenas de texto. Se crean con comillas:")

texto = "Hola mundo"
print("texto = 'Hola mundo'")
print("Valor:", texto)
print("Tipo:", type(texto))  # <class 'str'> // type detecta el tipo de dato automaticamente

# Métodos útiles de strings
print("\nMétodos útiles:")
print("texto.upper() ->", texto.upper()) # HOLA MUNDO (poner todo en mayúsculas)
print("texto.lower() ->", texto.lower()) # hola mundo (poner todo en minúsculas)
print("texto.split() ->", texto.split()) # ['Hola', 'mundo'] (dividir en palabras)
print("len(texto) ->", len(texto), "caracteres") # longitud del texto

# -------------------- INTEGERS (Números enteros) --------------------
print("\n--- INTEGERS (Enteros) ---")
print("Los int son números enteros (sin decimales):")

edad = 25
print("edad = 25")
print("Valor:", edad)
print("Tipo:", type(edad))  # <class 'int'> // type detecta el tipo de dato automaticamente

print("\nOperaciones matemáticas:")
numero1 = 10
numero2 = 5
numero3 = 3
numero4 = 2
print("10 + 5  =", numero1 + numero2) # Suma
print("10 - 5  =", numero1 - numero2) # Resta
print("10 * 5  =", numero1 * numero2) # Multiplicación
print("10 / 5  =", numero1 / numero2) # División (resultado: float)
print("10 // 3 =", numero1 // numero3) # División entera (resultado: int)
print("10 % 3  =", numero1 % numero3) # Módulo (residuo)
print("2 ** 3  =", numero4 ** numero3) # Potencia

# -------------------- FLOAT (Decimales/Double) --------------------
print("\n--- FLOAT (Decimales) ---")
print("Los float son números con decimales:")

precio = 19.99
pi = 3.14159
print("precio = " + str(precio)) # Se usa str() para convertir a string y mostrar
print("pi = " + str(pi)) # Se usa str() para convertir a string y mostrar
print("Valor precio:", precio)
print("Valor pi:", pi)
print("Valor precio + pi:", precio + pi) # Suma de float
print("Tipo:", type(precio))  # <class 'float'> // type detecta el tipo de dato automaticamente

print("\nRedondear:")
print("round(pi, 2) ->", round(pi, 2))  # 3.14

# -------------------- BOOLEAN (Verdadero/Falso) --------------------
print("\n--- BOOLEAN (Booleanos) ---")
print("Los bool solo tienen dos valores: True o False")

activo = True
terminado = False
print("activo = " + str(activo)) # Se usa str() para convertir a string y mostrar
print("terminado = " + str(terminado)) # Se usa str() para convertir a string y mostrar
print("Tipo:", type(activo))  # <class 'bool'> // type detecta el tipo de dato automaticamente

print("\nOperadores lógicos:")
print("True and False ->", True and False) # False (Recordando las tablas de verdad and solo es True si ambos son True)
print("True or False ->", True or False) # True (Recordando las tablas de verdad or es True si al menos uno es True)
print("not True ->", not True) # False (Invierte el valor)

# -------------------- NONE (Valor nulo) --------------------
print("\n--- NONE (Nulo) ---")
print("None representa 'sin valor' o 'vacío':")
resultado = None
print("resultado = None")
print("Valor:", resultado)