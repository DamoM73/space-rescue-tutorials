from GameFrame import RoomObject
import pygame

class Jumper(RoomObject):
    """
    A player that runs and jumps across blocks
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Astronaut.png")
        self.set_image(image, 56, 56)
        
        # gravity pulls the player down every frame
        self.gravity = 1
        self.on_ground = False
        
        # register events
        self.handle_key_events = True
        self.register_collision_object("Block")
        
    def key_pressed(self, key):
        """
        Runs left and right, and jumps when on the ground
        """
        if key[pygame.K_a]:
            self.x_speed = -6
        elif key[pygame.K_d]:
            self.x_speed = 6
        else:
            self.x_speed = 0
            
        if key[pygame.K_w] and self.on_ground:
            self.y_speed = -20
            
    def step(self):
        """
        Limits the falling speed and assumes we're in the air
        """
        if self.y_speed > 20:
            self.y_speed = 20
        self.on_ground = False
        
    def handle_collision(self, other, other_type):
        """
        Stops the player passing through blocks
        """
        if other_type == "Block":
            if self.prev_y + self.height <= other.y:
                # landed on top of the block
                self.y = other.y - self.height
                self.y_speed = 0
                self.on_ground = True
            elif self.prev_y >= other.y + other.height:
                # hit the bottom of the block
                self.y = other.y + other.height
                self.y_speed = 0
            else:
                # hit the side of the block
                self.x = self.prev_x
                self.x_speed = 0
