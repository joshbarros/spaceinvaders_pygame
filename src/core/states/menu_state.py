"""Menu state implementation."""

import pygame
from typing import Optional, List, Tuple

from core.states.game_state import GameState, GameStateType
from config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FONT_DIR,
    MENU_FONT_SIZE,
    GAME_OPTIONS
)

class MenuState(GameState):
    """Main menu state."""
    
    def __init__(self):
        """Initialize menu state."""
        super().__init__()
        self.font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), MENU_FONT_SIZE)
        self.selected_option = 0
        self.options = [
            ("START GAME", GameStateType.PLAYING),
            ("OPTIONS", None),  # Will toggle options menu
            ("QUIT", None)  # Will exit game
        ]
        
        # Title setup
        title_font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), MENU_FONT_SIZE * 2)
        self.title_surf = title_font.render("SPACE INVADERS", False, 'white')
        self.title_rect = self.title_surf.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        )
        
    def handle_event(self, event: pygame.event.Event) -> Optional[GameStateType]:
        """Handle pygame events.
        
        Args:
            event: Event to handle
            
        Returns:
            New game state if needed
        """
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                option_text, action = self.options[self.selected_option]
                if action:
                    return action
                elif option_text == "OPTIONS":
                    return GameStateType.OPTIONS
                elif option_text == "QUIT":
                    pygame.quit()
                    exit()
                    
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the menu.
        
        Args:
            screen: Surface to draw on
        """
        # Draw background
        screen.fill((0, 0, 0))
        
        # Draw title
        screen.blit(self.title_surf, self.title_rect)
        
        # Draw menu options
        for i, (text, _) in enumerate(self.options):
            color = 'yellow' if i == self.selected_option else 'white'
            text_surf = self.font.render(text, False, color)
            text_rect = text_surf.get_rect(
                center=(SCREEN_WIDTH // 2, 
                       SCREEN_HEIGHT // 2 + i * 50)
            )
            screen.blit(text_surf, text_rect)
            
        # Draw credits at the bottom
        credits_font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), MENU_FONT_SIZE // 2)
        credits_surf = credits_font.render("Game by Josue Barros - 2025", False, 'white')
        credits_rect = credits_surf.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        )
        screen.blit(credits_surf, credits_rect)
