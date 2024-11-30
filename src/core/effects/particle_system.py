"""Particle system for visual effects."""

import pygame
import random
from typing import List, Tuple
from math import sin, cos, pi

from config.settings import (
    PARTICLE_LIFETIME,
    PARTICLE_SIZE,
    PARTICLE_COLORS
)

class Particle:
    """Individual particle with position, velocity, and lifetime."""
    
    def __init__(self, pos: Tuple[float, float], velocity: Tuple[float, float], color: Tuple[int, int, int]):
        """Initialize particle.
        
        Args:
            pos: Initial (x, y) position
            velocity: (vx, vy) velocity
            color: RGB color tuple
        """
        self.x, self.y = float(pos[0]), float(pos[1])
        self.vx, self.vy = velocity
        # Ensure color is a valid RGB tuple
        if not isinstance(color, (tuple, list)) or len(color) != 3:
            self.color = (255, 0, 0)  # Default to red if invalid
        else:
            # Ensure all color components are valid integers between 0 and 255
            self.color = tuple(max(0, min(255, int(c))) for c in color)
        self.lifetime = PARTICLE_LIFETIME
        
    def update(self, dt: float) -> None:
        """Update particle position and lifetime.
        
        Args:
            dt: Time delta in seconds
        """
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.lifetime -= dt
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw particle on screen.
        
        Args:
            screen: Surface to draw on
        """
        try:
            alpha = int(max(0, min(255, 255 * (self.lifetime / PARTICLE_LIFETIME))))
            # Create a surface for the particle with alpha channel
            particle_surface = pygame.Surface((PARTICLE_SIZE * 2 + 1, PARTICLE_SIZE * 2 + 1), pygame.SRCALPHA)
            # Create RGBA color tuple
            color_with_alpha = (
                self.color[0],
                self.color[1],
                self.color[2],
                alpha
            )
            # Draw the particle
            pygame.draw.circle(
                particle_surface,
                color_with_alpha,
                (PARTICLE_SIZE + 1, PARTICLE_SIZE + 1),
                PARTICLE_SIZE
            )
            # Blit the particle surface onto the screen
            screen.blit(
                particle_surface,
                (int(self.x - PARTICLE_SIZE), int(self.y - PARTICLE_SIZE))
            )
        except (ValueError, IndexError, TypeError):
            # If any error occurs, skip drawing this particle
            pass

class ParticleSystem:
    """System to manage multiple particles."""
    
    def __init__(self):
        """Initialize particle system."""
        self.particles: List[Particle] = []
        
    def create_explosion(self, pos: Tuple[float, float], effect_type: str, count: int, speed: float) -> None:
        """Create an explosion effect.
        
        Args:
            pos: Center position of explosion
            effect_type: Type of effect ('explosion' or 'hit')
            count: Number of particles to create
            speed: Base speed of particles
        """
        try:
            colors = PARTICLE_COLORS.get(effect_type, [(255, 0, 0)])  # Default to red if effect type not found
            for _ in range(count):
                angle = random.uniform(0, 2 * pi)
                velocity = (
                    speed * cos(angle) * random.uniform(0.2, 1.0),
                    speed * sin(angle) * random.uniform(0.2, 1.0)
                )
                color = random.choice(colors)
                self.particles.append(Particle(pos, velocity, color))
        except (KeyError, AttributeError):
            # If any error occurs with colors, create a simple red explosion
            for _ in range(count):
                angle = random.uniform(0, 2 * pi)
                velocity = (
                    speed * cos(angle) * random.uniform(0.2, 1.0),
                    speed * sin(angle) * random.uniform(0.2, 1.0)
                )
                self.particles.append(Particle(pos, velocity, (255, 0, 0)))
            
    def update(self, dt: float) -> None:
        """Update all particles.
        
        Args:
            dt: Time delta in seconds
        """
        # Update and remove dead particles
        self.particles = [p for p in self.particles if p.lifetime > 0]
        for particle in self.particles:
            particle.update(dt)
            
    def draw(self, screen: pygame.Surface) -> None:
        """Draw all particles.
        
        Args:
            screen: Surface to draw on
        """
        for particle in self.particles:
            particle.draw(screen)
