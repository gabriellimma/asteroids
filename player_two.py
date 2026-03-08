import pygame
from player import Player
from constants import (
    SECOND_PLAYER_COLOR,
    LINE_WIDTH
    )

class PlayerTwo(Player):

    def draw(self, screen):
        pygame.draw.polygon(screen, SECOND_PLAYER_COLOR, self.triangle(), LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
