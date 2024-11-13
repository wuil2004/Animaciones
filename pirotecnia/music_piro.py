import pygame
import random
import time

# Configuración inicial de Pygame
pygame.init()
pygame.mixer.init()

# Tamaño de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Pirotecnia Musical")

# Cargar música
pygame.mixer.music.load("tu_musica.wav")
pygame.mixer.music.play(-1)  # Repetir la música

# Colores de fuegos artificiales
colors = [
    (255, 0, 0),    # Rojo
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
    (255, 255, 0),  # Amarillo
    (255, 0, 255),  # Rosa
    (0, 255, 255),  # Cian
    (255, 255, 255) # Blanco
]

# Función para crear un destello
def create_firework():
    x = random.randint(0, width)
    y = random.randint(0, height)
    color = random.choice(colors)
    pygame.draw.circle(window, color, (x, y), random.randint(10, 50))

# Configuración de sincronización de destellos
clock = pygame.time.Clock()
beat_interval = 500  # Intervalo en milisegundos entre destellos (ajustar según el ritmo)

running = True
while running:
    window.fill((0, 0, 0))  # Limpiar la pantalla (color negro)
    
    # Detectar eventos de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Crear destello de "pirotecnia" en sincronización
    if pygame.mixer.music.get_pos() % beat_interval < 50:  # Detecta el pulso de ritmo
        create_firework()
    
    pygame.display.flip()
    clock.tick(60)

# Cerrar Pygame
pygame.quit()