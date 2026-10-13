from GameFrame import RoomObject

class Block(RoomObject):
    """
    A solid block
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Repair_kit.png")
        self.set_image(image, 42, 42)
