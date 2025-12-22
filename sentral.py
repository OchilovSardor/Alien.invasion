import sys

import pygame

class AlienInvasion:
    """Overall class to manage game asserts and behavior."""

    def __init__(self):
        """Initialise the game and create resourses."""
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Alien Invasion")

        #Set the background color
        self.bg_color = (10, 10, 40)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during the each pass through the loop
            self.screen.fill(self.bg_color)
            
            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    #Make a game instanse and run the game
    ai = AlienInvasion()
    ai.run_game()
        
