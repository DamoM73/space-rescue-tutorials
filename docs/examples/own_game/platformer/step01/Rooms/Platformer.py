from GameFrame import Level
from Objects.Block import Block
from Objects.Jumper import Jumper

class Platformer(Level):
    """
    A platform game demo
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # a floor along the bottom of the screen
        for x in range(0, 1280, 42):
            self.add_room_object(Block(self, x, 758))
            
        # two floating platforms
        for x in range(300, 510, 42):
            self.add_room_object(Block(self, x, 600))
        for x in range(650, 860, 42):
            self.add_room_object(Block(self, x, 460))
            
        # add the player
        self.add_room_object(Jumper(self, 100, 650))
