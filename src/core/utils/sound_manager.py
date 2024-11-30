"""Sound management singleton."""

from typing import Dict
import pygame

from config.settings import (
    AUDIO_DIR,
    MUSIC_VOLUME,
    LASER_VOLUME,
    EXPLOSION_VOLUME
)

class SoundManager:
    """Singleton class for managing game sounds."""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._sounds: Dict[str, pygame.mixer.Sound] = {
                'music': pygame.mixer.Sound(str(AUDIO_DIR / 'music.wav')),
                'laser': pygame.mixer.Sound(str(AUDIO_DIR / 'laser.wav')),
                'explosion': pygame.mixer.Sound(str(AUDIO_DIR / 'explosion.wav'))
            }
            
            # Set volumes
            self._sounds['music'].set_volume(MUSIC_VOLUME)
            self._sounds['laser'].set_volume(LASER_VOLUME)
            self._sounds['explosion'].set_volume(EXPLOSION_VOLUME)
            
            self._initialized = True
    
    def play_music(self) -> None:
        """Start playing background music in loop."""
        self._sounds['music'].play(loops=-1)
    
    def play_laser(self) -> None:
        """Play laser sound effect."""
        self._sounds['laser'].play()
    
    def play_explosion(self) -> None:
        """Play explosion sound effect."""
        self._sounds['explosion'].play()
    
    def stop_all(self) -> None:
        """Stop all sounds."""
        for sound in self._sounds.values():
            sound.stop()
