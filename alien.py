import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the aliens image and set it's rect attributes
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Start each new alien at the near top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store aliens exact horizontal position
        self.x = float(self.rect.x)