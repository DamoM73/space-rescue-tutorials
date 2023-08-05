# Add Laser

Since Zork is hurling Asteroids at our defenceless space ship, we better give it something to fight back. In this lesson will will arm the space ship with a laser.

## Shooting the Laser

### Planning

We want to ship to spawn a laser whenever we press the space key. 

![Laser IPO](assets/img/laser_IPO.png)

This involves:

- creating a new laser class
- adding an event handler of the space key which create a laser object
- make the laser object move across the room when spawned
- deleting the laser object when it leaves the room

We already know how to do all this, so lets get to the coding.

### Coding

#### `Objects/Laser.py`

**Create** a new file in the `Objects` folder called `Laser.py` and then add the following code to it.

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
```

The only change worth noting is:

- **line 32**: since the laser is moving right, we delete it after it's `x` has moved past the screen width

**Save** `Objects/Laser.py`

### `Objects/__init__.py`

We need to tell GameFrame that we have added a new RoomObject to the `Objects` folder.

**Open** `Objects/__init__.py` and add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 5
from Objects.Title import Title
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Asteroid import Asteroid
from Objects.Laser import Laser
```

**Save** and **close** `Objects/__init__.py`

### `Objects/Ship.py`

**Open** `Objects/Ship.py` and add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 2, 32-33, 50-57
from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        
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
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            
    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
        
    def shoot_laser(self):
        """
        Shoots a laser from the ship
        """
        new_laser = Laser(self.room, 
                          self.x + self.width, 
                          self.y + self.height/2 - 4)
        self.room.add_room_object(new_laser)
```

Lets break that down:

- **line 2**: since we want the Ship to create a Laser object, we need to import the Laser class
- **lines 32-33**: handles the event of the space key being pressed
- **lines 50-57**: 
  - creates a new laser object at the middle of the right side of the ship
  - adds the laser object to the Room the Ship is in

```{admonition} Spliting instructions over multiple lines
:class: note
Lines **54 - 56** are actually one instruction split over 3 lines to make it easier to read.

The **[Python Style Guide](https://peps.python.org/pep-0008/)** recommends that lines of code shouldn't be more than 79 characters long. Although this isn't followed religiously, it is frown upon to write lines of code that are two long to read without scrolling sideway.

You can split arugements by placing a **linebreak** (pressing **Enter**) after any `,` (like in the code above). You can also place line breaks after `,` in list, dictionaries and tuples.

Placing long expressions inside parenthesis `( )` allows you to place a **linebreak** after any alrogithmic or Boolean operand.

This method can also be used to logically group operations in a exteremely long expression.
```

**Save** `Ship.py` and then test the code by running `MainController.py`.

## Restricting the laser

When testing, did you notice what happens if you hold down the space key? There is a constant stream of lasers flowing across the screen. You might even notice that some of the other object freeze. What is that?

Since our event lister is tied to the frame rate, it is detecting the space key press 30 times a second, and, consequently, spawning 30 lasers a second. That's a lot of lasers. We need to work out a way to restrict how many lasers can be shot a second.

### Planning

To address this issue we will limit how frequently the Ship can spawn a Laser. To do this we are going to use a **flag variable**.

```{admonition} Flag variables
:class: note
Flag variables, also known as Boolean flags, are variables used in computer programming to represent the state of a condition or a specific situation. Flag variables act as signals, indicating whether a particular condition is true or false, and they help control the flow of a program.
```

Specifically we are going to create a flag variable called `can_shoot` initialised to `True`. A laser can only spawn when `can_shoot` is `True`. Every time a laser is spawned, `can_shoot` will be set to `False` and a timer is started. When that timer ends, `can_shoot` is set back to `True`.

Lets look at that in an IPO table.

![laser with flag IPO](assets/img/laser_with_flag_IPO.png)

### Coding

#### `Objects/Ship.py`

Restricting the number of lasers is all about laser spawning, which happens in the Ship class so go back to `Objects/Ship.py` and change the highlighted code.

```{code-block} python
:linenos:
:emphasize-lines: 23, 56-62, 64-68
from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        
        self.can_shoot = True
        
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
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            
    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
        
    def shoot_laser(self):
        """
        Shoots a laser from the ship
        """
        if self.can_shoot:
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True
```

Investigating those changes:

- **line 23**: creates our flag variable and initializes it to `True`
- **line 56**: checks whether the Ship is allows to spawn a laser
- **lines 57-60**: these haven't changed, but their indentation has increased one level to place them inside the if statement.
- **line 61**: after spawning a laser, the `can_shoot` flag is set to `False` to prevent other lasers being spawned
- **line 62**: sets a timer which will call the `reset_shot` function when finished.
- **lines 64-68**: this function will be called when the timer has reached 0. It changed the `can_shoot` flag back to `True`.

**Save** `Ship.py` then run `MainController.py` to test that everything is working as planned.

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
```

### `Objects/__init__.py`

```{code-block} python
:linenos:
from Objects.Title import Title
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Asteroid import Asteroid
from Objects.Laser import Laser
```

### `Objects/Ship.py`

```{code-block} python
:linenos:
from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        
        self.can_shoot = True
        
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
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            
    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
        
    def shoot_laser(self):
        """
        Shoots a laser from the ship
        """
        if self.can_shoot:
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True
```