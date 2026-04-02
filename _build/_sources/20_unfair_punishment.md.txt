# Mechanic - Unfair Punishment

```{topic} In this lesson you will:
- apply learnt knowledge to plan code using using IPO tables
- improve gameplay by incorporating an identified mechanic
- apply learnt knowledge to destroy an object in response to an event
```

In the **[Game Design lesson](18_game_design.md)**, we identified when a game involved unfair punishment, it undermines the players experience of interactivity. We also identified a mechanic that unfairly punished the player:

| Unfair punishment | Solution |
| --- | --- |
| A laser shot at an asteroid can pass through the asteroid and hit an astronaut | Have the asteroid disappear when it collides with the first object |

In this lesson we will remove this unfair punishment.

## Planning

We have already identified a solution for this problem: Have the asteroid disappear when it collides with the first object. Fortunately, we already know the tool to achieve this, since we have used it before. We have used [delete_object()](documentation.md#delete_objectobj) many times throughout our code, so how should we apply it here? To answer that we need to consider two questions:

- What object needs to be deleted?
  - the Laser
- When event trigger the deletion?
  - Either of the two Laser collisions (asteroid or astronaut)

What does that look like in a IPO table?

![laser deletion IPO](assets/img/remove_laser_ipo.png)

We simply need to include the `delete_object()` method in both the asteroid collision event handler and the astronaut collision event handler. Let's get coding.

## Coding

### `Objects\Laser.py`

**Open** `Objects\Laser.py` and add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 52
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
            self.room.asteroid_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.astronaut_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(-10)
        self.room.delete_object(self)
```

Let's unpack that code:

- **line 52**: removes `self` (**this instance of Laser**)
  - we could have placed the `delete_object()` in both the asteroid and astronaut collisions, but since we want to use it on all laser collisions, we can simply place it in the `handle_collision()` method.

**Save** and **close** `Objects\Laser.py`.

## Testing

Now run `MainController.py` to test that the laser disappears when it hits both astronauts and asteroids.

## Commit and Push

We have finished and tested another section of code so we should make a Git commit.

To do this:

1. In GitHub Desktop go to the bottom left-hand box and write into the summary **Added lasers**.
2. Click on **Commit to main**
3. Click on **Push origin**

Now the work from this lesson is committed and synced with the online repo.

## Completed File States

Below are all the files we used in this lesson in their finished state. **Use this to check if your code is correct**.

### `Objects\Laser.py`

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
            self.room.asteroid_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.astronaut_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(-10)
        self.room.delete_object(self)
```
