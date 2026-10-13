from GameFrame import RoomObject, Globals
import pygame

class DifficultyMenu(RoomObject):
    """
    A menu for choosing how hard the game is
    """
    def __init__(self, room, x, y):
        """
        Initialise the difficulty menu
        """
        RoomObject.__init__(self, room, x, y)
        
        # load the menu images (each one highlights a different choice)
        self.menu_images = []
        for index in range(3):
            self.menu_images.append(self.load_image(f"Select_difficulty_frames/Select_difficulty_{index}.png"))
        self.set_image(self.menu_images[1], 500, 78)
        
        # register for key events
        self.handle_key_events = True
        self.chosen = False
        
    def key_pressed(self, key):
        """
        Choose a difficulty with the E, M or H key
        """
        if self.chosen:
            return
        
        if key[pygame.K_e]:
            self.choose(0, 30, 180, 7)
        elif key[pygame.K_m]:
            self.choose(1, 15, 150, 10)
        elif key[pygame.K_h]:
            self.choose(2, 8, 90, 14)
            
    def choose(self, index, spawn_min, spawn_max, speed):
        """
        Saves the chosen difficulty, highlights it, then starts the game
        """
        Globals.asteroid_spawn_min = spawn_min
        Globals.asteroid_spawn_max = spawn_max
        Globals.asteroid_speed = speed
        self.set_image(self.menu_images[index], 500, 78)
        self.chosen = True
        self.set_timer(15, self.start_game)
        
    def start_game(self):
        """
        Ends this Room so the game moves on to GamePlay
        """
        self.room.running = False
