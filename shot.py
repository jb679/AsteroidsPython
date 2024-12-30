import pygame
from constants import SHOT_RADIUS

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(self.containers)  # Add to specified groups
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
