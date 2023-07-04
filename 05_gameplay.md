# GamePlay Room

In this lesson we are going to create the central room for our game. All the game play will occur in this room, so it is aptly names GamePlay. 

We will:

- Create a new Room called GamePlay
- Indicate that this is the next room after the WelcomeScreen
- Make the game switch from WelcomeScreen to GamePlay when the player presses space.

Before starting we need to understand event-driven programming.

## Event-driven Programming

Event-driven programming is an approach where a program waits for specific events to occur and then performs designated actions in response to those events. Instead of following a predetermined sequence, the program listens for events, such as a button press or a message arriving, and executes specific code based on those events. It allows programs to be more interactive and responsive by dynamically responding to user actions or external inputs, enhancing the overall user experience.

We will be creating an event driven program, which makes sense for a computer game. You want the game to respond when the user does something, or when characters bump into each other.

To create an event-driven program you need to typically follow these steps:

1. Identify the **Events** that will trigger actions.
2. Define **Event Handlers**: the code that will be executed when an event is triggered.
3. **Register** Event Handlers: associate the event handlers with their corresponding events.
4. Start **Event Loop**: Begin the event loop or **event listener**, which continuously waits for events to occur.
5. **Execute** Event Handlers: When an event occurs, the event loop triggers the associated event handler.
6. **Repeat**: The event loop continues running, waiting for more events. This cycle repeats until the program is exited or a specific condition is met.

GameFrame handles many of the tasks above, but its important to understand the terminology before we continue.

## Create GamePlay Room

To create the GamePlay Room we follow the same steps as we did for the WelcomeScreen Room.

1. Create a new file in the `Rooms` folder
2. Import the Levels class from GameFrame
3. Create the GamePlay class
4. Initialise the GamePlay class calling the parent class `__init__` and then add a backdrop
5. Add the new file to the `__init__.py` in the `Rooms` folder

Create a new file in the `Rooms` folder called `GamePlay.py`, then add the following code to it.

```{code-block} python
:linenos:
from GameFrame import Level

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
```

Save the `GamePlay.py` file.

Then open the `__init__.py` file in the `Rooms` folder and add the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 2
from Rooms.WelcomeScreen import WelcomeScreen
from Rooms.GamePlay import GamePlay
```

Save and **close** the `__init__.py` file.

## Make GamePlay the next room after WelcomeScreen

To make this change we need to go back to the `Globals.py` file in the `GameFrame` folder.

Look for the `levels` variable. It contains a list of strings. According to the [GameFrame docs](documentation.md#levels) this holds the names of all the levels in the game, in the order that a player progresses through them.

Currently that list is the default `["WelcomeScreen", "Maze", "ScrollingShooter", "BreakOut"]` with `"WelcomeScreen"` first. This works with our program, but the rest don't. So change the list to the highlighted code below:

```{code-block} python
:linenos:
:lineno-start: 18
# - Set the order of the rooms - #
levels = ["WelcomeScreen", "GamePlay"]
```
