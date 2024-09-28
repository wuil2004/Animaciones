import turtle

# Crear objeto turtle
t = turtle.Turtle()
t.speed(0)  # Velocidad máxima

# Establecer el color de fondo
turtle.bgcolor("black")

# Lista de colores
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Función para dibujar una estrella
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)  # Girar 144 grados para formar una estrella

# Dibujar múltiples estrellas
for x in range(50):
    t.pencolor(colors[x % len(colors)])  # Cambiar el color de la pluma
    draw_star(x * 5)  # Dibujar una estrella de tamaño creciente
    t.penup()  # Levantar la pluma para mover sin dibujar
    t.goto(x * 2, x * 2)  # Mover la tortuga a una nueva posición
    t.pendown()  # Bajar la pluma para empezar a dibujar de nuevo
    t.right(36)  # Girar ligeramente para dar
