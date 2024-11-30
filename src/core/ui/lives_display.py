"""Lives display UI component."""

import pygame
from config.settings import FONT_DIR, SCREEN_WIDTH, SCORE_FONT_SIZE

class LivesDisplay:
    """Display for the player's remaining lives."""
    
    def __init__(self):
        """Initialize the lives display."""
        self.font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), SCORE_FONT_SIZE)
        
    def draw(self, screen: pygame.Surface, lives: int) -> None:
        """Draw the lives count on screen.
        
        Args:
            screen: Surface to draw on
            lives: Number of lives to display
        """
        lives_surf = self.font.render(f'Lives: {lives}', False, 'white')
        lives_rect = lives_surf.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        screen.blit(lives_surf, lives_rect)
