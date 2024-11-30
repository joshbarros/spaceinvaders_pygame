"""Main entry point for Space Invaders game."""

from core.game_controller import GameController

def main():
    """Initialize and run the game."""
    game = GameController()
    game.run()

if __name__ == '__main__':
    main()
