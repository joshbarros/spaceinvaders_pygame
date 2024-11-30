"""CRT screen effect implementation."""

import pygame
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRAPHICS_DIR

class CRTEffect:
    """Applies a CRT screen effect to the game display."""
    
    def __init__(self):
        """Initialize CRT effect."""
        self.tv = pygame.image.load(str(GRAPHICS_DIR / 'tv.png')).convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def create_crt_lines(self) -> pygame.Surface:
        """Create the scanline effect.
        
        Returns:
            Surface with scanline effect
        """
        line_height = 3
        line_amount = int(SCREEN_HEIGHT / line_height)
        
        # Create surface for lines
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        surface.set_colorkey('black')
        surface.set_alpha(50)
        
        # Draw the lines
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(
                surface,
                'white',
                (0, y_pos),
                (SCREEN_WIDTH, y_pos),
                1
            )
            
        return surface
        
    def draw(self, screen: pygame.Surface) -> None:
        """Apply CRT effect to screen.
        
        Args:
            screen: Pygame surface to apply effect to
        """
        # Draw scanlines
        screen.blit(self.create_crt_lines(), (0, 0))
        
        # Draw TV overlay
        screen.blit(self.tv, (0, 0))
