"""Game over state module."""

import pygame
from typing import Optional

from core.states.game_state import GameState, GameStateType
from config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FONT_SIZE,
    FONT_NAME,
    WHITE,
    GAME_OPTIONS
)

class GameOverState(GameState):
    """Game over screen state."""
    
    def __init__(self, final_score: int = 0):
        """Initialize game over state.
        
        Args:
            final_score: Final score to display
        """
        super().__init__()
        self.final_score = final_score
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        
    def update(self, dt: float) -> Optional[GameStateType]:
        """Update game over state.
        
        Args:
            dt: Time delta in seconds
            
        Returns:
            New game state if needed
        """
        keys = pygame.key.get_pressed()
        
        # Check for restart or quit
        if keys[pygame.K_SPACE]:
            # Stop any playing music before transitioning
            if GAME_OPTIONS.music_enabled and pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            return GameStateType.PLAYING
            
        if keys[pygame.K_ESCAPE]:
            return GameStateType.MENU
            
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the game over screen.
        
        Args:
            screen: Surface to draw on
        """
        # Fill background
        screen.fill((0, 0, 0))
        
        # Draw game over text
        game_over_text = self.font.render("GAME OVER", True, WHITE)
        score_text = self.font.render(f"Final Score: {self.final_score}", True, WHITE)
        restart_text = self.font.render("Press SPACE to restart", True, WHITE)
        menu_text = self.font.render("Press ESC for menu", True, WHITE)
        
        # Position text
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        
        # Draw text
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(menu_text, menu_rect)
