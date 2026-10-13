from GameFrame import RoomObject
import pygame

class Explorer(RoomObject):
    """
    A player that moves up, down, left and right through a maze
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Astronaut.png")
        self.set_image(image, 36, 36)
        
        # register events
        self.handle_key_events = True
        self.register_collision_object("Block")
        self.register_collision_object("Exit")
        
    def key_pressed(self, key):
        """
        Moves with the arrow keys, only while a key is held
        """
        self.x_speed = 0
        self.y_speed = 0
        if key[pygame.K_LEFT]:
            self.x_speed = -4
        elif key[pygame.K_RIGHT]:
            self.x_speed = 4
        elif key[pygame.K_UP]:
            self.y_speed = -4
        elif key[pygame.K_DOWN]:
            self.y_speed = 4
            
    def handle_collision(self, other, other_type):
        """
        Stops at walls and finishes at the exit
        """
        if other_type == "Block":
            self.blocked()
        elif other_type == "Exit":
            self.room.running = False
