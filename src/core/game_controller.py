"""Main game controller."""

import pygame
import sys
from typing import Optional

from core.states.game_state import GameState, GameStateType, GameStateManager
from core.states.menu_state import MenuState
from core.states.playing_state import PlayingState
from core.states.paused_state import PausedState
from core.states.game_over_state import GameOverState
from core.states.options_state import OptionsState
from config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    GAME_OPTIONS
)

class GameController:
    """Controls the game loop and state transitions."""
    
    def __init__(self):
        """Initialize pygame and game states."""
        pygame.init()
        pygame.display.set_caption("Space Invaders")
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self._state_manager = GameStateManager()
        
        # Register all game states
        self._state_manager.register_state(GameStateType.MENU, MenuState())
        self._state_manager.register_state(GameStateType.PLAYING, PlayingState())
        self._state_manager.register_state(GameStateType.PAUSED, PausedState())
        self._state_manager.register_state(GameStateType.GAME_OVER, GameOverState())
        self._state_manager.register_state(GameStateType.OPTIONS, OptionsState())
        
        # Set initial state
        self._state_manager.switch_state(GameStateType.MENU)
        
    def run(self) -> None:
        """Run the main game loop."""
        while True:
            dt = self.clock.tick(FPS) / 1000.0  # Convert to seconds
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                # Let current state handle the event
                self._state_manager.handle_event(event)
                
            # Update and draw current state
            self._state_manager.update(dt)
            
            # Clear screen
            self.screen.fill((0, 0, 0))
            
            # Draw current state
            self._state_manager.draw(self.screen)
            
            # Update display
            pygame.display.flip()
