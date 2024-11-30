"""Score display UI component."""

import pygame
from config.settings import FONT_DIR, SCREEN_WIDTH, SCORE_FONT_SIZE

class ScoreDisplay:
    """Display for the player's score."""
    
    def __init__(self):
        """Initialize the score display."""
        self.font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), SCORE_FONT_SIZE)
        
    def draw(self, screen: pygame.Surface, score: int) -> None:
        """Draw the score on screen.
        
        Args:
            screen: Surface to draw on
            score: Current score to display
        """
        score_surf = self.font.render(f'Score: {score}', False, 'white')
        score_rect = score_surf.get_rect(topleft=(20, 20))
        screen.blit(score_surf, score_rect)
