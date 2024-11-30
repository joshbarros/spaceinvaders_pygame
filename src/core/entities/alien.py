"""Alien entities module."""

import pygame
from random import choice, randint
from typing import Tuple, Optional

from config.settings import (
    GRAPHICS_DIR,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ALIEN_SPEED,
    ALIEN_LASER_SPEED,
    ALIEN_LASER_COOLDOWN,
    ALIEN_DESCENT_SPEED,
    ALIEN_SIZE,
    SCORE_VALUES
)
from core.entities.sprite_entity import SpriteEntity
from core.entities.laser import Laser

class Alien(SpriteEntity):
    """Basic alien enemy that moves and shoots."""
    
    def __init__(self, x: int, y: int, color: str):
        """Initialize the alien.
        
        Args:
            x: X position
            y: Y position
            color: Color variant ('red', 'green', or 'yellow')
        """
        super().__init__(str(GRAPHICS_DIR / f"{color}.png"), (x, y))
        
        # Scale alien sprite to new size
        self.image = pygame.transform.scale(self.image, ALIEN_SIZE)
        self.rect = self.image.get_rect(center=(x, y))
        
        self.value = SCORE_VALUES[color]
        self.last_shot = pygame.time.get_ticks()
        self.original_y = float(y)
        self.y_offset = 0.0
        
        # Random shooting cooldown
        self.current_cooldown = randint(*ALIEN_LASER_COOLDOWN)
        
    def shoot(self) -> Optional[Laser]:
        """Create a laser if cooldown has passed.
        
        Returns:
            Laser object if shot, None otherwise
        """
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.current_cooldown:
            self.last_shot = now
            # Set new random cooldown for next shot
            self.current_cooldown = randint(*ALIEN_LASER_COOLDOWN)
            return Laser(self.rect.center, ALIEN_LASER_SPEED, False)
        return None
        
    def update(self) -> None:
        """Update alien position."""
        # Only vertical movement (constant descent)
        self.y_offset += ALIEN_DESCENT_SPEED
        self.rect.y = int(self.original_y + self.y_offset)
        
        # Remove if off screen
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()

class Extra(SpriteEntity):
    """Bonus UFO that moves across the screen."""
    
    def __init__(self, side: str):
        """Initialize the UFO.
        
        Args:
            side: Starting side ('left' or 'right')
        """
        super().__init__(str(GRAPHICS_DIR / "extra.png"), (0, 80))
        self.value = SCORE_VALUES["extra"]
        
        if side == 'right':
            self.speed = -3
            self.rect.x = SCREEN_WIDTH + 50
        else:
            self.speed = 3
            self.rect.x = -50
            
    def update(self) -> None:
        """Update UFO position and destroy if off screen."""
        self.rect.x += self.speed
        if self.rect.x < -100 or self.rect.x > SCREEN_WIDTH + 100:
            self.kill()
