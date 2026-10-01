from GameFrame import TextObject, Globals, RoomObject

class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Initialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        
    def update_score(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()
        

class Lives(RoomObject):
    """
    A class for displaying the number of lives remaining
    """
    def __init__(self, room, x: int, y: int):
        """
        Initialises the lives object
        """   
        RoomObject.__init__(self, room, x, y)
        
        # load the lives images (1 to 5 hearts) into a list
        self.lives_icon = []
        for index in range(1, 6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{index}.png"))
        self.update_image()
        
    def update_image(self):
        """
        Updates the number of lives on the UI
        """
        self.set_image(self.lives_icon[Globals.LIVES - 1], 125, 23)
        

class Rescued(TextObject):
    """
    A class for showing how many astronauts have been rescued
    """
    def __init__(self, room, x: int, y: int):
        """
        Initialises the rescued counter
        """
        TextObject.__init__(self, room, x, y)
        
        # set values
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.update_rescued()
        
    def update_rescued(self):
        """
        Shows the number of astronauts rescued out of the goal
        """
        self.text = f"Rescued: {Globals.rescued} / {Globals.rescue_goal}"
        self.update_text()
        

class Streak(TextObject):
    """
    A class for showing the asteroid streak and the laser limit
    """
    def __init__(self, room, x: int, y: int):
        """
        Initialises the streak counter
        """
        TextObject.__init__(self, room, x, y)
        
        # set values
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.update_streak()
        
    def max_lasers(self):
        """
        Returns how many lasers can be on the screen at once
        """
        return min(1 + Globals.streak, 5)
        
    def update_streak(self):
        """
        Shows the streak and the laser limit
        """
        self.text = f"Streak: {Globals.streak}  Lasers: {self.max_lasers()}"
        self.update_text()
