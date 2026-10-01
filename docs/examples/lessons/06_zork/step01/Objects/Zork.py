from GameFrame import RoomObject

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
