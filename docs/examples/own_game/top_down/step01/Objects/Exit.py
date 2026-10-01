from GameFrame import RoomObject

class Exit(RoomObject):
    """
    The way out of the maze
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Shield_frames/Shield_0.png")
        self.set_image(image, 42, 42)
