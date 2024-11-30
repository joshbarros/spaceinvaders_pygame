"""Paused game state with options menu."""

import pygame
from typing import Optional, List, Tuple

from core.states.game_state import GameState, GameStateType, get_game_state
from config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FONT_DIR,
    MENU_FONT_SIZE,
    GAME_OPTIONS
)

class PausedState(GameState):
    """State when game is paused with options menu."""
    
    def __init__(self):
        """Initialize pause menu state."""
        self.font = pygame.font.Font(str(FONT_DIR / "Pixeled.ttf"), MENU_FONT_SIZE)
        self.selected_option = 0
        self.options = [
            ("RESUME", GameStateType.PLAYING),
            ("CRT Effect: {}".format("ON" if GAME_OPTIONS.crt_effect else "OFF"), None),
            ("Music: {}".format("ON" if GAME_OPTIONS.music_enabled else "OFF"), None),
            ("Sound Effects: {}".format("ON" if GAME_OPTIONS.sound_effects_enabled else "OFF"), None),
            ("QUIT", GameStateType.MENU)
        ]
        
    def _update_option_text(self) -> None:
        """Update the text of toggleable options."""
        self.options[1] = ("CRT Effect: {}".format("ON" if GAME_OPTIONS.crt_effect else "OFF"), None)
        self.options[2] = ("Music: {}".format("ON" if GAME_OPTIONS.music_enabled else "OFF"), None)
        self.options[3] = ("Sound Effects: {}".format("ON" if GAME_OPTIONS.sound_effects_enabled else "OFF"), None)
        
    def handle_option_selection(self) -> Optional[GameStateType]:
        """Handle the selection of a menu option.
        
        Returns:
            New game state if needed
        """
        option_text, action = self.options[self.selected_option]
        
        if action == GameStateType.PLAYING:
            # Resume music when unpausing
            playing_state = get_game_state(GameStateType.PLAYING)
            playing_state.resume_game()
            return action
        elif action:
            return action
            
        # Handle toggles
        if self.selected_option == 1:  # CRT Effect
            GAME_OPTIONS.toggle_crt()
        elif self.selected_option == 2:  # Music
            GAME_OPTIONS.toggle_music()
        elif self.selected_option == 3:  # Sound Effects
            GAME_OPTIONS.toggle_sound_effects()
            
        self._update_option_text()
        return None
        
    def handle_event(self, event: pygame.event.Event) -> Optional[GameStateType]:
        """Handle pygame events.
        
        Args:
            event: Event to handle
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Resume music when unpausing with ESC
                playing_state = get_game_state(GameStateType.PLAYING)
                playing_state.resume_game()
                return GameStateType.PLAYING
            elif event.key in (pygame.K_w, pygame.K_UP):
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                return self.handle_option_selection()
                
        return None
        
    def update(self, dt: float) -> Optional[GameStateType]:
        """Update pause menu state.
        
        Args:
            dt: Delta time since last update
            
        Returns:
            New game state if needed
        """
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the pause menu.
        
        Args:
            screen: Surface to draw on
        """
        # Darken the background
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        screen.blit(overlay, (0, 0))
        
        # Draw menu title
        title_surf = self.font.render("PAUSED", False, 'white')
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)
        
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
