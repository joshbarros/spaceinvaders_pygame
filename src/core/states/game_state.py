"""Game state management."""

import pygame
from enum import Enum, auto
from typing import Optional, Dict

class GameStateType(Enum):
    """Available game states."""
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    VICTORY = auto()
    OPTIONS = auto()

class GameState:
    """Base class for game states."""
    
    def handle_event(self, event: pygame.event.Event) -> Optional[GameStateType]:
        """Handle pygame events.
        
        Args:
            event: Event to handle
            
        Returns:
            New game state if needed
        """
        return None
        
    def update(self, dt: float) -> Optional[GameStateType]:
        """Update game state.
        
        Args:
            dt: Delta time since last update
            
        Returns:
            New game state if needed
        """
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the current state.
        
        Args:
            screen: Surface to draw on
        """
        pass

class GameStateManager:
    """Manages game states and transitions."""
    
    def __init__(self, initial_state: GameStateType = GameStateType.MENU):
        """Initialize the state manager.
        
        Args:
            initial_state: Initial game state
        """
        self._states: Dict[GameStateType, GameState] = {}
        self._current_state: Optional[GameState] = None
        self._current_state_type: Optional[GameStateType] = initial_state
        
    def register_state(self, state_type: GameStateType, state: GameState) -> None:
        """Register a state with the manager.
        
        Args:
            state_type: Type of state to register
            state: State instance
        """
        self._states[state_type] = state
        if state_type == self._current_state_type:
            self._current_state = state
            
    def switch_state(self, state_type: GameStateType) -> None:
        """Switch to a different state.
        
        Args:
            state_type: Type of state to switch to
        """
        if state_type in self._states:
            self._current_state = self._states[state_type]
            self._current_state_type = state_type
            
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle events in current state.
        
        Args:
            event: Event to handle
        """
        if self._current_state:
            new_state = self._current_state.handle_event(event)
            if new_state:
                self.switch_state(new_state)
                
    def update(self, dt: float) -> None:
        """Update current state.
        
        Args:
            dt: Delta time since last update
        """
        if self._current_state:
            new_state = self._current_state.update(dt)
            if new_state:
                self.switch_state(new_state)
                
    def draw(self, screen: pygame.Surface) -> None:
        """Draw current state.
        
        Args:
            screen: Surface to draw on
        """
        if self._current_state:
            self._current_state.draw(screen)

# Global state manager instance
_state_manager = GameStateManager(GameStateType.MENU)

def get_game_state(state_type: GameStateType) -> Optional[GameState]:
    """Get a game state by type.
    
    Args:
        state_type: Type of state to get
        
    Returns:
        State instance if found
    """
    return _state_manager._states.get(state_type)
