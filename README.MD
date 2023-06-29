# Space Invaders

This project is a recreation of the classic arcade game, Space Invaders, implemented in Python using the Pygame library. The gameplay involves controlling a spaceship to destroy invading alien ships.

# Special Thanks
This project was inspired by the Space Invaders arcade game developed by Tomohiro Nishikado.

# Project Structure
The project has the following file and folder structure:

## src
This folder contains the source code files for the game:

* ###### main.py: The main entry point of the game. It manages the game loop and event handling.
* ###### game.py: This file contains the Game class, handling the overall game logic including collision checks, scoring and sound effects. It integrates other classes to provide complete gameplay.
* ###### alien.py: This file contains the Alien class representing the alien invaders. Each alien object handles its own movement and rendering.
* ###### crt.py: This file provides a retro CRT screen effect for the game.
* ###### laser.py: Contains the Laser class representing lasers shot by both the player and aliens. This includes the logic for movement and rendering of lasers.
* ###### obstacle.py: This file contains the Obstacle class representing barriers that can block lasers. Each obstacle has its own hit points and is removed after taking a certain amount of damage.
* ###### player.py: This file contains the Player class representing the player-controlled spaceship. This includes logic for movement, firing lasers, and rendering the spaceship.
* ###### settings.py: This file defines the game's settings and constants such as screen resolution, alien speed, laser speed, etc.

## audio
This folder contains audio files used in the game for background music and sound effects:

* ###### explosion.wav: The sound effect that is played when an alien is destroyed.
* ###### laser.wav: The sound effect for laser shots fired by the player's spaceship.
* ###### music.wav: The background music that plays during the game.

## font
This folder contains font files used for displaying text in the game:

* ###### Pixeled.ttf: The font used for displaying score and other textual information on the screen.

## graphics
This folder contains image files used for the game's visuals:

* ###### extra.png: The image for the extra bonus items that appear occasionally in the game.
* ###### green.png, red.png, yellow.png: Images for different types of alien invaders.
* ###### player.png: The image for the player's spaceship.
* ###### tv.png: The image used for the CRT screen effect.

# Instructions
To run the project, follow these steps:

1. Install Python 3 if you haven't already.
2. Install the Pygame library by running the command: `pip install pygame`.
3. Navigate to the project's src directory.
4. Run the command: `python3 src/main.py`.

Ensure that the required resources (images, sounds, etc.) are in the appropriate directories as indicated in the folder structure.

Feel free to modify and explore the game to suit your needs.

Enjoy playing!
