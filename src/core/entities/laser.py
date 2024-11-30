"""Laser projectile entity."""

import pygame
from typing import Tuple
from config.settings import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_LASER_SIZE, ALIEN_LASER_SIZE

class Laser(pygame.sprite.Sprite):
    """Laser projectile that can be fired by player or aliens."""
    
    def __init__(self, pos: Tuple[float, float], speed: float, is_player_laser: bool = True):
        """Initialize the laser.
        
        Args:
            pos: Initial (x, y) position
            speed: Movement speed (negative for upward, positive for downward)
            is_player_laser: Whether this is a player's laser (default: True)
        """
        super().__init__()
        
        # Create laser surface with size based on shooter
        size = PLAYER_LASER_SIZE if is_player_laser else ALIEN_LASER_SIZE
        self.image = pygame.Surface(size)
        self.image.fill('cyan' if is_player_laser else 'red')
        self.rect = self.image.get_rect(center=pos)
        
        self.speed = speed
        self.is_player_laser = is_player_laser
        
    def destroy(self):
        """Destroy the laser when it goes off screen."""
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
            
    def update(self):
        """Update laser position."""
        self.rect.y += self.speed
        self.destroy()
