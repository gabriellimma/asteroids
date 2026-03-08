import pygame
from constants import *
from logger import log_state
from player import Player
from player_two import PlayerTwo

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
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    p2 = PlayerTwo(SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        updatable.update(dt)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()
