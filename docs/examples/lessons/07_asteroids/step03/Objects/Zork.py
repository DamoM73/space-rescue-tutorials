from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
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
        
        # start asteroid timer
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    
    def step(self):
        """
        Determine what happens to Zork on each tick of the game clock
        """
        self.keep_in_room()
