## Reto 1
### JUAN PABLO FLORES DÍAZ
class Libro:
    # Variable de clase
    total_libros = 0

    def __init__(self, titulo, paginas):
        # Atributos de instancia
        self.titulo = titulo
        self.paginas = paginas
        # Incremento de la variable de clase cada vez que se crea un objeto
        Libro.total_libros += 1

# Creación de 3 libros
l1 = Libro("Cien años de soledad", 471)
l2 = Libro("Don Quijote", 863)
l3 = Libro("El Principito", 96)

# Impresión de resultados
print("Total de libros:", Libro.total_libros)
print(l1.__dict__)
print(l2.__dict__)
print(l3.__dict__)

## Reto 2
### JUAN PABLO FLORES DÍAZ
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __add__(self, otro):
        # Retorna la suma de los atributos precio de ambos objetos
        return self.precio + otro.precio

# Creación de productos
p1 = Producto("Laptop", 800)
p2 = Producto("Mouse", 25)

# Resultados
print("Suma de precios:", p1 + p2)
print(p1.__dict__)
print(p2.__dict__)

## Reto 3
### JUAN PABLO FLORES DÍAZ
class Estudiante:
    activos = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Estudiante.activos += 1
        print(f"Estudiante {self.nombre} creado. Activos: {Estudiante.activos}")

    def __del__(self):
        Estudiante.activos -= 1
        print(f"Estudiante {self.nombre} eliminado. Activos restantes: {Estudiante.activos}")

# Creación de estudiantes
e1 = Estudiante("Juan")
e2 = Estudiante("Maria")

# Eliminar uno con del
del e1

## Reto 4
### JUAN PABLO FLORES DÍAZ
class Item:
    total_items = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Item.total_items += 1

    def __add__(self, otro):
        # Devuelve un nuevo Item que representa el total
        return Item("Total Acumulado", self.precio + otro.precio)

# Creación de objetos
i1 = Item("Manzana", 0.5)
i2 = Item("Pan", 1.0)
i3 = Item("Leche", 1.5)

# Acumular total usando +
total = i1 + i2 + i3

print("Total de items creados:", Item.total_items)
print("Suma total de precios:", total.precio)
print("Dict de i1:", i1.__dict__)

## Reto 5
### JUAN PABLO FLORES DÍAZ
class Persona:
    cantidad = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.cantidad += 1

    def __add__(self, otro):
        return self.edad + otro.edad

    def __del__(self):
        Persona.cantidad -= 1

# Ejecución
p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

print("Dict p1:", p1.__dict__)
print("Dict p2:", p2.__dict__)
print("Suma de edades:", p1 + p2)
print("Cantidad actual:", Persona.cantidad)

del p1
print("Cantidad tras eliminar a p1:", Persona.cantidad)