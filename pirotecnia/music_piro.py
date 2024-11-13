import pygame
import random
import time
import math

# Configuración inicial de Pygame
pygame.init()
pygame.mixer.init()

# Tamaño de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Pirotecnia Musical")

# Cargar música
pygame.mixer.music.load("pirotecnia/audio.mp3")
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

# Clase para crear partículas de fuegos artificiales
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 5)
        self.speed = random.uniform(1, 4)
        self.angle = random.uniform(0, 2 * math.pi)
        self.life = 100  # Duración de la partícula

    def move(self):
        # Movimiento de la partícula
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + 0.1  # Gravedad ligera
        self.life -= 1
        if self.life > 0:
            pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)

# Función para crear una explosión de partículas
def create_firework():
    x = random.randint(100, width - 100)
    y = random.randint(100, height - 300)
    color = random.choice(colors)
    particles = [Particle(x, y, color) for _ in range(50)]
    return particles

# Configuración de sincronización de explosiones
clock = pygame.time.Clock()
beat_interval = 500  # Intervalo en milisegundos entre explosiones

running = True
fireworks = []
while running:
    window.fill((0, 0, 0))  # Limpiar la pantalla (color negro)
    
    # Detectar eventos de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Crear una explosión en sincronización con el ritmo
    if pygame.mixer.music.get_pos() % beat_interval < 50:
        fireworks.append(create_firework())
    
    # Dibujar y actualizar partículas de cada explosión
    for firework in fireworks:
        for particle in firework:
            particle.move()
        # Eliminar las partículas que han terminado su vida
        firework[:] = [p for p in firework if p.life > 0]

    pygame.display.flip()
    clock.tick(60)

# Cerrar Pygame
pygame.quit()
