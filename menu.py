import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def landing_page():
    """Tela inicial para selecionar modo de jogo"""
    screen = pygame.display.get_surface()
    font_title = pygame.font.Font(None, 72)
    font_subtitle = pygame.font.Font(None, 36)

    running = True
    selected = 1  # 1 ou 2 jogadores (padrão 1)

    while running:
        screen.fill("black")

        # Título
        title = font_title.render("ASTEROIDS", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        # Opções
        p1_text = font_subtitle.render("1 Player", True,
                                       (255, 255, 0) if selected == 1 else (255, 255, 255))
        p2_text = font_subtitle.render("2 Players", True,
                                       (255, 255, 0) if selected == 2 else (255, 255, 255))
        quit_text = font_subtitle.render("Quit", True,
                                       (255, 255, 0) if selected == 3 else (255, 255, 255))

        screen.blit(p1_text, (SCREEN_WIDTH // 2 - p1_text.get_width() // 2, 300))
        screen.blit(p2_text, (SCREEN_WIDTH // 2 - p2_text.get_width() // 2, 400))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 500))

        # Instruções
        info = font_subtitle.render("Use arrow keys and ENTER to select", True, (200, 200, 200))
        screen.blit(info, (SCREEN_WIDTH // 2 - info.get_width() // 2, 550))

        pygame.display.flip()

        # Processar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = selected - 1 if selected > 1 else 3
                elif event.key == pygame.K_DOWN:
                    selected = selected + 1 if selected < 3 else 1
                elif event.key == pygame.K_RETURN:
                    if selected == 3:  # Quit
                        pygame.quit()
                        exit()
                    else:
                        return selected
