import pygame
import random
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

# Clase para el proyectil inicial del fuego artificial
class Firework:
    def __init__(self):
        self.x = random.randint(100, width - 100)
        self.y = height
        self.color = random.choice(colors)
        self.speed_y = random.uniform(-5, -8)  # Velocidad de ascenso
        self.exploded = False
        self.explosion_height = random.randint(150, 300)  # Altura de la explosión
        self.particles = []

    def move(self):
        if not self.exploded:
            # Ascender hasta la altura de explosión
            self.y += self.speed_y
            pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), 5)
            # Explota al alcanzar la altura deseada
            if self.y <= self.explosion_height:
                self.exploded = True
                self.create_particles()
        else:
            # Mover partículas después de la explosión
            for particle in self.particles:
                particle.move()
            # Eliminar partículas que han terminado su vida
            self.particles[:] = [p for p in self.particles if p.life > 0]

    def create_particles(self):
        # Crear partículas de explosión
        for _ in range(50):  # Número de partículas
            self.particles.append(Particle(self.x, self.y, self.color))

# Clase para las partículas de la explosión
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

# Configuración de sincronización de fuegos artificiales
clock = pygame.time.Clock()
beat_interval = 500  # Intervalo en milisegundos entre explosiones

fireworks = []
running = True
while running:
    window.fill((0, 0, 0))  # Limpiar la pantalla (color negro)
    
    # Detectar eventos de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Crear fuegos artificiales en sincronización con el ritmo
    if pygame.mixer.music.get_pos() % beat_interval < 50:
        fireworks.append(Firework())
    
    # Mover y dibujar cada fuego artificial
    for firework in fireworks:
        firework.move()
    
    # Eliminar fuegos artificiales que ya han explotado y agotado todas sus partículas
    fireworks[:] = [fw for fw in fireworks if fw.exploded is False or fw.particles]

    pygame.display.flip()
    clock.tick(60)

# Cerrar Pygame
pygame.quit()
