import sys
import pygame
from logger import log_state, log_event
from constants import *

from player import Player
from player_two import PlayerTwo
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

VERSION = pygame.version.ver


def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawables)
    Asteroid.containers = (updatable, drawables, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawables, updatable)

    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()
    #p2 = PlayerTwo(SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.colides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()

            if asteroid.colides_with(p1):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()
