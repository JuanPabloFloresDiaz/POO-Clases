import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Semáforo")
ventana.geometry("300x600")

# Crear Canvas
canvas = tk.Canvas(
    ventana,
    width=200,
    height=500,
    bg="white"
)
canvas.pack()

# Crear óvalos (luces del semáforo, inician en gris)
rojo = canvas.create_oval(
    50, 30,
    150, 130,
    fill="gray"
)

amarillo = canvas.create_oval(
    50, 180,
    150, 280,
    fill="gray"
)

verde = canvas.create_oval(
    50, 330,
    150, 430,
    fill="gray"
)


# Funciones
def encender_rojo():
    canvas.itemconfig(rojo, fill="red")
    canvas.itemconfig(amarillo, fill="gray")
    canvas.itemconfig(verde, fill="gray")


def encender_amarillo():
    canvas.itemconfig(rojo, fill="gray")
    canvas.itemconfig(amarillo, fill="yellow")
    canvas.itemconfig(verde, fill="gray")


def encender_verde():
    canvas.itemconfig(rojo, fill="gray")
    canvas.itemconfig(amarillo, fill="gray")
    canvas.itemconfig(verde, fill="green")


# Botones
btn_rojo = tk.Button(
    ventana,
    text="Rojo",
    command=encender_rojo
)
btn_rojo.pack()

btn_amarillo = tk.Button(
    ventana,
    text="Amarillo",
    command=encender_amarillo
)
btn_amarillo.pack()

btn_verde = tk.Button(
    ventana,
    text="Verde",
    command=encender_verde
)
btn_verde.pack()

ventana.mainloop()
