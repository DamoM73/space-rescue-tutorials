from GameFrame import Level, Globals
from Objects.Fighter import Fighter
from Objects.Rock import Rock
import random

class Scroller(Level):
    """
    A vertical scrolling demo
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set a scrolling background image
        self.set_background_image("background.png")
        self.set_background_scroll(4)
        
        # add the player near the bottom of the screen
        self.add_room_object(Fighter(self, 600, 680))
        
        # start dropping rocks
        self.set_timer(30, self.drop_rock)
        
    def drop_rock(self):
        """
        Drops a rock at a random place along the top of the screen
        """
        x = random.randint(0, Globals.SCREEN_WIDTH - 50)
        self.add_room_object(Rock(self, x, -49))
        self.set_timer(random.randint(10, 30), self.drop_rock)
