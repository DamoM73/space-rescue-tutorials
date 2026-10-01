from GameFrame import Level, Globals, TextObject
from Objects.HighScoreEntry import HighScoreEntry

class HighScores(Level):
    """
    Screen for saving the player's score and showing the top scores
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # show the player's score and ask for their initials
        self.message = TextObject(self, 380, 120, f"Your score: {Globals.SCORE}", 50, 'Arial Black', (255,255,255))
        self.add_room_object(self.message)
        self.prompt = TextObject(self, 380, 220, "Type your initials, then press Enter", 30, 'Arial Black', (255,255,255))
        self.add_room_object(self.prompt)
        
        # add the initials entry box
        self.add_room_object(HighScoreEntry(self, 580, 290))
        
    def show_scores(self, top_scores):
        """
        Shows the top scores, then goes back to the welcome screen
        """
        self.prompt.text = "Top scores"
        self.prompt.update_text()
        
        # one line of text for each score
        y = 400
        for name, score in top_scores:
            line = TextObject(self, 540, y, f"{name}   {score}", 40, 'Arial Black', (255,255,255))
            self.add_room_object(line)
            y += 50
            
        # go back to the welcome screen after 5 seconds
        self.set_timer(150, self.finish)
        
    def finish(self):
        """
        Ends this Room so the game goes back to the welcome screen
        """
        self.running = False
