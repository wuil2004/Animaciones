import turtle
import random

# Crear el objeto tortuga
t = turtle.Turtle()
t.speed(0)  # Establecer la velocidad máxima para la animación
turtle.bgcolor("black")  # Fondo negro para resaltar los colores

# Lista de colores brillantes
colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan"]

# Función para dibujar una espiral con colores cambiantes
def draw_spiral():
    for i in range(360):  # Bucle para crear el patrón de espiral
        t.pencolor(random.choice(colors))  # Cambiar el color de la pluma aleatoriamente
        t.width(i / 100 + 1)  # Aumentar el grosor del trazo a medida que la espiral crece
        t.forward(i)  # Mover la tortuga hacia adelante
        t.left(59)  # Girar para formar la espiral

# Función para dibujar estrellas aleatorias
def draw_stars():
    t.penup()
    t.goto(-300, -300)
    t.pendown()
    t.hideturtle()
    for _ in range(20):  # Dibujar 20 estrellas en posiciones aleatorias
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(5):  # Dibujar cada estrella
            t.forward(50)
            t.right(144)
        t.pencolor(random.choice(colors))  # Cambiar el color de cada estrella

# Ejecutar la animación
draw_stars()  # Dibujar las estrellas de fondo
draw_spiral()  # Iniciar la espiral animada

# Terminar el dibujo
turtle.done()
