"""Player entity module."""

import pygame
from typing import Tuple, Optional

from config.settings import (
    GRAPHICS_DIR,
    AUDIO_DIR,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SPEED,
    PLAYER_LASER_SPEED,
    PLAYER_LASER_COOLDOWN,
    PLAYER_SIZE,
    GAME_OPTIONS
)
from core.entities.sprite_entity import SpriteEntity
from core.entities.laser import Laser

class Player(SpriteEntity):
    """Player entity that can move and shoot lasers."""
    
    def __init__(self, position: Optional[Tuple[float, float]] = None):
        """Initialize the player.
        
        Args:
            position: Initial (x, y) position of the player. If None, centers at bottom
        """
        # Set default position at bottom center
        if position is None:
            position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
            
        super().__init__(str(GRAPHICS_DIR / "player.png"), position)
        
        # Scale player sprite to new size
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = self.image.get_rect(center=position)
        
        self.speed = PLAYER_SPEED
        self.lasers = pygame.sprite.Group()
        self.ready_to_shoot = True
        self.laser_time = 0
        self.laser_cooldown = PLAYER_LASER_COOLDOWN
        
    def get_input(self) -> None:
        """Handle player input for movement and shooting."""
        keys = pygame.key.get_pressed()
        
        # Horizontal movement with screen wrapping
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            if self.rect.left >= SCREEN_WIDTH:
                self.rect.right = 0
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.rect.right <= 0:
                self.rect.left = SCREEN_WIDTH
            
        # Shooting
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.ready_to_shoot:
            self.shoot()
            
    def shoot(self) -> None:
        """Create a laser projectile."""
        self.lasers.add(Laser(self.rect.center, PLAYER_LASER_SPEED, True))
        self.ready_to_shoot = False
        self.laser_time = pygame.time.get_ticks()
        if GAME_OPTIONS.sound_effects_enabled:
            pygame.mixer.Sound(str(AUDIO_DIR / "laser.wav")).play()
            
    def recharge(self) -> None:
        """Recharge laser if cooldown has passed."""
        if not self.ready_to_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready_to_shoot = True
                
    def update(self) -> None:
        """Update player state."""
        self.get_input()
        self.recharge()
        self.lasers.update()
        
        # Remove lasers that are off screen
        for laser in self.lasers:
            if laser.rect.bottom < 0:
                laser.kill()
