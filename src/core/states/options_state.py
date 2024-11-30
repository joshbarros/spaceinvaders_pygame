"""Options menu state."""

import pygame
from typing import Optional

from core.states.game_state import GameState, GameStateType
from config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FONT_DIR,
    MENU_FONT_SIZE,
    GAME_OPTIONS
)

class OptionsState(GameState):
    """Options menu state."""
    
    def __init__(self):
        """Initialize options state."""
        super().__init__()
        self.font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), MENU_FONT_SIZE)
        self.selected_option = 0
        self._update_options()
        
    def _update_options(self) -> None:
        """Update options text based on current settings."""
        self.options = [
            ("CRT Effect: {}".format("ON" if GAME_OPTIONS.crt_effect else "OFF"), None),
            ("Music: {}".format("ON" if GAME_OPTIONS.music_enabled else "OFF"), None),
            ("Sound Effects: {}".format("ON" if GAME_OPTIONS.sound_effects_enabled else "OFF"), None),
            ("Fullscreen: {}".format("ON" if GAME_OPTIONS.fullscreen else "OFF"), None),
            ("Difficulty: {}".format(GAME_OPTIONS.difficulty), None),
            ("BACK", GameStateType.MENU)
        ]
        
    def handle_event(self, event: pygame.event.Event) -> Optional[GameStateType]:
        """Handle pygame events.
        
        Args:
            event: Event to handle
            
        Returns:
            New game state if needed
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return GameStateType.MENU
            elif event.key in (pygame.K_w, pygame.K_UP):
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                option_text, action = self.options[self.selected_option]
                
                if action:
                    return action
                    
                # Handle toggles
                if self.selected_option == 0:  # CRT Effect
                    GAME_OPTIONS.toggle_crt()
                elif self.selected_option == 1:  # Music
                    GAME_OPTIONS.toggle_music()
                elif self.selected_option == 2:  # Sound Effects
                    GAME_OPTIONS.toggle_sound_effects()
                elif self.selected_option == 3:  # Fullscreen
                    GAME_OPTIONS.toggle_fullscreen()
                elif self.selected_option == 4:  # Difficulty
                    difficulties = ["Easy", "Normal", "Hard"]
                    current_idx = difficulties.index(GAME_OPTIONS.difficulty)
                    GAME_OPTIONS.difficulty = difficulties[(current_idx + 1) % len(difficulties)]
                    
                self._update_options()
                
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the options menu.
        
        Args:
            screen: Surface to draw on
        """
        # Draw background
        screen.fill((0, 0, 0))
        
        # Draw title
        title_surf = self.font.render("OPTIONS", False, 'white')
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)
        
        # Draw options
        for i, (text, _) in enumerate(self.options):
            color = 'yellow' if i == self.selected_option else 'white'
            text_surf = self.font.render(text, False, color)
            text_rect = text_surf.get_rect(
                center=(SCREEN_WIDTH // 2, 
                       SCREEN_HEIGHT // 2 + i * 50)
            )
            screen.blit(text_surf, text_rect)
            
        # Draw credits
        credits_font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), MENU_FONT_SIZE // 2)
        credits_surf = credits_font.render("Game by Josue Barros - 2025", False, 'white')
        credits_rect = credits_surf.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        )
        screen.blit(credits_surf, credits_rect)
