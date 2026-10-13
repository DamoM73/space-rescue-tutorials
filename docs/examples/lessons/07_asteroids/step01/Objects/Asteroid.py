from GameFrame import RoomObject

class Asteroid(RoomObject):
    """
    A class for Zork's dangerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("asteroid.png")
        self.set_image(image,50,49)
