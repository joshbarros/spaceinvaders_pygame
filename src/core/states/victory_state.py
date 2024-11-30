"""Victory state implementation."""

import pygame
from typing import Optional

from core.states.game_state import GameState, GameStateType
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_DIR

class VictoryState(GameState):
    """Victory state."""
    
    def __init__(self, final_score: int = 0):
        """Initialize victory state.
        
        Args:
            final_score: Final score achieved
        """
        self.font = pygame.font.Font(str(FONT_DIR / 'Pixeled.ttf'), 20)
        self.text = self.font.render('VICTORY!', False, 'white')
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
        
        self.score = self.font.render(f'FINAL SCORE: {final_score}', False, 'white')
        self.score_rect = self.score.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        )
        
        self.instruction = self.font.render('PRESS SPACE TO PLAY AGAIN', False, 'white')
        self.instruction_rect = self.instruction.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT * 2/3)
        )
        
    def update(self, dt: float) -> Optional[GameStateType]:
        """Update victory state.
        
        Args:
            dt: Delta time since last update
        """
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw victory state.
        
        Args:
            screen: Surface to draw on
        """
        screen.blit(self.text, self.text_rect)
        screen.blit(self.score, self.score_rect)
        screen.blit(self.instruction, self.instruction_rect)
        
    def handle_event(self, event: pygame.event.Event) -> Optional[GameStateType]:
        """Handle pygame events.
        
        Args:
            event: Event to handle
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return GameStateType.PLAYING
        return None
