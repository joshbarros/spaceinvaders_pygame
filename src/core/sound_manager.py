"""Sound manager for handling game audio."""

import pygame
from pathlib import Path
from typing import Dict

from config.settings import AUDIO_DIR, GAME_OPTIONS

class SoundManager:
    """Manages all game sounds and music."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize the sound manager."""
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.music_loaded = False
        
        # Load sound effects
        self.sounds["laser"] = pygame.mixer.Sound(str(AUDIO_DIR / "laser.wav"))
        self.sounds["explosion"] = pygame.mixer.Sound(str(AUDIO_DIR / "explosion.wav"))
        self.sounds["alien_laser"] = pygame.mixer.Sound(str(AUDIO_DIR / "alien_laser.wav"))
        
        # Set default volumes
        for sound in self.sounds.values():
            sound.set_volume(0.3)
            
        # Set music volume
        pygame.mixer.music.set_volume(0.5)
        
    def play_sound(self, sound_name: str) -> None:
        """Play a sound effect if enabled.
        
        Args:
            sound_name: Name of the sound to play
        """
        if GAME_OPTIONS.sound_effects_enabled and sound_name in self.sounds:
            self.sounds[sound_name].play()
            
    def play_music(self) -> None:
        """Start playing background music if enabled."""
        if GAME_OPTIONS.music_enabled and not self.music_loaded:
            pygame.mixer.music.load(str(AUDIO_DIR / "music.wav"))
            pygame.mixer.music.play(-1)  # Loop indefinitely
            self.music_loaded = True
            
    def pause_music(self) -> None:
        """Pause currently playing music."""
        if self.music_loaded:
            pygame.mixer.music.pause()
            
    def resume_music(self) -> None:
        """Resume paused music."""
        if self.music_loaded:
            pygame.mixer.music.unpause()
            
    def stop_music(self) -> None:
        """Stop currently playing music."""
        pygame.mixer.music.stop()
        self.music_loaded = False
        
    def update_volumes(self) -> None:
        """Update volumes based on current settings."""
        volume = 0.3 if GAME_OPTIONS.sound_effects_enabled else 0
        for sound in self.sounds.values():
            sound.set_volume(volume)
            
        volume = 0.5 if GAME_OPTIONS.music_enabled else 0
        pygame.mixer.music.set_volume(volume)
        
    def play_laser(self) -> None:
        """Play laser sound effect."""
        self.play_sound("laser")
        
    def play_explosion(self) -> None:
        """Play explosion sound effect."""
        self.play_sound("explosion")
        
    def play_alien_laser(self) -> None:
        """Play alien laser sound effect."""
        self.play_sound("alien_laser")
