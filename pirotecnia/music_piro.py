import pygame
import random
import math

# Configuración inicial de Pygame
pygame.init()
pygame.mixer.init()

# Tamaño de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Pirotecnia Musical - Figuras")

# Cargar música
pygame.mixer.music.load("audio.mp3")
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

# Tipos de figuras disponibles
shapes = ["circle", "flower", "star", "heart", "panda"]
current_shape = 0  # Índice para el tipo de figura actual

# Clase para el proyectil inicial del fuego artificial
class Firework:
    def __init__(self, shape):
        self.x = random.randint(100, width - 100)
        self.y = height
        self.color = random.choice(colors)
        self.speed_y = random.uniform(-7, -10)  # Velocidad de ascenso
        self.exploded = False
        self.explosion_height = random.randint(150, 300)  # Altura de la explosión
        self.particles = []
        self.shape = shape  # Figura seleccionada

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
        # Crear partículas dependiendo de la figura
        if self.shape == "circle":
            self.create_circle_particles()
        elif self.shape == "flower":
            self.create_flower_particles()
        elif self.shape == "star":
            self.create_star_particles()
        elif self.shape == "heart":
            self.create_heart_particles()
        elif self.shape == "panda":
            self.create_panda_particles()

    def create_circle_particles(self):
        for angle in range(0, 360, 10):  # Generar partículas en un círculo
            radian = math.radians(angle)
            self.particles.append(Particle(self.x, self.y, self.color, radian, speed=3))

    def create_flower_particles(self):
        for angle in range(0, 360, 15):  # Generar pétalos
            radian = math.radians(angle)
            for offset in (1, 2):  # Múltiples capas
                self.particles.append(Particle(self.x, self.y, self.color, radian, speed=offset * 2))

    def create_star_particles(self):
        for angle in range(0, 360, 36):  # Picos de la estrella
            radian = math.radians(angle)
            self.particles.append(Particle(self.x, self.y, self.color, radian, speed=5))
            self.particles.append(Particle(self.x, self.y, self.color, radian + math.radians(18), speed=3))

    def create_heart_particles(self):
        for t in range(0, 360, 5):  # Usar coordenadas polares para el corazón
            radian = math.radians(t)
            x_offset = 16 * math.sin(radian)**3
            y_offset = -(13 * math.cos(radian) - 5 * math.cos(2 * radian) - 2 * math.cos(3 * radian) - math.cos(4 * radian))
            self.particles.append(Particle(self.x + x_offset * 10, self.y + y_offset * 10, self.color, 0, speed=0))

    def create_panda_particles(self):
        # Cara principal
        self.particles.append(Particle(self.x, self.y, (255, 255, 255), 0, speed=0, radius=20))
        # Ojos
        self.particles.append(Particle(self.x - 10, self.y - 10, (0, 0, 0), 0, speed=0, radius=6))
        self.particles.append(Particle(self.x + 10, self.y - 10, (0, 0, 0), 0, speed=0, radius=6))
        # Orejas
        self.particles.append(Particle(self.x - 20, self.y - 20, (0, 0, 0), 0, speed=0, radius=10))
        self.particles.append(Particle(self.x + 20, self.y - 20, (0, 0, 0), 0, speed=0, radius=10))

# Clase para las partículas de la explosión
class Particle:
    def __init__(self, x, y, color, angle, speed, radius=None):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius if radius else random.randint(2, 4)
        self.speed = speed
        self.angle = angle
        self.life = 100  # Duración de la partícula
        self.fade = 255  # Valor inicial para el desvanecimiento

    def move(self):
        # Movimiento de la partícula
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + 0.1  # Gravedad ligera
        self.life -= 1
        self.fade = max(0, self.fade - 3)  # Reducir el valor de desvanecimiento
        if self.life > 0:
            faded_color = (
                max(0, self.color[0] * self.fade // 255),
                max(0, self.color[1] * self.fade // 255),
                max(0, self.color[2] * self.fade // 255),
            )
            pygame.draw.circle(window, faded_color, (int(self.x), int(self.y)), self.radius)

# Configuración de sincronización de fuegos artificiales
clock = pygame.time.Clock()
fireworks = []
auto_firework_timer = 0
running = True

while running:
    window.fill((0, 0, 0))  # Limpiar la pantalla (color negro)
    
    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Cambiar figura con flechas izquierda y derecha
            if event.key == pygame.K_LEFT:
                current_shape = (current_shape - 1) % len(shapes)
            elif event.key == pygame.K_RIGHT:
                current_shape = (current_shape + 1) % len(shapes)
            # Lanzar fuego artificial con barra espaciadora
            elif event.key == pygame.K_SPACE:
                fireworks.append(Firework(shapes[current_shape]))

    # Lanzar fuegos artificiales automáticamente cada 1 segundo
    auto_firework_timer += clock.get_time()
    if auto_firework_timer > 1000:
        auto_firework_timer = 0
        fireworks.append(Firework(random.choice(shapes)))
    
    # Dibujar texto de figura seleccionada
    font = pygame.font.Font(None, 36)
    text = font.render(f"Figura: {shapes[current_shape].capitalize()}", True, (255, 255, 255))
    window.blit(text, (10, 10))
    
    # Mover y dibujar cada fuego artificial
    for firework in fireworks:
        firework.move()
    
    # Eliminar fuegos artificiales que ya han explotado y agotado todas sus partículas
    fireworks[:] = [fw for fw in fireworks if fw.exploded is False or fw.particles]

    pygame.display.flip()
    clock.tick(60)

# Cerrar Pygame
pygame.quit()
