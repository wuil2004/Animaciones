import turtle
import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Animación de Turtle con botón Start/Stop")

# Configurar el canvas de tkinter para turtle
canvas = turtle.ScrolledCanvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Configurar el entorno de turtle
t_screen = turtle.TurtleScreen(canvas)
t_screen.bgcolor("black")

# Crear el objeto turtle
t = turtle.RawTurtle(t_screen)
t.speed(0)
t.pensize(2)

# Variables de control
running = False

# Lista de colores
colors = ["cyan", "magenta", "yellow", "white", "red", "green", "blue"]

# Función de animación
def animate():
    global running
    if running:
        t.pencolor(colors[t.xcor() % len(colors)])  # Cambiar color del círculo
        t.circle(100)  # Dibujar círculo de radio 100
        t.left(10)  # Girar un poco para el próximo círculo
        t_screen.ontimer(animate, 100)  # Volver a ejecutar la animación en 100 ms

# Función para iniciar/detener la animación
def toggle_animation():
    global running
    if running:
        running = False
    else:
        running = True
        animate()  # Iniciar la animación si no está corriendo

# Crear botón para iniciar/detener
start_stop_button = tk.Button(root, text="Start/Stop", command=toggle_animation)
start_stop_button.pack(pady=20)

# Iniciar el bucle principal de tkinter
root.mainloop()
