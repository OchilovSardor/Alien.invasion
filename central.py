import sys
from time import sleep

import pygame

from settings import Setting
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        #Create an instanse to store game statistics
        #and crate a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        #Creating instanse of the Ship class
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #make the Play button
        self.play_button = Button(self, "Play")
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when player clicks Play"""
        
        button_click = self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.stats.game_active:
            #Reset the game settings
            self.settings.initialise_dynamic_settings()
            
            #reset the game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            #Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #Hide the mouse cursor
            pygame.mouse.set_visible(False)
        


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
        
        self._check_bullets_aliens_collitions()

    def _check_bullets_aliens_collitions(self):
        """Respond to a bullet aliens collitions"""
        #Remove any alien and that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.aliens_point * len(aliens)
            self.sb.prep_score()
        
        if not self.aliens:
            #Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _ship_hit(self):
        """Respond to a ship being hit by an alien"""
        if self.stats.ship_left > 0:
            #Decriment ships_sefl
            self.stats.ship_left -= 1

            #Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """
        Check if the fleet is at adge
        then update the position of all aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        #Look for an alien and ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

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
        number_rows = availabble_space_y // (3 * alien_height)

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

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check is alien have reached the bottom of  screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Threat this the same as if alien hit the ship
                self._ship_hit()
                break


    def _update_screen(self):
        """Redraw the screen during the each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Draw the score information
        self.sb.show_score()

        #Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #Make a game instanse and run the game
    ai = AlienInvasion()
    ai.run_game()
        
