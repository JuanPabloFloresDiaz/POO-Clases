# Ejercicio 1:
# Crear una clase Auto con atributos: marca, modelo, anio, color
class Auto:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
# Crear una clase Garage con atributos: capacidad y una lista de autos
class Garage:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.autos = []
# Agregar un auto al garage
    def agregar_auto(self, auto):
        if len(self.autos) < self.capacidad:
            self.autos.append(auto)
            print("Auto agregado al garage")
        else:
            print("El garage esta lleno")
# Retirar un auto del garage
    def retirar_auto(self, auto):
        if auto in self.autos:
            self.autos.remove(auto)
            print("Auto retirado del garage")
        else:
            print("El auto no esta en el garage")
# Imprimir los autos del garage
    def imprimir_autos(self):
        print("Autos en el garage:")
        for auto in self.autos:
            print(auto.marca, auto.modelo, auto.anio, auto.color)
# Crear un garage con capacidad para 3 autos
mi_garage = Garage(3)
# Crear 3 autos
auto1 = Auto("Toyota", "Corolla", 2022, "Negro")
auto2 = Auto("Honda", "Civic", 2023, "Blanco")
auto3 = Auto("Ford", "Focus", 2021, "Gris")
# Agregar los autos al garage
mi_garage.agregar_auto(auto1)
mi_garage.agregar_auto(auto2)
mi_garage.agregar_auto(auto3)
# Imprimir los autos del garage
mi_garage.imprimir_autos()
# Ejercicio 2:
# Crear una clase Persona con atributos: nombre, edad, genero
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    # Metodo imprimir persona
    def imprimir_persona(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Genero: ", self.genero)
# Crear una clase ListaPersonas con atributos: capacidad y una lista de personas
class ListaPersonas:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.personas = []
# Agregar una persona a la lista
    def agregar_persona(self, persona):
        if len(self.personas) < self.capacidad:
            self.personas.append(persona)
            print("Persona agregada a la lista")
        else:
            print("La lista esta llena")
# Retirar una persona de la lista
    def retirar_persona(self, persona):
        if persona in self.personas:
            self.personas.remove(persona)
            print("Persona retirada de la lista")
        else:
            print("La persona no esta en la lista")
# Imprimir las personas de la lista
    def imprimir_personas(self):
        print("Personas en la lista:")
        for persona in self.personas:
            persona.imprimir_persona()
# Crear una lista de personas con capacidad para 3 personas
mi_lista = ListaPersonas(3)
# Crear 3 personas
persona1 = Persona("Juan", 25, "Masculino")
persona2 = Persona("Maria", 30, "Femenino")
persona3 = Persona("Pedro", 35, "Masculino")
# Agregar las personas a la lista
mi_lista.agregar_persona(persona1)
mi_lista.agregar_persona(persona2)
mi_lista.agregar_persona(persona3)
# Imprimir las personas de la lista
mi_lista.imprimir_personas()
