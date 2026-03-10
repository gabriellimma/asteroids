import pygame
from player import Player
from shot import Shot
from constants import (
    SECOND_PLAYER_COLOR,
    LINE_WIDTH,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    SHOT_RADIUS,
    PLAYER_SHOOT_SPEED
    )

class PlayerTwo(Player):

    def draw(self, screen):
        pygame.draw.polygon(screen, SECOND_PLAYER_COLOR, self.triangle(), LINE_WIDTH)

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, 2)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt
        mouse_buttons = pygame.mouse.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if mouse_buttons[0]:
            if self.shot_cooldown <= 0:
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
