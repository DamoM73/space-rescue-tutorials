# Laser Asteroid Collision

We have our lasers shooting at a reasonable frequency, now we need them to do something. Specifically we will make them destroy any asteroids that they collide with.

## Planning

We have written very similar code to address the collision between an Asteroid and the Ship. This time, instead of ending the game, we simply want to destroy the asteroid.

Stating this clearly, upon collision between an Asteroid and a Laser we want:

- the asteroid to be destroyed
- the laser to keep moving across the screen

We need to work out how to destroy objects. Check the GameFame Documentation under the [RoomObjects methods](documentation.md#roomobject-methods) and you will find the `delete_object` method that removes an object from the room.

We will place the code, summarised in the IPO table below, in the Laser class.

![Laser Asteroid collision IPO](assets/img/laser_asteroid_collision_IPO.png)

## Coding

Remember in GameFrame handling collisions is a two step process. First you must register which object collisions to detect using the `register_collision_object` method, and then create a methods called `handle_collision` which holds the game logic associated with the collision.

### `Objects/Laser.py`

**Open** `Objects/Laser.py` and add the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 22-23, 38-44
from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 33, 9)
        
        # set movement
        self.set_direction(0, 20)
        
        # handle events
        self.register_collision_object("Asteroid")
        
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)
            
    # --- Event handlers
    def handle_collision(self, other, other_type):
        """
        Handles laser collisions with other registered objects
        """
        if other_type == "Asteroid":
            self.room.delete_object(other)
```

Most of this code should be familiar, but we'll investigate it anyway:

- **lines 22-23**: registers collisions with `Asteroid` objects as an event that must be handled
- **lines 38-44**: handles registered collisions
- **line 43**: handles collisions with `Asteroid` objects
- **line 44**:
  - deletes the `other` object - in this case the asteroid the laser has collided with
  - from the room that this ship (`self`) is in

**Save** `Laser.py` then run `MainController.py` to test that everything is working as planned.

## Commit and Push

We have finished and tested another section of code so we should make a Git commit.

To do this:

1. In GitHub Desktop go to the bottom left-hand box and write into the summary `Created GamePlay room`.
2. Click on **Commit to main**
3. Click on **Push origin**

Now the work from this lesson is committed and synced with the online repo.

## Completed File States

Below are all the files we used in this lesson in their finished state. **Use this to check if your code is correct**.

### `Objects/Laser.py`

```{code-block} python
:linenos:
from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 33, 9)
        
        # set movement
        self.set_direction(0, 20)
        
        # handle events
        self.register_collision_object("Asteroid")
        
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)
            
    # --- Event handlers
    def handle_collision(self, other, other_type):
        """
        Handles laser collisions with other registered objects
        """
        if other_type == "Asteroid":
            self.room.delete_object(other)
```