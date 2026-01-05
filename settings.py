class Setting:
    """Class to store all the settings of the game"""

    def __init__(self):
        """Initialize game's settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_hight = 700
        self.bg_color = (230,230,250)

        #Speed of the ship
        self.ship_speed = 1.5
        self.ships_limit = 3

        #Bullets settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 247)
        self.bullets_allowed = 5

        #Alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

