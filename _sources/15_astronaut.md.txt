# Add Astronaut

```{topic} In this lesson you will:
- apply learnt knowledge to plan code using IPO tables
- apply learnt knowledge to create a new object
- apply learnt knowledge to move object across a screen
- apply learnt knowledge to keep bounce an object of the edges of the screen
- apply learnt knowledge to delete an object once it has exited the screen
- apply learnt knowledge to deal with collisions
```

Now we will add our target of rescue, the astronauts. All the code in the process will not introduce any new concepts, so lets get straight into the planning.

## Planning

We want to:

- create an Astronaut class
- have Zork randomly spawn an Astronaut
- upon spawn the Astronaut moves across the screen
- if the Astronaut exits the screen left, is it deleted
- when Astronauts collides with the Ship they are rescued and disappear
- when Astronauts collide with the Laser they are vaporised and disappear

Lets look at all of these in IPO tables.

![Astronaut IPO tables](assets/img/astronaut_IPOs.png)

Each of the parts of these IPO tables we have done before, the only difference is that they're arranged differently. Therefore, we should be able to get on with the coding.

## Coding

### `Objects.Astronaut.py`

In the `Objects` folder **create** a new file and call it `Astronaut.py`, then add the code below.

```{code-block} python
:linenos:
from GameFrame import RoomObject

class Astronaut(RoomObject):
    """
    Class for the astronauts escaping from Zork
    """
    
    def __init__(self,room,x,y):
        """
        Initialise the astronaut instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)
        
        # set travel direction
        self.set_direction(180, 5)
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Determines what happend to the astronaut on each tick of the game clock
        """
        self.outside_of_room()
        
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Astronaut objects
        """
        # ship collision
        if other_type == "Ship":
            self.room.delete_object(self)
            
    def outside_of_room(self):
        """
        removes astronauts that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
```

This code:

- **lines 1-17**: creates the Astronaut class
- **lines 19-20**: set the Astronaut travel direction
- **lines 22-23**: registers collisions with Ship objects
- **lines 25-29**: checks if the Astronaut is outside the room
- **lines 32-38**: handles a collision with a Ship object
- **lines 40-45**: deletes the Astronaut if it is outside of the room

**Save** `Astronaut.py`

## `Objects/__init__.py`

We have just created a new RoomObject, so we need to let GameFrame know by editing the `Objects/__init__.py`.

**Open** `Objects/__init__.py` and then add the highlighted code:

```{code-block} python
:linenos:
:emphasize-lines: 6
from Objects.Title import Title
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Asteroid import Asteroid
from Objects.Laser import Laser
from Objects.Astronaut import Astronaut
```

**Save** and **close** `Objects/__init__.py`

### `Objects/Zork.py`

We know need to make Zork randomly spawn Astronauts

**Open** `Objects/Zork.py` and add the highlighted code below to the `__init__()` method:

```{code-block} python
:linenos:
:lineno-start: 10
:emphasize-lines: 19-21
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        
        # set inital movement
        self.y_speed = random.choice([-10, 10])
        
        # start asteroid timer
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
        # start astronaut timer
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
```

Then add the following code to the bottom of `Objects/Zork.py`:

```{code-block} python
:linenos:
:lineno-start: 58
    def spawn_astronaut(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn astronaut and add to room
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        
        # reset timer for next astronaut spawn
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
```

**Save** `Objects/Zork.py` and the test it by running `MainController.py`

### `Objects/Laser.py`

Finally we need to deal with the Astronaut and Laser collision.

**Open** `Objects/Laser.py` and the following highlighted code.

```{code-block} python
:linenos:
:emphasize-lines: 24, 46-47
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
        self.register_collision_object("Astronaut")
        
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
        elif other_type == "Astronaut":
            self.room.delete_object(other)
```

**Save** `Objects/Laser.py` and the test it by running `MainController.py`

## Commit and Push

We have finished and tested another section of code so we should make a Git commit.

To do this:

1. In GitHub Desktop go to the bottom left-hand box and write into the summary **Added astronaut**.
2. Click on **Commit to main**
3. Click on **Push origin**

Now the work from this lesson is committed and synced with the online repo.

## Completed File States

Below are all the files we used in this lesson in their finished state. **Use this to check if your code is correct**.

### `Objects/Astronaut.py`

```{code-block} python
:linenos:
from GameFrame import RoomObject

class Astronaut(RoomObject):
    """
    Class for the astronauts escaping from Zork
    """
    
    def __init__(self,room,x,y):
        """
        Initialise the astronaut instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)
        
        # set travel direction
        self.set_direction(180, 5)
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Determines what happend to the astronaut on each tick of the game clock
        """
        self.outside_of_room()
        
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Astronaut objects
        """
        # ship collision
        if other_type == "Ship":
            self.room.delete_object(self)
            
    def outside_of_room(self):
        """
        removes astronauts that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
```

### `Objects/__init__.py`

```{code-block} python
:linenos:
from Objects.Title import Title
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Asteroid import Asteroid
from Objects.Laser import Laser
from Objects.Astronaut import Astronaut
```

### `Objects/Zork.py`

```{code-block} python
:linenos:
from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Astronaut import Astronaut
import random

class Zork(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        
        # set inital movement
        self.y_speed = random.choice([-10, 10])
        
        # start asteroid timer
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
        # start astronaut timer
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
        
        
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
        
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        
        # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
    def spawn_astronaut(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn astronaut and add to room
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        
        # reset timer for next astronaut spawn
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
```

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
        self.register_collision_object("Astronaut")
        
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
        elif other_type == "Astronaut":
            self.room.delete_object(other)
```