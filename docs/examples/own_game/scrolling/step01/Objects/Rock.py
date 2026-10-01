from GameFrame import RoomObject, Globals

class Rock(RoomObject):
    """
    A rock that falls down the screen
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("asteroid.png")
        self.set_image(image, 50, 49)
        
        # fall straight down (90 degrees)
        self.set_direction(90, 8)
        
    def step(self):
        """
        Removes the rock once it has left the bottom of the screen
        """
        if self.y > Globals.SCREEN_HEIGHT:
            self.room.delete_object(self)
