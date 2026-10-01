from GameFrame import EntryTextObject, Globals, DataBaseController
import pygame

class HighScoreEntry(EntryTextObject):
    """
    Lets the player type their initials, then saves their score
    """
    def __init__(self, room, x, y):
        """
        Initialise the initials entry box
        """
        EntryTextObject.__init__(self, room, x, y, max_len=3)
        
        # set values
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,0)
        self.update_text()
        self.saved = False
        
    def key_pressed(self, key):
        """
        Types the initials, and saves them when Enter is pressed
        """
        if self.saved:
            return
        
        EntryTextObject.key_pressed(self, key)
        if key[pygame.K_RETURN] and len(self.text) > 0:
            self.save_score()
            
    def save_score(self):
        """
        Saves the score in the database, then shows the top scores
        """
        self.saved = True
        database = DataBaseController("scores.db")
        database.create_scores_table()
        database.add_score(self.text, Globals.SCORE)
        top_scores = database.get_top_scores(5)
        database.close()
        self.room.show_scores(top_scores)
