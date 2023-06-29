import pygame, sys
from random import choice, randint
from player import Player
from alien import Alien, Extra
from laser import Laser
from settings import *
import obstacle

# Game class manages the overall game logic
class Game:
    def __init__(self):
        # Initialize the player and position it at the center-bottom of the screen
        player_sprite = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT), SCREEN_WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Initialize game lives and related graphics
        self.lives = 3
        self.lives_surf = pygame.image.load('./graphics/player.png').convert_alpha()
        self.live_x_start_pos = SCREEN_WIDTH - (self.lives_surf.get_size()[0] * 2 + 20)

        # Initialize score and font
        self.score = 0
        self.font = pygame.font.Font('./font/Pixeled.ttf')

        # Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (SCREEN_WIDTH / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = SCREEN_WIDTH / 15, y_start = 480)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1

        # Extra alien setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # Audio setup
        music = pygame.mixer.Sound('./audio/music.wav')
        music.set_volume(0.2)
        music.play(loops = -1)

        self.laser_sound = pygame.mixer.Sound('./audio/laser.wav')
        self.laser_sound.set_volume(0.5)
        self.explosion_sound = pygame.mixer.Sound('./audio/explosion.wav')
        self.explosion_sound.set_volume(0.3)

    def create_obstacle(self, x_start, y_start, offset_x):
        # Create an obstacle based on the given shape
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        # Create multiple obstacles
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 100):
        # Set up aliens in a grid layout, differentiated by color
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0: alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: alien_sprite = Alien('green', x, y)
                else: alien_sprite = Alien('red', x, y)

                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        # Check the position of the aliens and reverse direction if they reach the screen's edge
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= SCREEN_WIDTH:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        # Move aliens down by a given distance
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        # Random alien shoots a laser
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, SCREEN_HEIGHT)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        # Timer to spawn extra alien
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right', 'left']), SCREEN_WIDTH))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
      # This method checks for various collision scenarios in the game

      if self.player.sprite.lasers:
        # Checks if a player's laser has collided with anything
        for laser in self.player.sprite.lasers:
          # If a laser collides with a block, destroy both the laser and the block
          if pygame.sprite.spritecollide(laser, self.blocks, True):
            pass
            # laser.kill()

          # If a laser collides with an alien, destroy the alien, increase the score, and play the explosion sound
          aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
          if aliens_hit:
            for alien in aliens_hit:
              self.score += alien.value
            laser.kill()
            self.explosion_sound.play()

          # If a laser collides with an extra, destroy the extra, increase the score
          if pygame.sprite.spritecollide(laser, self.extra, True):
            self.score += 500
            laser.kill()

      if self.alien_lasers:
        # Checks if an alien's laser has collided with anything
        for laser in self.alien_lasers:
          # If a laser collides with a block, destroy both the laser and the block
          if pygame.sprite.spritecollide(laser, self.blocks, True):
            laser.kill()

          # If a laser collides with the player, decrease lives and if lives are 0 or less, quit the game
          if pygame.sprite.spritecollide(laser, self.player, False):
            laser.kill()
            self.lives -=1
            if self.lives <= 0:
              pygame.quit()
              sys.exit()

      if self.aliens:
        # Checks if an alien has collided with anything
        for alien in self.aliens:
          # If an alien collides with a block, destroy the block
          pygame.sprite.spritecollide(alien, self.blocks, True)

          # If an alien collides with the player, quit the game
          if pygame.sprite.spritecollide(alien, self.player, False):
            pygame.quit()
            sys.exit()


    def display_lives(self):
        # Display the remaining lives on the screen
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * self.lives_surf.get_size()[0] + 10)
            self.screen.blit(self.lives_surf, (x, 8))

    def display_score(self):
        # Display the current score on the screen
        score_surf = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (10, -10))
        self.screen.blit(score_surf, score_rect)

    def victory_message(self):
        # Display a victory message if all aliens are destroyed
        if not self.aliens.sprites():
            victory_surf = self.font.render('You won', False, 'white')
            victory_rect = victory_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            self.screen.blit(victory_surf, victory_rect)


    def run(self, screen):
        # Game loop
        self.screen = screen
        self.player.update()  # Update player's state
        self.aliens.update(self.alien_direction)  # Update alien's state
        self.alien_position_checker()  # Check aliens' positions and adjust if necessary
        self.alien_lasers.update()  # Update alien lasers' state
        self.extra_alien_timer()  # Count down to spawn an extra alien
        self.extra.update()  # Update extra alien's state
        self.collision_checks()  # Check for any collisions

        # Draw game objects onto the screen
        self.player.sprite.lasers.draw(self.screen)
        self.blocks.draw(self.screen)
        self.player.draw(self.screen)
        self.aliens.draw(self.screen)
        self.alien_lasers.draw(self.screen)
        self.extra.draw(self.screen)

        # Display lives and score
        self.display_lives()
        self.display_score()

        # Display victory message if all aliens are defeated
        self.victory_message()
