import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """A class to menage bullets from the ship"""

    def __init__(self, ai_game):
        """Create a bullet objct at ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.sttings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                self.settings.bullet_height)
        self.rect.midtop = self.ship.rect.midtop

        