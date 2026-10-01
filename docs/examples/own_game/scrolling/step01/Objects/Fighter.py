from GameFrame import RoomObject, Globals
import pygame

class Fighter(RoomObject):
    """
    A ship that flies up the screen and dodges falling rocks
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image, then turn it to face up the screen
        image = self.load_image("Ship.png")
        self.set_image(image, 80, 80)
        self.rotate(90)
        
        # register events
        self.handle_key_events = True
        self.register_collision_object("Rock")
        
    def key_pressed(self, key):
        """
        Moves left and right with the A and D keys
        """
        if key[pygame.K_a] and self.x > 0:
            self.x_speed = -8
        elif key[pygame.K_d] and self.x < Globals.SCREEN_WIDTH - self.width:
            self.x_speed = 8
        else:
            self.x_speed = 0
            
    def handle_collision(self, other, other_type):
        """
        Ends the game when a rock hits the ship
        """
        if other_type == "Rock":
            self.room.running = False
