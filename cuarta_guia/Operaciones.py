# operaciones.py
# Módulo con funciones matemáticas básicas

def suma(a, b):
    """Retorna la suma de dos números"""
    return a + b

def resta(a, b):
    """Retorna la resta de dos números"""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicación de dos números"""
    return a * b

def division(a, b):
    """Retorna la división de dos números, maneja división por cero"""
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b