class Setting:
    """Class to store all the settings of the game"""

    def __init__(self):
        """Initialize game's settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_hight = 700
        self.bg_color = (230,230,250)

        # ship settings
        self.ships_limit = 3

        #Bullets settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 247)
        self.bullets_allowed = 5

        #Alien setting
        self.fleet_drop_speed = 10

        #how quiqly the game speeds up
        self.speedup_scale = 1.3

        #How quickly aliens value increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    
    def initialise_dynamic_settings(self):
        """Initialize settings that changes through the game"""
        self.ship_speed = 2.0
        self.bullet_speed = 1.5
        self.alien_speed = 1.5

        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #Scoring 
        self.aliens_point = 50

    
    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.aliens_point = int(self.aliens_point * self.score_scale)




