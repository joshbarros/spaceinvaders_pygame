import pygame, sys
from game import Game
from crt import CRT
from settings import *

if __name__ == '__main__':
    # Initialize all imported pygame modules
    pygame.init()
    # Set up the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set the title of the window
    pygame.display.set_caption('Space Invaders')
    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game()
    # Create a CRT object for the CRT effect
    crt = CRT()

    # Define an event for alien laser
    ALIENLASER = pygame.USEREVENT + 1
    # Set a timer for alien laser event every 800 milliseconds
    pygame.time.set_timer(ALIENLASER, 800)

    # Main game loop
    while True:
        # Event loop
        for event in pygame.event.get():
            # If the event is QUIT (like closing the window), stop the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the event is the alien laser event, let the aliens shoot
            if event.type == ALIENLASER:
              game.alien_shoot()

        # Fill the screen with a color
        screen.fill((30, 30, 30))
        # Run the game logic
        game.run(screen)
        # Draw the CRT effect
        crt.draw(screen)
        # Update the full display surface to the screen
        pygame.display.flip()
        # Limit the game to 60 frames per second
        clock.tick(60)
