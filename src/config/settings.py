"""Game configuration and settings."""

from pathlib import Path
from typing import Tuple, Dict

# Screen settings
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720
FPS: int = 60
SCREEN_SIZE: Tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Font settings
FONT_SIZE: int = 36
SCORE_FONT_SIZE: int = 24
FONT_NAME: str = None  # Use pygame's default font

# Color settings
WHITE: Tuple[int, int, int] = (255, 255, 255)
BLACK = (0, 0, 0)
RED: Tuple[int, int, int] = (255, 0, 0)
GREEN: Tuple[int, int, int] = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW: Tuple[int, int, int] = (255, 255, 0)
BACKGROUND_COLOR = (30, 30, 30)

# Asset paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = BASE_DIR / "assets"
FONT_DIR = ASSETS_DIR / "font"
AUDIO_DIR = ASSETS_DIR / "audio"
GRAPHICS_DIR = ASSETS_DIR / "graphics"

# Game settings
PLAYER_LIVES: int = 3
PLAYER_SPEED: int = 15
PLAYER_LASER_SPEED: int = -8
PLAYER_LASER_COOLDOWN: int = 600
PLAYER_SIZE: Tuple[int, int] = (60, 48)
PLAYER_LASER_SIZE: Tuple[int, int] = (4, 20)

# Alien settings
ALIEN_ROWS: int = 5
ALIEN_COLS: int = 11
ROW_SPACING: int = 60
COL_SPACING: int = 60
ALIEN_X_DISTANCE: int = 60
ALIEN_Y_DISTANCE: int = 48
ALIEN_SIZE: Tuple[int, int] = (50, 40)
ALIEN_SPEED: float = 0.0
ALIEN_LASER_SPEED: int = 8
ALIEN_LASER_COOLDOWN: Tuple[int, int] = (750, 5000)  # Random interval between shots
ALIEN_LASER_SIZE: Tuple[int, int] = (8, 25)
ALIEN_DESCENT_SPEED: float = 2.8125  # Increased by 1.5x from 1.875
ALIEN_SPAWN_DELAY: int = 2000
ALIEN_MIN_SPAWN_COUNT: int = 1  # Reduced by 50%
ALIEN_MAX_SPAWN_COUNT: int = 2  # Reduced by 50%

# Extra alien settings
EXTRA_SPAWN_TIME_MIN: int = 400
EXTRA_SPAWN_TIME_MAX: int = 800
EXTRA_POINTS: int = 500

# Menu settings
MENU_FONT_SIZE: int = 36
SCORE_FONT_SIZE: int = 24

# Particle settings
PARTICLE_LIFETIME: float = 0.75
PARTICLE_SPEED: int = 150
PARTICLE_COUNT: int = 30
PARTICLE_SIZE: int = 4
PARTICLE_COLORS: dict = {
    'explosion': [(255, 100, 0), (255, 50, 0), (255, 0, 0), (200, 0, 0)],  # Orange to red
    'hit': [(255, 255, 0), (255, 200, 0), (255, 150, 0), (255, 100, 0)]  # Yellow to orange
}

# Star settings
STAR_COUNT: int = 100
STAR_SPEED_MIN: int = 50
STAR_SPEED_MAX: int = 200
STAR_SIZE_MIN: int = 1
STAR_SIZE_MAX: int = 3

# Scoring
SCORE_VALUES: Dict[str, int] = {
    "red": 100,
    "green": 200,
    "yellow": 300,
    "extra": 500
}

# Sound settings
MUSIC_VOLUME: float = 0.2
LASER_VOLUME: float = 0.5
EXPLOSION_VOLUME: float = 0.3

# Obstacle settings
OBSTACLE_AMOUNT: int = 4
OBSTACLE_BLOCK_SIZE: int = 6
OBSTACLE_Y_POSITION: int = SCREEN_HEIGHT - 200

# Player constraints
PLAYER_BOTTOM_MARGIN: int = 50
PLAYER_SIDE_MARGIN: int = 40

class GameOptions:
    """Game options singleton."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
        
    def _initialize(self):
        """Initialize default options."""
        self.crt_effect = False
        self.music_enabled = True
        self.sound_effects_enabled = True
        self.fullscreen = False
        self.difficulty = "Normal"
        
    def toggle_crt(self):
        """Toggle CRT effect."""
        self.crt_effect = not self.crt_effect
        
    def toggle_music(self):
        """Toggle music."""
        self.music_enabled = not self.music_enabled
        
    def toggle_sound_effects(self):
        """Toggle sound effects."""
        self.sound_effects_enabled = not self.sound_effects_enabled
        
    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        self.fullscreen = not self.fullscreen

# Global options instance
GAME_OPTIONS = GameOptions()
