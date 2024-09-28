import turtle

# Crear objeto turtle
t = turtle.Turtle()
t.speed(0)  # Establecer velocidad máxima

# Establecer el color de fondo
turtle.bgcolor("black")

# Lista de colores
colors = ["red", "blue", "green", "orange", "purple", "white"]

# Dibujar un patrón de espiral
for x in range(500):
    t.pensize(x / 100 + 1)  # Cambiar el grosor de la pluma
    t.pencolor(colors[x % len(colors)])  # Cambiar color de la pluma
    t.forward(x)  # Mover la tortuga hacia adelante
    t.left(59)    # Girar la tortuga 59 grados hacia la izquierda

# Terminar el programa al hacer clic
turtle.done()
