import pygame

# Block class extends the Pygame Sprite class and represents a block in an obstacle in the game.
class Block(pygame.sprite.Sprite):
  # Initialize the block with its size, color, and position (x, y).
  def __init__(self, size, color, x, y):
    super().__init__()
    # Create a surface for the block and fill it with the specified color.
    self.image = pygame.Surface((size, size))
    self.image.fill(color)
    # Set the block's position using its image's rect.
    self.rect = self.image.get_rect(topleft = (x, y))

# Define a shape for the obstacle as a list of strings.
shape = [
  '  xxxxxxx',
  ' xxxxxxxxx',
  'xxxxxxxxxxxx',
  'xxxxxxxxxxxx',
  'xxxxxxxxxxxx',
  'xxx      xxx',
  'xx        xx',
]
