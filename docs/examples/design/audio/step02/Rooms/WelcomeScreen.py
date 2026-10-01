from GameFrame import Level, Globals
from Objects.Title import Title

class WelcomeScreen(Level):
    """
    Initial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # add title object
        self.add_room_object(Title(self, 240, 200))
        
        # play background music, unless it's already playing
        if not Globals.music_playing:
            self.bg_music = self.load_sound("Music.mp3")
            self.bg_music.play(loops=-1)
            Globals.music_playing = True
