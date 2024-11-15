import turtle

# Crear objeto turtle
t = turtle.Turtle()
t.shape("turtle")  # Cambiar la forma a una tortuga
t.speed(1)  # Ajustar la velocidad para ver mejor el dibujo
t.pensize(5)  # Tamaño de la pluma

# Función para dibujar la letra 'P'
def draw_p():
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-30, 180)
    t.penup()
    t.goto(t.xcor() + 40, t.ycor() - 100)
    t.pendown()

# Función para dibujar la letra 'Y'
def draw_y():
    t.penup()
    t.goto(t.xcor() + 40, t.ycor())
    t.pendown()
    t.forward(50)
    t.right(45)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(t.xcor() + 40, t.ycor() - 100)
    t.pendown()

# Función para dibujar la letra 'T'
def draw_t():
    t.penup()
    t.goto(t.xcor() + 40, t.ycor() + 100)
    t.pendown()
    t.forward(50)
    t.backward(25)
    t.right(90)
    t.forward(100)
    t.penup()
    t.goto(t.xcor() + 25, t.ycor())
    t.pendown()

# Función para dibujar la letra 'H'
def draw_h():
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)
    t.penup()
    t.goto(t.xcor() + 40, t.ycor() - 100)
    t.pendown()

# Función para dibujar la letra 'O'
def draw_o():
    t.penup()
    t.goto(t.xcor() + 40, t.ycor())
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(t.xcor() + 50, t.ycor() - 100)
    t.pendown()

# Función para dibujar la letra 'N'
def draw_n():
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(140)
    t.left(135)
    t.forward(100)
    t.penup()
    t.goto(t.xcor() + 40, t.ycor() - 100)
    t.pendown()

# Función para escribir PYTHON
def write_python():
    draw_p()
    draw_y()
    draw_t()
    draw_h()
    draw_o()
    draw_n()

# Función para dibujar la letra 'U'
def draw_u():
    t.penup()
    t.goto(t.xcor() + 20, t.ycor() + 100)
    t.pendown()
    t.forward(70)
    t.backward(100)
    t.circle(-40, -180)
    t.penup()
    t.goto(t.xcor() + 40, t.ycor() - 100)
    t.pendown()

# Dibujo de la palabra "PYTHON"
t.penup()
t.goto(-300, 100)  # Ajustar la posición de inicio
t.pendown()
write_python()

# Terminar 
turtle.done()
