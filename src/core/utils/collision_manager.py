"""Collision detection and handling."""

import pygame
from typing import Tuple

from core.utils.sound_manager import SoundManager

class CollisionManager:
    """Manages all collision detection and resolution in the game."""
    
    def __init__(self):
        """Initialize collision manager."""
        self.sound_manager = SoundManager()
    
    def check_player_laser_collisions(
        self,
        player_lasers: pygame.sprite.Group,
        aliens: pygame.sprite.Group,
        blocks: pygame.sprite.Group,
        extra: pygame.sprite.GroupSingle
    ) -> int:
        """Check collisions between player lasers and other entities.
        
        Args:
            player_lasers: Group of player laser sprites
            aliens: Group of alien sprites
            blocks: Group of obstacle block sprites
            extra: Group containing bonus UFO
            
        Returns:
            Score from destroyed aliens
        """
        score = 0
        
        if player_lasers:
            for laser in player_lasers:
                # Check collision with blocks
                if pygame.sprite.spritecollide(laser, blocks, True):
                    laser.kill()
                
                # Check collision with aliens
                aliens_hit = pygame.sprite.spritecollide(laser, aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        score += alien.value
                    laser.kill()
                    self.sound_manager.play_explosion()
                
                # Check collision with extra
                if pygame.sprite.spritecollide(laser, extra, True):
                    score += 500
                    laser.kill()
                    
        return score
    
    def check_alien_laser_collisions(
        self,
        alien_lasers: pygame.sprite.Group,
        player: pygame.sprite.GroupSingle,
        blocks: pygame.sprite.Group
    ) -> bool:
        """Check collisions between alien lasers and other entities.
        
        Args:
            alien_lasers: Group of alien laser sprites
            player: Group containing player sprite
            blocks: Group of obstacle block sprites
            
        Returns:
            True if player was hit, False otherwise
        """
        if alien_lasers:
            for laser in alien_lasers:
                # Check collision with blocks
                if pygame.sprite.spritecollide(laser, blocks, True):
                    laser.kill()
                
                # Check collision with player
                if pygame.sprite.spritecollide(laser, player, False):
                    laser.kill()
                    return True
        return False
    
    def check_aliens_reached_bottom(
        self,
        aliens: pygame.sprite.Group,
        player: pygame.sprite.GroupSingle,
        blocks: pygame.sprite.Group
    ) -> bool:
        """Check if aliens have reached the bottom or collided with player/blocks.
        
        Args:
            aliens: Group of alien sprites
            player: Group containing player sprite
            blocks: Group of obstacle block sprites
            
        Returns:
            True if game should end, False otherwise
        """
        if aliens:
            for alien in aliens:
                # Check collision with blocks
                pygame.sprite.spritecollide(alien, blocks, True)
                
                # Check collision with player
                if pygame.sprite.spritecollide(alien, player, False):
                    return True
                    
        return False
