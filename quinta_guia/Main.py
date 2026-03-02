from Teclado import Teclado

# #Reto 1
# # Convertir caracteres a código ASCII (ord)
# # Pide al usuario una palabra y muestra el código ASCII del primer carácter.
# # Debes usar ord().

# print("=" * 50)
# print("RETO 1: Código ASCII de un carácter")
# print("=" * 50)
# palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)
# primer_caracter = palabra[0]
# codigo_ascii = ord(primer_caracter)
# print(f"El código ASCII del primer carácter '{primer_caracter}' es: {codigo_ascii}")
# print()

# # Reto 2
# # Convertir código ASCII a carácter (chr)
# # Pide un número al usuario y conviértelo en su carácter correspondiente.
# # Usa chr() y maneja errores con try-except.

# print("=" * 50)
# print("RETO 2: Carácter desde código ASCII")
# print("=" * 50)
# try:
#     codigo = Teclado.read_integer("Ingrese un código ASCII:", min_value=0, max_value=1114111)
#     caracter = chr(codigo)
#     print(f"El carácter correspondiente al código {codigo} es: '{caracter}'")
# except ValueError as e:
#     print(f"Error: {e}")
# print()

# # Reto 3
# # Extraer parte de una cadena (slice)
# # Pide una frase y muestra:
# # •	Los primeros 5 caracteres
# # •	Los últimos 4 caracteres
# # Usa slicing.

# print("=" * 50)
# print("RETO 3: Slicing de cadenas")
# print("=" * 50)
# frase = Teclado.read_text("Ingrese una frase:", min_length=5)
# print(f"Frase completa: {frase}")
# print(f"Primeros 5 caracteres: {frase[:5]}")
# if len(frase) >= 4:
#     print(f"Últimos 4 caracteres: {frase[-4:]}")
# else:
#     print(f"Últimos caracteres: {frase}")
# print()

# # Reto 4
# # Buscar palabra con in y not in
# # Pide una frase y una palabra.
# # •	Si la palabra está en la frase, muestra: “La palabra existe”
# # •	Si no está, muestra: “La palabra no existe”
# # Usa in y not in.
# print("=" * 50)
# print("RETO 4: Buscar palabra en frase")
# print("=" * 50)
# frase = Teclado.read_text("Ingrese una frase:", min_length=1)
# palabra = Teclado.read_text("Ingrese una palabra a buscar:", min_length=1)
# if palabra in frase:
#     print("La palabra existe")
# if palabra not in frase:
#     print("La palabra no existe")
# print()

# # Reto 5
# # Carácter mínimo y máximo
# # Pide una palabra y muestra:
# # •	El carácter menor usando min()
# # •	El carácter mayor usando max()

# print("=" * 50)
# print("RETO 5: Carácter mínimo y máximo")
# print("=" * 50)
# palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)
# print(f"Palabra: {palabra}")
# print(f"Carácter menor: {min(palabra)}")
# print(f"Carácter mayor: {max(palabra)}")
# print()

# # Reto 6
# # Buscar posición con index()
# # Pide una palabra y una letra.
# # •	Muestra la posición de esa letra usando index()
# # •	Usa try-except para evitar error si no existe

# print("=" * 50)
# print("RETO 6: Buscar posición con index()")
# print("=" * 50)
# palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)
# letra = Teclado.read_text("Ingrese una letra a buscar:", min_length=1, max_length=1)
# try:
#     posicion = palabra.index(letra)
#     print(f"La letra '{letra}' se encuentra en la posición: {posicion}")
# except ValueError:
#     print(f"La letra '{letra}' no se encuentra en la palabra '{palabra}'")
# print()

# # Reto 7
# # Pide una palabra y muéstrala centrada en 20 espacios usando center().

# print("=" * 50)
# print("RETO 7: Centrar palabra")
# print("=" * 50)
# palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)
# palabra_centrada = palabra.center(20)
# print(f"Palabra original: '{palabra}'")
# print(f"Palabra centrada: '{palabra_centrada}'")
# print(f"Con asteriscos: |{palabra.center(20, '*')}|")
# print()

# # Reto 8
# # Pide un nombre de archivo y verifica si termina en:
# # •	.txt
# # •	.py
# # Usa endswith()

# print("=" * 50)
# print("RETO 8: Verificar extensión de archivo")
# print("=" * 50)
# archivo = Teclado.read_text("Ingrese un nombre de archivo:", min_length=1)
# if archivo.endswith('.txt'):
#     print(f"El archivo '{archivo}' es un archivo de texto (.txt)")
# elif archivo.endswith('.py'):
#     print(f"El archivo '{archivo}' es un archivo de Python (.py)")
# else:
#     print(f"El archivo '{archivo}' no es .txt ni .py")
# print()

# # Reto 9
# # Comparaciones de cadenas
# # Pide dos palabras y muestra:
# # •	Si son iguales (==)
# # •	Si son diferentes (!=)
# # •	Cuál es mayor alfabéticamente (>)

# print("=" * 50)
# print("RETO 9: Comparaciones de cadenas")
# print("=" * 50)
# palabra1 = Teclado.read_text("Ingrese la primera palabra:", min_length=1)
# palabra2 = Teclado.read_text("Ingrese la segunda palabra:", min_length=1)
# print(f"Palabra 1: {palabra1}")
# print(f"Palabra 2: {palabra2}")
# print(f"Son iguales (==): {palabra1 == palabra2}")
# print(f"Son diferentes (!=): {palabra1 != palabra2}")
# if palabra1 > palabra2:
#     print(f"'{palabra1}' es mayor alfabéticamente que '{palabra2}'")
# elif palabra1 < palabra2:
#     print(f"'{palabra2}' es mayor alfabéticamente que '{palabra1}'")
# else:
#     print("Son iguales alfabéticamente")
# print()

# Reto 10
# Ordenar letras de una palabra
# Pide una palabra y:
# •	Muéstrala ordenada usando sorted()
# •	Conviértela en lista y usa sort()
# Explica la diferencia entre sorted() y sort().

print("=" * 50)
print("RETO 10: Ordenar letras de una palabra")
print("=" * 50)
palabra = Teclado.read_text("Ingrese una palabra:", min_length=1)

# Usando sorted() - retorna una nueva lista ordenada
ordenada_sorted = sorted(palabra)
print(f"Palabra original: {palabra}")
print(f"Usando sorted(): {ordenada_sorted}")
print(f"Como cadena: {''.join(ordenada_sorted)}")

# Usando sort() - modifica la lista original
lista_letras = list(palabra)
print(f"\nLista antes de sort(): {lista_letras}")
lista_letras.sort()
print(f"Lista después de sort(): {lista_letras}")
print(f"Como cadena: {''.join(lista_letras)}")

print("\nDiferencia:")
print("- sorted(): Retorna una NUEVA lista ordenada sin modificar el original")
print("- sort(): Modifica la lista ORIGINAL y no retorna nada (None)")
print()
