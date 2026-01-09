import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        "Initialize the button attributes"
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set the dimentions and the properties of the button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_colot = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Built a button rect ofbject and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepared only once
        self._prep_msg(msg)



    def _prep_msg(self, msg):
        """Turning msg into render image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_colot,
               self.button_color)
        self.msg_imag_rect = self.msg_image.get_rect()
        self.msg_imag_rect.center = self.rect.center

    def draw_button(self):
        """Draw a button and then draw a message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_imag_rect) 