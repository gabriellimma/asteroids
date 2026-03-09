import pygame
from circleshape import CircleShape
from constants import SHOT_COLOR, SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, SHOT_RADIUS, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt