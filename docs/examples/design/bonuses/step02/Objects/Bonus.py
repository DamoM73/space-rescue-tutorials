from GameFrame import RoomObject, Globals

class RepairKit(RoomObject):
    """
    A bonus that gives the ship an extra life
    """
    def __init__(self, room, x, y):
        """
        Initialise the repair kit
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Repair_kit.png")
        self.set_image(image, 42, 42)
        
        # set travel direction
        self.set_direction(180, 6)
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Removes the repair kit once it has left the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
            
    def handle_collision(self, other, other_type):
        """
        Gives the ship an extra life, up to 5 lives
        """
        if other_type == "Ship":
            self.room.delete_object(self)
            self.room.life_gained.play()
            if Globals.LIVES < 5:
                Globals.LIVES += 1
                self.room.lives.update_image()

class Shield(RoomObject):
    """
    A bonus that protects the ship from asteroids for a while
    """
    def __init__(self, room, x, y):
        """
        Initialise the shield
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Shield_frames/Shield_0.png")
        self.set_image(image, 46, 46)
        
        # set travel direction
        self.set_direction(180, 6)
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Removes the shield once it has left the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
            
    def handle_collision(self, other, other_type):
        """
        Turns on the ship's shield
        """
        if other_type == "Ship":
            self.room.delete_object(self)
            self.room.shield_up.play()
            other.shield_on()
