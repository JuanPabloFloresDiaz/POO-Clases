# =============================================================================
# 3. ENTRADA DE DATOS (input)
# =============================================================================
print("\n" + "=" * 60)
print("3. PEDIR DATOS AL USUARIO (input)")
print("=" * 60)

print("\nEjemplos de código (comentados para no interrumpir):")
print("nombre = input('¿Cómo te llamas? ')")
print("edad = int(input('¿Cuántos años tienes? '))")
print("print('Hola', nombre, ', tienes', edad, 'años')")
print("\nNOTA: input() SIEMPRE devuelve un string")
print("Si necesitas un número, usa int() o float()")

# Ejemplo de uso real de input
nombre = input("\n¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
print(f"Hola {nombre}, tienes {edad} años")

# Para el caso de int y float, se explicara con un ejemplo real
altura = float(input("¿Cuánto mides (en metros)? "))
print(f"Mides {altura} metros") 
print(f"Redondeando tu altura: {round(altura, 2)} metros")

# En conclusión para valor int o float con input, debes de usar la función int() o float()
# y luego pasarle como parámetro el input() para que convierta el string a número.
# Se simplifica a realizar un parseInt o parseDouble como en otros lenguajes.