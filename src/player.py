import pygame
from laser import Laser

# Player class extends the Pygame Sprite class and represents the player in the game.
class Player(pygame.sprite.Sprite):
  # Initialize the player with its position (pos), max x constraint, and speed.
  def __init__(self, pos, constraint, speed):
    super().__init__()
    # Load the player's image from the graphics folder.
    self.image = pygame.image.load('./graphics/player.png').convert_alpha()
    # Set the player's position using its image's rect.
    self.rect = self.image.get_rect(midbottom = pos)
    # Set the player's speed and max x constraint.
    self.speed = speed
    self.max_x_constraint = constraint
    # Set the player's laser shooting status, time, and cooldown.
    self.ready = True
    self.laser_time = 0
    self.laser_cooldown = 600

    # Create a group for the player's lasers.
    self.lasers = pygame.sprite.Group()

    # Load the laser sound from the audio folder and set its volume.
    self.laser_sound = pygame.mixer.Sound('./audio/laser.wav')
    self.laser_sound.set_volume(0.5)

  # Check for player input.
  def get_input(self):
    keys = pygame.key.get_pressed()

    # Move the player to the right or left if the corresponding key is pressed.
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
    elif keys[pygame.K_LEFT]:
      self.rect.x -= self.speed

    # Shoot a laser if the space key is pressed and the player is ready.
    if keys[pygame.K_SPACE] and self.ready:
      self.shoot_laser()
      self.ready = False
      self.laser_time = pygame.time.get_ticks()
      self.laser_sound.play()

  # Recharge the player's laser shooting ability after the cooldown period.
  def recharge(self):
    if not self.ready:
      current_time = pygame.time.get_ticks()
      if current_time - self.laser_time >= self.laser_cooldown:
        self.ready = True

  # Constrain the player's movement within the screen's boundaries.
  def constraint(self):
    if self.rect.left <= 0:
      self.rect.left = 0
    if self.rect.right >= self.max_x_constraint:
      self.rect.right = self.max_x_constraint

  # Shoot a laser from the player's position.
  def shoot_laser(self):
    self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))

  # Update the player's status and its lasers.
  def update(self):
    self.get_input()
    self.constraint()
    self.recharge()
    self.lasers.update()
