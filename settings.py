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

        #Bullets settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 247)

