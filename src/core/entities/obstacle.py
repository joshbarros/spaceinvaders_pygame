"""Obstacle protection entities."""

from typing import Tuple
import pygame

from config.settings import OBSTACLE_BLOCK_SIZE

class Block(pygame.sprite.Sprite):
    """Individual block that makes up an obstacle."""
    
    def __init__(self, position: Tuple[float, float], color: Tuple[int, int, int] = (241, 79, 80)):
        """Initialize block.
        
        Args:
            position: Position of the block
            color: RGB color tuple for the block
        """
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_BLOCK_SIZE, OBSTACLE_BLOCK_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=position)

class Obstacle:
    """Factory class for creating obstacle formations."""
    
    shape = [
        '  xxxxxxx  ',
        ' xxxxxxxxx ',
        'xxxxxxxxxxx',
        'xxxxxxxxxxx',
        'xxxxxxxxxxx',
        'xxx     xxx',
        'xx       xx'
    ]
    
    @classmethod
    def create(cls, position: Tuple[float, float]) -> pygame.sprite.Group:
        """Create an obstacle formation.
        
        Args:
            position: Base position for the obstacle
            
        Returns:
            Group of block sprites forming the obstacle
        """
        blocks = pygame.sprite.Group()
        for row_index, row in enumerate(cls.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = position[0] + col_index * OBSTACLE_BLOCK_SIZE
                    y = position[1] + row_index * OBSTACLE_BLOCK_SIZE
                    block = Block((x, y))
                    blocks.add(block)
        return blocks
