import tkinter as tk
import random as rnd


# Clase padre
class Mascota:
    total_mascotas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.x = rnd.randint(50, 580)
        self.y = rnd.randint(50, 300)
        self.sword_x = rnd.randint(10, 30)
        self.sword_y = rnd.randint(10, 30)
        Mascota.total_mascotas += 1

    def mover(self):
        self.sword_x = rnd.randint(-20, 20)
        self.sword_y = rnd.randint(-20, 20)
        self.x += self.sword_x
        self.y += self.sword_y

        # Mantener dentro del canvas
        self.x = max(20, min(620, self.x))
        self.y = max(20, min(330, self.y))

    def obtener_emoji(self):
        return "?"


# Crear las clases hijas
class Perro(Mascota):
    def obtener_emoji(self):
        return "🐕"


class Gato(Mascota):
    def obtener_emoji(self):
        return "😺"


class Serpiente(Mascota):
    def obtener_emoji(self):
        return "🐍"


# Crear la ventana
mascotas = []

ventana = tk.Tk()
ventana.title("Mascotas Virtuales")
ventana.geometry("700x500")

canvas = tk.Canvas(ventana, width=650, height=350, bg="white")
canvas.pack(pady=10)

info = tk.Label(ventana, text="Sin mascotas")
info.pack()


# Dibujar las mascotas
def dibujar_mascotas():
    canvas.delete("all")

    for mascota in mascotas:
        canvas.create_text(
            mascota.x,
            mascota.y,
            text=mascota.obtener_emoji(),
            font=("Arial", 25)
        )
        canvas.create_text(
            mascota.x,
            mascota.y + 25,
            text=mascota.nombre,
            font=("Arial", 8)
        )

    info.config(text="Mascotas: " + str(Mascota.total_mascotas))


# Agregar mascotas
def agregar_perro():
    mascotas.append(
        Perro("Perro")
    )
    info.config(
        text="Mascotas: " + str(Mascota.total_mascotas)
    )
    dibujar_mascotas()


def agregar_gato():
    mascotas.append(
        Gato("Gato")
    )
    info.config(
        text="Mascotas: " + str(Mascota.total_mascotas)
    )
    dibujar_mascotas()


def agregar_serpiente():
    mascotas.append(
        Serpiente("Serpiente")
    )
    info.config(
        text="Mascotas: " + str(Mascota.total_mascotas)
    )
    dibujar_mascotas()


# Mover mascotas
def mover_mascotas():
    for mascota in mascotas:
        mascota.mover()

    dibujar_mascotas()
    ventana.after(500, mover_mascotas)


# Botones
btn_perro = tk.Button(
    ventana,
    text="Agregar Perro",
    command=agregar_perro
)
btn_perro.pack(side="left", padx=10)

btn_gato = tk.Button(
    ventana,
    text="Agregar Gato",
    command=agregar_gato
)
btn_gato.pack(side="left", padx=10)

btn_serpiente = tk.Button(
    ventana,
    text="Agregar Serpiente",
    command=agregar_serpiente
)
btn_serpiente.pack(side="left", padx=10)

# Iniciar
mover_mascotas()
ventana.mainloop()
