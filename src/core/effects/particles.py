"""Particle effects system."""

import pygame
import random
from typing import List, Tuple, Optional
import math

class Particle:
    """Individual particle in an effect."""
    
    def __init__(self, pos: Tuple[float, float], color: Tuple[int, int, int], 
                 speed: float, angle: float, size: int, lifetime: float):
        """Initialize a particle.
        
        Args:
            pos: Starting position (x, y)
            color: RGB color tuple
            speed: Movement speed
            angle: Movement direction in radians
            size: Particle size in pixels
            lifetime: How long the particle lives in seconds
        """
        self.x, self.y = pos
        self.color = color
        self.speed = speed
        self.angle = angle
        self.size = size
        self.lifetime = lifetime
        self.age = 0
        self.dead = False
        
    def update(self, dt: float) -> None:
        """Update particle position and age.
        
        Args:
            dt: Delta time in seconds
        """
        self.x += math.cos(self.angle) * self.speed * dt * 60
        self.y += math.sin(self.angle) * self.speed * dt * 60
        self.age += dt
        self.dead = self.age >= self.lifetime
        
        # Fade out near end of life
        fade = 1 - (self.age / self.lifetime)
        self.color = tuple(int(c * fade) for c in self.color)
        self.size = max(1, int(self.size * fade))

class ParticleSystem:
    """Manages multiple particle effects."""
    
    def __init__(self):
        """Initialize the particle system."""
        self.particles: List[Particle] = []
        
    def create_explosion(self, pos: Tuple[float, float], color: Tuple[int, int, int], 
                        num_particles: int = 20) -> None:
        """Create an explosion effect.
        
        Args:
            pos: Center position of explosion
            color: Base color of particles
            num_particles: Number of particles to create
        """
        for _ in range(num_particles):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(2, 5)
            size = random.randint(2, 4)
            lifetime = random.uniform(0.5, 1.0)
            
            # Add some color variation
            color_var = 20
            varied_color = tuple(
                min(255, max(0, c + random.randint(-color_var, color_var)))
                for c in color
            )
            
            self.particles.append(
                Particle(pos, varied_color, speed, angle, size, lifetime)
            )
            
    def create_impact(self, pos: Tuple[float, float], direction: float,
                     color: Tuple[int, int, int], num_particles: int = 10) -> None:
        """Create an impact effect.
        
        Args:
            pos: Impact position
            direction: Base direction in radians
            color: Base color of particles
            num_particles: Number of particles to create
        """
        spread = math.pi / 4  # 45 degree spread
        for _ in range(num_particles):
            angle = direction + random.uniform(-spread, spread)
            speed = random.uniform(3, 6)
            size = random.randint(1, 3)
            lifetime = random.uniform(0.2, 0.5)
            
            # Add some color variation
            color_var = 20
            varied_color = tuple(
                min(255, max(0, c + random.randint(-color_var, color_var)))
                for c in color
            )
            
            self.particles.append(
                Particle(pos, varied_color, speed, angle, size, lifetime)
            )
    
    def update(self, dt: float) -> None:
        """Update all particles.
        
        Args:
            dt: Delta time in seconds
        """
        # Update all particles and remove dead ones
        self.particles = [p for p in self.particles if not p.dead]
        for particle in self.particles:
            particle.update(dt)
            
    def draw(self, screen: pygame.Surface) -> None:
        """Draw all particles.
        
        Args:
            screen: Surface to draw on
        """
        for particle in self.particles:
            pygame.draw.circle(
                screen,
                particle.color,
                (int(particle.x), int(particle.y)),
                particle.size
            )
