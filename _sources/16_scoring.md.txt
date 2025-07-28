# Add Scoring

```{topic} In this lesson you will:
- learn how to create a TestObjects
- apply learnt knowledge to add object to rooms
- apply learnt knowledge to use the variables in `Globals.py`
- apply learnt knowledge to plan code using IPO tables
- learn how to dynamically change values in `Globals.py`
```

Now we have all our moving part, it's time to reward the player for their efforts, and what better way to reward them, than using scoring.

GameFrame is an event-driven framework, so the easiest way in incorporate scoring it to connect it to various events.

We will be providing the player with both positive and negative scoring events:

- Rescuing an astronaut &rarr; +50 points
- Shooting an asteroid &rarr; + 5 points
- Shooting an astronaut &rarr; -10 points

Lets work out how we can incorporate this into our code.

## Display Score

### Planning

First thing we need to do is find the scoring mechanism. Look to the GameFrame Documentation under the **[Globals variables](documentation.md#globals-variables)** you will see a variable called `SCORE`. We can use this to keep track of the score.

Next we need to work how we can draw numbers onto the screen. Again, referring to the GameFrame Documents you will notice the **[Text Object](documentation.md#text-object)** which specialises in displaying text. The docs also tell us that it is a special type of RoomObject, so we can treat it like a RoomObject. The `__init__()` requires extra arguments when you instantiate a TextObject. The TextObject also has a method to write new text values to the screen.

So we have our two mechanisms for recording and displaying the score. Before we start changing the score, lets try to display the current SCORE on the screen.

### Coding

#### `Objects/Hud.py`

In the `Objects` folder **create** a new file called `Hud.py`, then enter the following code:

```{code-block} python
:linenos:
from GameFrame import TextObject, Globals

class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
```

```{admonition} File name and class name can differ
:class: note
Before we unpack this code, it is worth noting that, for the first time, the name of the class and the file name differs. They don't have to be the same. We are going to have two HUD (Heads Up Display) elements: score and lives. It make sense to keep these two classes in the same file. Alternatively we could have made two files `score.py` and `lives.py`. You will find that in coding there are many valid paths to the destination.
```

Exploring this code a bit more:

- **line 1**: the `Score` class is a `TextObject` and the variable `SCORE` is part of `GameFrame.Globals` so these need to be imported.
- **lines 7-12**: 
  - define the class as a subclass of the `TextObjects` class
  - identifies four arguments that must be passed when creating a `Score` object
    - `room` &rarr; the room the object will be placed in
    - `x` &rarr; the x coordinate for the object
    - `y` &rarr; the y coordinate for the object
    - `text` &rarr; the text that is going to be displayed
- **lines 15-18**: sets all the font values for the text
- **line 19**: write the text to the screen. Without the method call nothing will appear on the screen.

**Save** `Hud.py`.

#### `Objects.__init__.py`

**Open** `Objects.__init__.py` and add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 7
from Objects.Title import Title
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Asteroid import Asteroid
from Objects.Laser import Laser
from Objects.Astronaut import Astronaut
from Objects.Hud import Score
```

**Save** and **close** `Objects.__init__.py`.

## `Rooms/GamePlay.py`

Finally we need to add the Score to the GamePlay class.

**Open** `Rooms/GamePlay.py` and add the highlighted code.

```{code-block} python
:linenos:
:emphasize-lines: 4, 17-21
from GameFrame import Level, Globals
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hud import Score

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add objects
        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self,1120, 50))
        
        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
```


**Save** and **close** `Rooms/GamePlay.py` then run `MainController.py` to see if our score appears on the screen.

## Changing score

We have a score on our screen, now we need a way to change that score. Looking at our objective, certain collision events will result in points being awarded or taken away. The easiest way to achieve this is to create a method that can be called to update the score.

### Planning

The score updating method will need to do two things:

1. change the value of the global score variable
2. write the new score on the screen

Expressing that in an IPO table:

![score update IPO](assets/img/score_update_IPO.png)

Lets put that into code.

### Coding

**Open** `Objects/Hud.py` and add the following code to the end of the `Score` class

```{code-block} python
:linenos:
:lineno-start: 21      
    def update_score(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()
```

Breaking that code down:

- **line 21**: defines a method used to change the score
- **line 25**: adjusts the `Global.SCORE` value by the provided `change` argument
- **line 26**: changes the value of the Score's text to the new value of `Globals.SCORE`
- **line 27**: writes the new text to the screen

**Save** and **close** `Hud.py` and then run the game with `MainController.py` to test for any errors.

## Adding scores to collisions

Our objective identify three collisions we want to add scoring to:

1. Laser &rarr; Asteroid
2. Laser &rarr; Astronaut
3. Astronaut &rarr; Ship

We already have event handlers for all three of these collisions, so we just need to adjust them.

Lets start with the Laser ones.

### `Objects/Laser.py`

**Open** `Objects/Laser.py` and add the highlighted text to the `handle_collision` method.

```{code-block} python
:linenos:
:emphasize-lines: 8,11
:lineno-start: 39
    # --- Event handlers
    def handle_collision(self, other, other_type):
        """
        Handles laser collisions with other registered objects
        """
        if other_type == "Asteroid":
            self.room.delete_object(other)
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.delete_object(other)
            self.room.score.update_score(-10)
```

Unpacking these lines:

- **line 46**: responds to the Asteroid collision event (ie. laser shoots an asteroid) by increasing the score by `5`
- **line 49**: responds to the Astronaut collision event (ie. laser shoots an astronaut) by decreasing the score by `10`

**Save** and **close** `Objects/Laser.py`

Onto the Astronaut & Ship collisions

### `Objects/Astronaut.py`

**Open** `Objects/Astronaut.py` and add the highlighted code to the `handle_collision` method:

```{code-block} python
:linenos:
:emphasize-lines: 9
:lineno-start: 31
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Astronaut objects
        """
        # ship collision
        if other_type == "Ship":
            self.room.delete_object(self)
            self.room.score.update_score(50)
```

**Line 39** work exactly the same as the last two calls to `update_score`, but this time it add `50` to the score.

**Save** and **close** `Objects/Astronaut.py`.

## Testing

Time to test our code. We just made three changes to the code so we want to check for the success of all three changes. To do this we will use a **testing table** consisting of four columns:

- **Test**: Lists what you are testing
- **Expected results**: State what you expect the result to be
- **Actual results**: Record what the actual result was when you tested
- **Remedy**: If the actual results differ from the expected results, record has you fixed the problem.

Below is our testing table with the first two columns completed. Copy it down and finish it off.

| Test | Expected results | Actual results | Remedy |
| --- | --- | --- | --- |
| Laser shoots asteroid | score + 5 | | |
| Laser shoots astronaut | score - 10 | | |
| Ship collects astronaut | score + 50 | | |

## Commit and Push

We have finished and tested another section of code so we should make a Git commit.

To do this:

1. In GitHub Desktop go to the bottom left-hand box and write into the summary **Added scoring**.
2. Click on **Commit to main**
3. Click on **Push origin**

Now the work from this lesson is committed and synced with the online repo.

## Completed File States

Below are all the files we used in this lesson in their finished state. **Use this to check if your code is correct**.

### `Objects/Hud.py`

```{code-block} python
:linenos:
from GameFrame import TextObject, Globals

class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        
    def update_score(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()
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
from Objects.Hud import Score
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
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.delete_object(other)
            self.room.score.update_score(-10)
```

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
            self.room.score.update_score(50)
            
    def outside_of_room(self):
        """
        removes astronauts that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
```