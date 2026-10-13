from GameFrame import RoomObject, Globals
import pygame

class ShipMenu(RoomObject):
    """
    A menu for choosing the player's ship
    """
    def __init__(self, room, x, y):
        """
        Initialise the ship menu
        """
        RoomObject.__init__(self, room, x, y)
        
        # load the menu images (each one highlights a different ship)
        self.menu_images = []
        for index in range(2):
            self.menu_images.append(self.load_image(f"Select_ship_frames/Select_ship_{index}.png"))
        self.set_image(self.menu_images[0], 400, 145)
        
        # register for key events
        self.handle_key_events = True
        self.chosen = False
        
    def key_pressed(self, key):
        """
        Choose a ship with the S or A key
        """
        if self.chosen:
            return
        
        if key[pygame.K_s]:
            self.choose(0, "Swerver")
        elif key[pygame.K_a]:
            self.choose(1, "Attractor")
            
    def choose(self, index, ship_type):
        """
        Saves the chosen ship, highlights it, then starts the game
        """
        Globals.ship_type = ship_type
        self.set_image(self.menu_images[index], 400, 145)
        self.chosen = True
        self.set_timer(15, self.start_game)
        
    def start_game(self):
        """
        Ends this Room so the game moves on to GamePlay
        """
        self.room.running = False
