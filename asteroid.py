import pygame
from circleshape import CircleShape
from logger import log_event
import random
from constants import (
    ASTEROID_COLOR,
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS
)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            new_rng_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(new_rng_angle)
            v2 = self.velocity.rotate(-new_rng_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v1 * 1.2

            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = v2 * 1.2
