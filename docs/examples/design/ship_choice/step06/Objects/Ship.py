from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame
import random

class Ship(RoomObject):
    """
    A class for the player's avatar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set images for the chosen ship
        if Globals.ship_type == "Attractor":
            self.normal_image = self.load_image("Attractor_frames/Rescue_0.png")
            self.shield_image = self.load_image("Attractor_invinc_frames/Rescue_0.png")
        else:
            self.normal_image = self.load_image("Rescue_frames/Rescue_0.png")
            self.shield_image = self.load_image("Rescue_invinc_frames/Rescue_0.png")
        self.set_image(self.normal_image,100,100)
        
        # register events
        self.handle_key_events = True
        
        self.can_shoot = True
        
        # the shield starts off
        self.shielded = False
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y_speed = -10
        elif key[pygame.K_s]:
            self.y_speed = 10
        if key[pygame.K_SPACE]:
            self.shoot_laser()
            
    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            
    def step(self):
        """
        Determine what happens to the Ship on each tick of the game clock
        """
        self.keep_in_room()
        
    def shoot_laser(self):
        """
        Shoots a laser from the ship
        """
        max_lasers = self.room.streak.max_lasers()
        if self.can_shoot and self.room.count_object("Laser") < max_lasers:
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            self.room.shoot_laser.play()
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True
            
    def shield_on(self):
        """
        Protects the ship from asteroids for a random time
        """
        self.shielded = True
        self.set_image(self.shield_image,100,100)
        self.set_timer(random.randint(150, 300), self.shield_off)
        
    def shield_off(self):
        """
        Turns the shield off again
        """
        self.shielded = False
        self.set_image(self.normal_image,100,100)
