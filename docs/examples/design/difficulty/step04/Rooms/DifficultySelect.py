from GameFrame import Level
from Objects.DifficultyMenu import DifficultyMenu

class DifficultySelect(Level):
    """
    Screen for choosing the difficulty
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # add difficulty menu
        self.add_room_object(DifficultyMenu(self, 390, 361))
