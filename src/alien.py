import pygame

# Alien class extends the Pygame Sprite class and represents an enemy alien in the game.
class Alien(pygame.sprite.Sprite):
  # Initialize the alien with its color and position (x, y).
  def __init__(self, color, x, y):
    super().__init__()
    # Load the alien's image from the graphics folder.
    file_path = './graphics/' + color + '.png'
    self.image = pygame.image.load(file_path).convert_alpha()
    # Set the alien's position using its image's rect.
    self.rect = self.image.get_rect(topleft = (x, y))

    # Assign a value to the alien based on its color.
    if color == 'red': self.value = 100
    elif color == 'green': self.value = 200
    else: self.value = 300

  # Update the alien's position.
  def update(self, direction):
    self.rect.x += direction

# Extra class extends the Pygame Sprite class and represents an extra alien in the game.
class Extra(pygame.sprite.Sprite):
  # Initialize the extra alien with its side (left or right) and the screen width.
  def __init__(self, side, SCREEN_WIDTH):
    super().__init__()
    # Load the extra's image from the graphics folder.
    self.image = pygame.image.load('./graphics/extra.png').convert_alpha()

    # Set the extra's initial position and speed based on its side.
    if side == 'right':
      x = SCREEN_WIDTH + 50
      self.speed = -3
    else:
      x = -50
      self.speed = 3

    # Set the extra's position using its image's rect.
    self.rect = self.image.get_rect(topleft = (x, 80))

  # Update the extra's position.
  def update(self):
    self.rect.x += self.speed
