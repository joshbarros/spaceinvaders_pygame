import pygame
from random import randint
from settings import *

# Class to create CRT effect
class CRT:
    def __init__(self):
        # Load the TV graphics and scale it to the screen size
        self.tv = pygame.image.load('./graphics/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def create_crt_lines(self):
        # Set line height for CRT lines
        line_height = 3
        # Calculate the amount of lines needed based on the screen height
        line_amount = int(SCREEN_HEIGHT / line_height)
        # Draw each line on the TV surface
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (SCREEN_WIDTH, y_pos), 1)

    def draw(self, screen):
        self.screen = screen
        # Set the alpha for the TV surface for transparency
        self.tv.set_alpha(randint(75, 90))
        # Create the CRT lines on the TV surface
        self.create_crt_lines()
        # Blit (draw) the TV surface onto the screen
        self.screen.blit(self.tv, (0, 0))
