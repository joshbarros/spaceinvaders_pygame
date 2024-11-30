"""Starfield background effect."""

import pygame
import random
from typing import List, Tuple

from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Star:
    """Individual star in the starfield."""
    
    def __init__(self):
        """Initialize a star with random position and speed."""
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = random.uniform(0.5, 2.0)
        self.brightness = random.randint(100, 255)
        self.size = random.randint(1, 3)
        
    def update(self, dt: float) -> None:
        """Update star position.
        
        Args:
            dt: Delta time in seconds
        """
        self.y += self.speed * dt * 60
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)
            self.brightness = random.randint(100, 255)

class StarField:
    """Dynamic starry background effect."""
    
    def __init__(self, num_stars: int = 100):
        """Initialize the starfield.
        
        Args:
            num_stars: Number of stars to create
        """
        self.stars = [Star() for _ in range(num_stars)]
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def update(self, dt: float) -> None:
        """Update all stars.
        
        Args:
            dt: Delta time in seconds
        """
        for star in self.stars:
            star.update(dt)
            
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the starfield.
        
        Args:
            screen: Surface to draw on
        """
        self.surface.fill((0, 0, 0))
        for star in self.stars:
            color = (star.brightness, star.brightness, star.brightness)
            pygame.draw.circle(self.surface, color, (int(star.x), int(star.y)), star.size)
        screen.blit(self.surface, (0, 0))
