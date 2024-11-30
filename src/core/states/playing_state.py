"""Playing state module."""

import pygame
from random import randint, choice
from typing import Optional, Tuple

from core.states.game_state import GameState, GameStateType
from core.entities.player import Player
from core.entities.alien import Alien, Extra
from core.effects.particle_system import ParticleSystem
from core.effects.starfield import StarField
from core.ui.score_display import ScoreDisplay
from core.ui.lives_display import LivesDisplay
from config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_LIVES,
    EXTRA_SPAWN_TIME_MIN,
    EXTRA_SPAWN_TIME_MAX,
    ALIEN_MIN_SPAWN_COUNT,
    ALIEN_MAX_SPAWN_COUNT,
    ALIEN_SPAWN_DELAY,
    PARTICLE_COUNT,
    PARTICLE_SPEED,
    GAME_OPTIONS,
    AUDIO_DIR
)

class PlayingState(GameState):
    """State for main gameplay."""
    
    def __init__(self):
        """Initialize playing state."""
        super().__init__()
        self.last_spawn_time = 0
        self.particles = ParticleSystem()
        self.reset_game()
        
    def reset_game(self) -> None:
        """Reset game state."""
        # Initialize sprite groups
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        
        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.spawn_aliens()  # Initial spawn
        
        # Extra setup
        self.extra = pygame.sprite.GroupSingle()
        self.last_extra_spawn = pygame.time.get_ticks()
        self.extra_spawn_time = randint(EXTRA_SPAWN_TIME_MIN, EXTRA_SPAWN_TIME_MAX)
        
        # Score and lives setup
        self.score = 0
        self.lives = PLAYER_LIVES
        
        # Timing setup
        self.last_spawn_time = pygame.time.get_ticks()
        
        # Effects setup
        self.particles = ParticleSystem()
        self.starfield = StarField()
        
        # UI setup
        self.score_display = ScoreDisplay()
        self.lives_display = LivesDisplay()
        
        # Music setup
        if GAME_OPTIONS.music_enabled:
            pygame.mixer.music.load(str(AUDIO_DIR / "music.wav"))
            pygame.mixer.music.play(-1)
            
    def spawn_aliens(self) -> None:
        """Spawn new aliens."""
        colors = ['red', 'green', 'yellow']
        count = randint(ALIEN_MIN_SPAWN_COUNT, ALIEN_MAX_SPAWN_COUNT)
        
        for _ in range(count):
            color = choice(colors)
            x = randint(50, SCREEN_WIDTH - 50)
            y = randint(-100, 0)  # Start above screen
            self.aliens.add(Alien(x, y, color))
            
    def check_alien_spawning(self) -> None:
        """Check if it's time to spawn new aliens."""
        now = pygame.time.get_ticks()
        if now - self.last_spawn_time >= ALIEN_SPAWN_DELAY:
            self.last_spawn_time = now
            self.spawn_aliens()
            
    def handle_collisions(self) -> None:
        """Handle all game collisions."""
        if not self.player.sprite:
            return
            
        # Alien lasers hitting player
        for laser in self.alien_lasers:
            if pygame.sprite.spritecollide(laser, self.player, False):
                laser.kill()
                self.lives -= 1
                # Create explosion particles
                self.particles.create_explosion(
                    self.player.sprite.rect.center,
                    'explosion',
                    PARTICLE_COUNT,
                    PARTICLE_SPEED
                )
                if self.lives <= 0:
                    self.player.sprite.kill()
                
        # Player lasers hitting aliens
        for laser in self.player.sprite.lasers:
            aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
            if aliens_hit:
                for alien in aliens_hit:
                    laser.kill()
                    self.score += alien.value
                    # Create hit particles
                    self.particles.create_explosion(
                        alien.rect.center,
                        'hit',
                        PARTICLE_COUNT // 2,  # Smaller explosion for hits
                        PARTICLE_SPEED
                    )
                    
        # Direct collisions between player and aliens
        if pygame.sprite.spritecollide(self.player.sprite, self.aliens, True):
            self.lives -= 1
            # Create large explosion
            self.particles.create_explosion(
                self.player.sprite.rect.center,
                'explosion',
                PARTICLE_COUNT * 2,  # Bigger explosion for direct hits
                PARTICLE_SPEED
            )
            if self.lives <= 0:
                self.player.sprite.kill()
                
    def spawn_extra(self) -> None:
        """Spawn extra UFO if time has passed."""
        now = pygame.time.get_ticks()
        if now - self.last_extra_spawn >= self.extra_spawn_time:
            # Randomly choose which side the extra alien appears from
            side = choice(['left', 'right'])
            self.extra.add(Extra(side))
            self.last_extra_spawn = now
            self.extra_spawn_time = randint(EXTRA_SPAWN_TIME_MIN, EXTRA_SPAWN_TIME_MAX)
            
    def update(self, dt: float) -> Optional[GameStateType]:
        """Update game state.
        
        Args:
            dt: Time delta in seconds
            
        Returns:
            New game state if needed
        """
        # Check for pause
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return GameStateType.PAUSED
            
        # Update all game objects
        if self.player.sprite:
            self.player.sprite.update()
            
        self.aliens.update()
        self.extra.update()
        self.alien_lasers.update()
        self.particles.update(dt)
        self.starfield.update(dt)
        
        # Spawn new aliens
        self.check_alien_spawning()
        
        # Check collisions
        self.handle_collisions()
        
        # Spawn extra
        self.spawn_extra()
        
        # Check game over
        if self.lives <= 0:
            return GameStateType.GAME_OVER
            
        return None
        
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the game state.
        
        Args:
            screen: Surface to draw on
        """
        # Draw background
        screen.fill((0, 0, 0))
        
        # Draw starfield
        self.starfield.draw(screen)
        
        # Draw game objects
        self.player.draw(screen)
        self.aliens.draw(screen)
        self.extra.draw(screen)
        self.alien_lasers.draw(screen)
        if self.player.sprite:
            self.player.sprite.lasers.draw(screen)
            
        # Draw particles
        self.particles.draw(screen)
        
        # Draw UI
        self.score_display.draw(screen, self.score)
        self.lives_display.draw(screen, self.lives)
