import pygame

# Laser class extends the Pygame Sprite class and represents a laser in the game.
class Laser(pygame.sprite.Sprite):
  # Initialize the laser with its position (pos), speed, and the screen height.
  def __init__(self, pos, speed, SCREEN_HEÎGHT):
    super().__init__()
    # Create a surface for the laser and fill it with white color.
    self.image = pygame.Surface((4, 20))
    self.image.fill('white')
    # Set the laser's position using its image's rect.
    self.rect = self.image.get_rect(center = pos)
    # Set the laser's speed and the y constraint based on the screen height.
    self.speed = speed
    self.height_y_constraint = SCREEN_HEÎGHT

  # Destroy the laser if it's outside of the screen's boundaries.
  def destroy(self):
    if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
      self.kill()

  # Update the laser's position and check if it needs to be destroyed.
  def update(self):
    self.rect.y += self.speed
    self.destroy()
