"""Core package for the Houssam Ascension life-RPG prototype."""

from .engine import GameEngine
from .state import load_game_state, save_game_state

__all__ = ["GameEngine", "load_game_state", "save_game_state"]
