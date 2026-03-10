import pygame

class Score:
    def __init__(self, score = 0):
        self.score = score
        self.player_one_score = 0
        self.player_two_score = 0
        self.font = pygame.font.Font(None, 36)

    def get_score(self) -> int:
        return self.score

    def setScore(self, score: int) -> int:
        self.score = score

    def increase_score(self, player:int, by: int):
        """
        add points to the player (1 or 2) 
        and to the score
        """
        if player == 1:
            self.player_one_score += by
            self.score += by
        if player == 2:
            self.player_two_score += by
            self.score += by

    def draw(self, screen):
        """draws the score on screen"""
        p1_text = self.font.render(f"P1: {self.player_one_score}", True, "white")
        screen.blit(p1_text, (10,10))

        p2_text = self.font.render(f"P2: {self.player_two_score}", True, "white")
        screen.blit(p2_text, (700,10))

    def reset_score(self):
        """resets the score"""
        self.player_one_score = 0
        self.player_two_score = 0
