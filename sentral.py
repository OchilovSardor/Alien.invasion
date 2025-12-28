import sys

import pygame

from settings import Setting
from ship import Ship

class AlienInvasion:
    """Overall class to manage game asserts and behavior."""

    def __init__(self):
        """Initialise the game and create resourses."""
        pygame.init()
        self.settings = Setting()

        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width,self.settings.screen_hight))
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_hight = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #Creating instanse of the Ship class
        self.ship = Ship(self)

       
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            #Redraw the screen during the each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_key_up_events(event)

    def check_keydown_events(self, event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def check_key_up_events(self, event):
        """Respond to keyup"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Redraw the screen during the each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
               
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #Make a game instanse and run the game
    ai = AlienInvasion()
    ai.run_game()
        
