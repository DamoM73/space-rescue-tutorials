from GameFrame import Level
from Objects.ShipMenu import ShipMenu

class ShipSelect(Level):
    """
    Screen for choosing the player's ship
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # add ship menu
        self.add_room_object(ShipMenu(self, 440, 327))
