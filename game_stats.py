class GameStats:
    """Track statistics for an alien invasion"""

    def __init__(self, ai_game):
        """Initialize the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #set the game to an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ships_limit