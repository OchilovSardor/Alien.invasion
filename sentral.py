import sys

import pygame

from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    
    def _check_key_up_events(self, event):
        """Respond to keyup"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    
    def _update_bullets(self):
        """Update the position of the bullets and get rid of old bullets"""
        #Update bullets position
        self.bullets.update()

        #Get rid of bullets that have been disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Create an alien and find the number of aliens in row
        #Spacing between each alien is equal to one aliens width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availabble_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = availabble_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fin in the screen
        ship_height = self.ship.rect.height
        availabble_space_y = (self.settings.screen_hight - (3 * alien_height)
                              - ship_height)
        number_rows = availabble_space_y // (2 * alien_height)

        #Create a full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self, alien_number, row_number):
        """Create an alien and pace it in the row"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_screen(self):
        """Redraw the screen during the each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #Make a game instanse and run the game
    ai = AlienInvasion()
    ai.run_game()
        
