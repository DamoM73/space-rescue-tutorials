# Welcome screen

To get the ball rolling, well create a welcome screen for our game. This is a nice easy way to introduce some of the concepts and processes we will be using throughout.

## Planning

### Wireframe

```{admonition} Wireframes
:class: note
A wireframe is like a blueprint or skeleton of a website or app. It's a simple, basic outline that shows where different elements, like buttons, images, and text, will go on the screen. It focuses on the layout and arrangement of elements rather than the colors or details. It's a helpful tool for visualizing and discussing ideas before creating the final design, just like making a rough sketch or draft of a drawing before adding all the details.
```

Below is a wireframe of our welcome screen.

![Welcome screen wireframe](assets/img/welcome_wf.png)

This wireframe shows three different parts of the program wee need to address:

- the game window (blue text):
  - features of the window that will hold our game
  - need to change size and title
- the WelcomeScreen room (orange text):
  - the main part of our window is taken up with the game surface which holds the WelcomeScreen Room
  - it contains a background image and the Title Object
- the Title Object (green text):
  - represented by the placeholder (box with an x)
  - contains an image
  - has a key event to react to space being pressed

### Class diagram

We now know how the screen will look, but let's also consider the Class diagram. Check out [Deepest Dungeon](https://damom73.github.io/python-oop-with-deepest-dungeon/stage_1.html#class-diagram) for a refresher on Class diagrams if you need it.

![welcome screen class diagram](assets/img/welcome_cd.png)

We can see that the **WelcomeScreen** class has two attributes:

- background image
- Title RoomObject

We can also see that the Title class has:

- attribute: image
- method: keypressed

So we can see that there are three tasks we need to complete to create our welcome screen:

1. Adjust the window values
2. Create the WelcomeScreen Room
3. Create the Title RoomObject

Let's start.

## Adjusting window values

The window values reside in `Globals.py` in the `GameFrame` folder, so open it up.

To change the window size, adjust the `SCREEN_WIDTH` and `SCREEN_HEIGHT`:

```{code-block} python
:linenos:
:lineno-start: 7
:emphasize-lines: 1-2
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
```

Then change the `window_name` value:

```{code-block} python
:lineno-start: 15
:emphasize-lines: 2
# - Set the Window display name - #
window_name = 'Space Rescue'
```

Save the `Globals.py` file using `control` + `S` (Windows) `command` + S (macOS)

## Create WelcomeScreen Room

Let's check the [GameFrame documentation](documentation.md#roomslevels) to see how we can create a level.

So we need to create a new file in the `Rooms` folder called `WelcomeScreen.py`.

In this file we are going to create a WelcomeScreen class. This is going to be a sub-class of the Level class provided by GameFrame. So the first thing we need to do is to import the Level class from GameFrame:

```{code-block} python
:linenos:
:emphasize-lines: 1
from GameFrame import Level
```

Now we can create our WelcomeScreen class. Following the instructions from the documentation add the following code.

```{code-block} python
:linenos:
:emphasize-lines: 3-8
from GameFrame import Level

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
```

Lets break that down a bit:

- line 3 &rarr; defines our class and explicitly names it as a subclass of the `Level` class.
- lines 4-6 &rarr; a doc string that explains the class.
- line 7 &rarr; the `__init__` method that is called automatically when a `WelcomeScreen` object is made.
- line 8 &rarr; calling the `__init__` method of the `Level` parent class will mean the `WelcomeScreen` class will inherent all the attributes and methods from `Level`.

Now save the `WelcomeScreen.py` file.

### Testing WelcomeScreen

So we've made a welcome screen, let's run the game and see what happens.

Open `MainController.py` and then click the play button in the top righthand corner.

![play button](assets/img/run.png)

Well, that didn't go to plan. You probably have the following error:

```{code-block}
Traceback (most recent call last):
  File "d:\GIT\space_rescue_pygame\MainController.py", line 34, in <module>
    room = class_name(screen, joysticks)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'module' object is not callable
```

Have a close look at this error. I guarantee this is not the last time you will see it, that's why I purposely caused it. 

Reading the error it is really obscure what the problem. Remember when looking at the file structure I said that if you add a new Room or Object you need to link it to GameFrame using the `__init__.py` file. This is the kind of error that occurs when you forget.

To remedy this error, open the `__init__.py` file in the `Rooms` folder and add the following code:

```{code-block} python
:linenos:
from Rooms.WelcomeScreen import WelcomeScreen
```

Save the `__init__.py` file, and run your program again using the `MainController.py`.

You should now have a screen like this:

![Welcome Screen 1](assets/img/welcome_1.png)

Not very exciting, but it's the correct size, and the window title reads **Space Rescue**, so that's a start.

### Adding the background

Let's make it less boring by adding a background image. Again, check the [GameFrame docs](documentation.md#roomslevels) to see how we can do this.

You will see that there is a method **set_background_image** which takes an image file. So we will have to call this method, but when? Well, we want the background to appear as soon as the room is created, so, it needs to be called in the `__init__` method.

Go back to the `WelcomeScreen.py` file and then add the highlighted code to the `__init__` method.

```{code-block} python
:linenos:
:emphasize-lines: 10-11
from GameFrame import Level

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
```

Breaking that down:

- line 10 &rarr; structural comment to explain what is happening. This is a really good habit to develop.
- line 11:
  - `self` &rarr; remember in OOP the need to refer all actions to the current instance of the object (self)
  - `set_background_iamge` &rarr; a method inherited from the `Level` parent class.
  - `"Background.png"` an image file in the `images` folder (go to the folder and see if you can find it).

Save `WelcomeScreen.py` and then run the program again using `MainController.py`.
