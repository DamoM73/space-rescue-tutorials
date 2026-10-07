# Common Errors

!!! learn "On this page we will learn"
    - how to read a Python traceback from a GameFrame game
    - what the most common GameFrame errors mean
    - how to fix each one

When something goes wrong, Python stops the game and prints a **traceback** in the terminal. A traceback lists the path Python took to reach the error, with the **most recent step last**. So the most useful lines are usually at the **bottom**:

- the last line says **what** went wrong (the type of error and a message)
- the `File` lines above it say **where**: look for the last one that's in your own ***Objects*** or ***Rooms*** folder, not in ***GameFrame***

The errors below are the ones we're most likely to see. The file paths will be different on your computer.

---

## No module named 'pygame'

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 4, in <module>
    import pygame
ModuleNotFoundError: No module named 'pygame'
```

- **lines 2–3** → the error happened on line 4 of ***MainController.py***, the very first thing the game does.
- **line 4** → Python can't find Pygame.

**Why**: the game is running without our virtual environment, so it can't see the Pygame we installed there.

**Fix**: check the bottom-right of VS Code shows `.venv` (see [Setup](../start/setup.md#virtual-environment)). If it doesn't, press ++ctrl+shift+p++, choose **Python: Select Interpreter** and pick the one with `.venv`. In Thonny, see [Using Thonny](using_thonny.md#check-the-virtual-environment).

---

## 'module' object is not callable

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 34, in <module>
    room = class_name(screen, joysticks)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'module' object is not callable
```

- **lines 2–4** → the error happened when GameFrame tried to create a Room.
- **line 5** → GameFrame found a **module** (a file) instead of a class.

**Why**: we created a new Room but didn't add it to ***Rooms/\_\_init\_\_.py***.

**Fix**: add `from Rooms.RoomName import RoomName` to ***Rooms/\_\_init\_\_.py***. New objects need the same in ***Objects/\_\_init\_\_.py***. We first saw this in [Lesson 1](../lessons/01_welcome.md#testing-welcomescreen).

---

## No file found in working directory

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 35, in <module>
    exit_val = room.run()
  File "C:\GitHub\space-rescue-resources\GameFrame\Level.py", line 72, in run
    self.process_user_events()
  File "C:\GitHub\space-rescue-resources\GameFrame\Level.py", line 250, in process_user_events
    event()
  File "C:\GitHub\space-rescue-resources\Objects\Zork.py", line 50, in spawn_asteroid
    new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
  File "C:\GitHub\space-rescue-resources\Objects\Asteroid.py", line 18, in __init__
    self.set_image(image,50,49)
  File "C:\GitHub\space-rescue-resources\GameFrame\RoomObject.py", line 37, in set_image
    self.image_orig = pygame.image.load(image).convert_alpha()
FileNotFoundError: No file 'Images\asteriod.png' found in working directory 'C:\GitHub\space-rescue-resources'.
```

- **lines 2–7** → the game was running, and a timer called a method.
- **lines 8–9** → Zork's `spawn_asteroid` method created an asteroid.
- **lines 10–11** → this is the last line in **our** code: line 18 of ***Asteroid.py***, where we set the image.
- **lines 12–13** → GameFrame tried to load the image file.
- **line 14** → there's no file called ***asteriod.png*** in the ***Images*** folder.

**Why**: the file name in our code doesn't match the real file. Here it's a typo (`asteriod` instead of `asteroid`).

**Fix**: check the file name in the ***Images*** (or ***Sounds***) folder and copy it exactly, including capital letters. Windows doesn't mind if the capitals are different, but macOS and Linux do, so `"Background.png"` works on one computer and crashes on another.

---

## name 'Globals' is not defined

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 35, in <module>
    exit_val = room.run()
  File "C:\GitHub\space-rescue-resources\GameFrame\Level.py", line 153, in run
    item.step()
  File "C:\GitHub\space-rescue-resources\Objects\Ship.py", line 50, in step
    self.keep_in_room()
  File "C:\GitHub\space-rescue-resources\Objects\Ship.py", line 43, in keep_in_room
    elif self.y + self.height > Globals.SCREEN_HEIGHT:
NameError: name 'Globals' is not defined. Did you mean: 'globals'?
```

- **lines 4–5** → GameFrame was running each object's `step` method.
- **lines 6–9** → the Ship's `step` called `keep_in_room`, and line 43 of ***Ship.py*** used `Globals`.
- **line 10** → Python doesn't know what `Globals` is.

**Why**: we used `Globals` in a file without importing it.

**Fix**: add it to the import at the top of the file: `from GameFrame import RoomObject, Globals`. The same error happens with any class we forget to import, like `Asteroid` in ***Zork.py***.

---

## object has no attribute

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 35, in <module>
    exit_val = room.run()
  File "C:\GitHub\space-rescue-resources\GameFrame\Level.py", line 157, in run
    item.check_collisions()
  File "C:\GitHub\space-rescue-resources\GameFrame\RoomObject.py", line 72, in check_collisions
    self.handle_collision(item, item_type)
  File "C:\GitHub\space-rescue-resources\Objects\Laser.py", line 47, in handle_collision
    self.score.update_score(5)
AttributeError: 'Laser' object has no attribute 'score'
```

- **lines 4–7** → GameFrame found a collision and called `handle_collision`.
- **lines 8–9** → line 47 of ***Laser.py*** tried to use `self.score`.
- **line 10** → the Laser doesn't have a `score` attribute.

**Why**: the Score belongs to the **Room**, not the Laser. We wrote `self.score` instead of `self.room.score`.

**Fix**: use `self.room.` to reach anything that belongs to the Room: the score, the lives, and the sounds. If the message names the **Room** (for example `'GamePlay' object has no attribute 'lives'`), check that the Room creates that attribute with `self.lives = …`.

---

## 'NoneType' object is not callable

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 35, in <module>
    exit_val = room.run()
  File "C:\GitHub\space-rescue-resources\GameFrame\Level.py", line 72, in run
    self.process_user_events()
  File "C:\GitHub\space-rescue-resources\GameFrame\Level.py", line 250, in process_user_events
    event()
TypeError: 'NoneType' object is not callable
```

- **lines 4–7** → GameFrame was running a timer's method.
- **line 8** → the timer was given `None` instead of a method.

**Why**: we put brackets after the method name in `set_timer`, for example `self.set_timer(10, self.reset_shot())`. The brackets **run** the method straight away, and the timer gets what it returns (`None`).

**Fix**: leave the brackets off: `self.set_timer(10, self.reset_shot)`. See [Passing a method as an argument](../lessons/07_asteroids.md#start-the-timer). The traceback doesn't show our file here, so search our code for `set_timer(` and check each one.

---

## unindent does not match any outer indentation level

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\GitHub\space-rescue-resources\MainController.py", line 32, in <module>
    mod = __import__(mod_name)
  File "C:\GitHub\space-rescue-resources\Rooms\__init__.py", line 1, in <module>
    from Rooms.WelcomeScreen import WelcomeScreen
  File "C:\GitHub\space-rescue-resources\Rooms\WelcomeScreen.py", line 2, in <module>
    from Objects.Title import Title
  File "C:\GitHub\space-rescue-resources\Objects\__init__.py", line 3, in <module>
    from Objects.Zork import Zork
  File "C:\GitHub\space-rescue-resources\Objects\Zork.py", line 43
    self.keep_in_room()
IndentationError: unindent does not match any outer indentation level
```

- **lines 2–9** → the game was still loading its files when the error happened.
- **lines 10–11** → the problem is line 43 of ***Zork.py***.
- **line 12** → that line's indentation doesn't line up with the lines around it.

**Why**: the line has the wrong number of spaces (here 7 instead of 8). This often happens when pasting code.

**Fix**: line the code up with the lines above it. Inside a method, the code should be indented 8 spaces (two levels). VS Code shows faint vertical guide lines to help.

---

## Nothing happens, but there's no error

Some mistakes don't cause an error. The game runs, but something doesn't work. Check these:

- **Collision does nothing**: the class name in `register_collision_object("Ship")` and `other_type == "Ship"` must match the class name exactly, capital letters and all.
- **Key press does nothing**: check `self.handle_key_events = True` is in `__init__`, and the method is spelt `key_pressed`.
- **`step` or `handle_collision` never runs**: check the method name is spelt exactly right. A misspelt method is just a new method that GameFrame never calls.
- **Object doesn't appear**: check it's added to the Room with `add_room_object`, and that its `x` and `y` are on the screen.

!!! tip "Use print to investigate"
    Like we did in [Lesson 8](../lessons/08_moving_asteroids.md#coding_2), add a `print` inside the method you think isn't running. If nothing appears in the terminal, the method isn't being called.
