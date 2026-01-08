import pygame
import circleshape
import constants
from logger import log_event
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2 * 1.2