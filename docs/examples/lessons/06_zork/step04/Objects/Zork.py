from GameFrame import RoomObject
import random

class Zork(RoomObject):
    """
    A class for the game's antagonist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Zork object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        
        # set initial movement
        self.y_speed = random.choice([-10, 10])
