import turtle
import random

# Crear el objeto turtle para representar el "animalito"
t = turtle.Turtle()
t.shape("turtle")  # Cambiar la forma de la turtle a una tortuga
t.speed(1)  # Establecer una velocidad media

# Configuración de la pantalla
turtle.bgcolor("lightblue")

# Función para mover la tortuga aleatoriamente
def move_turtle():
    for _ in range(100):  # Controlar cuántos pasos hará la tortuga
        t.forward(50)  # Mover hacia adelante
        angle = random.randint(0, 360)  # Cambiar la dirección de manera aleatoria
        t.right(angle)

# Ejecutar la animación
move_turtle()

# Terminar el programa al hacer clic
turtle.done()
