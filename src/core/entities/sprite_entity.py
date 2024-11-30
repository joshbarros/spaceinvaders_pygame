"""Base sprite entity for all game objects."""

from abc import ABC, abstractmethod
import pygame
from typing import Tuple, Optional

class SpriteEntity(pygame.sprite.Sprite, ABC):
    """Abstract base class for all game entities."""
    
    def __init__(self, image_path: str, position: Tuple[float, float]):
        """Initialize the sprite entity.
        
        Args:
            image_path: Path to the sprite's image file
            position: Initial (x, y) position of the sprite
        """
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        
    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        """Update the sprite's state."""
        pass
    
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the sprite on the given surface.
        
        Args:
            surface: Pygame surface to draw on
        """
        surface.blit(self.image, self.rect)
