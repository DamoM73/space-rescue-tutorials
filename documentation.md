# GameFrame - API

By Steven Tucker

## Overview

GameFrame has been developed to take the excellent PyGame libraries and make them more accessible and easy to use for beginner to intermediate programmers. GameFrame aims to help with learning the concepts of text based game programming without getting caught up in the implementation details.

GameFrame is set up as an event driven framework. Programmers define `Rooms` and `Room Objects`, then write functions to handle certain events such as collisions, button clicks and so on. Just define all the items of your game, then let it run. GameFrame handles the Game loop and collision detection, just register your object for an event and write the code that will run when that event occurs.

GameFrame was primarily written for education, however it can be used to make a variety of games that can be can be freely shared, altered and improved. It's free and available for everyone to use, students, hobbyist and accomplished programmers alike.

## GameFrame folder structure

GameFrame organises files so that the same types of files are together. This organization makes it easier to setup and maintain a game. By keeping files of the same type together, it makes it easy to locate particular files and to create a 'birds eye view' of the project.

The following is a description of the files and folders found in the GameFrame project folder.

### GameFrame

This folder holds most of the code provided by GameFrame. When making a game, the only file in this folder that you need to edit is the `Globals.py` file.

### Images

This folder holds all game images such as backgrounds and game characters. All graphic files that are in your game go here.

### Objects

This is where you put all the individual parts (objects) of your game. For instance, you could make a player that has an image (from the Images folder) and moves across the screen if the arrow buttons are pressed. The player would be one object in the game. An enemy, wall, bouncing ball etc. could be other objects.

### Rooms

Rooms are stages or levels in the game. In the Rooms folder you put each level/stage/room of your game. For instance, the first room might be a maze, and when the player reaches the end of the maze they move into the next room which is a platform game.

### Sounds

This folder holds all game sounds such as gunfire and explosions. All sound files that are in your game go here.

### License

The License file is not a part of the game. It lays out the rules around using and distributing GameFrame. The License is the Gnu General Public License, which basically means you can use it however you like, but you can't stop anyone else from using it, and if you make changes to GameFrame itself (the files inside the GameFrame folder) and want to share it with other people, you can do that as well (It's not stealing. You are allowed to do that!)

### `MainController.py`

This is the file that is run to start the game. We don't need to edit this file, but when we want to run the game, this is the file that is run.

### `README.md`

This file contains a brief description of GameFrame. We do not need to edit this file. It is used to provide a description on GitHub for people who want to know what the project is about. You can delete this file if you like, but leaving it doesn't cause any problems.

### `__init__.py`

Inside folders there is a file called `__init__.py` It is this file that allows us to group files into different folders and still have the game know where to find everything. Whenever we add a file to a folder, we need to add an entry to the `__init__.py` file in the same folder to let the rest of the program know that the new file is there.

You will need to include code in this format

```python
from Folder.FileName import ClassName
```

## `GameFrame/Globals.py`

The `Globals.py` file holds the overall game information and variables that can be accessed from any code file. As well as editing the `Globals.py` file to set game information, you may need to access or update information in the file from other parts of the program.

To do this you need to import the file as follows:

``` python
from GameFrame import Globals
```

### `Globals.py` Variables

#### `running`

This variable indicates that the game is in play.

Set this variable to False to end the game.

``` python
Globals.running = False
```

#### `FRAMES_PER_SECOND `

This variable sets how often the screen is redrawn. It is set by default to 30 times every second. If this rate is increased (or decreased), all movement must be adjusted accordingly. If an object moves 5 pixels every frame, then it will travel further in a second at 40 Frames per second (200 pixels), than it will at 30 (150 pixels).

#### `SCREEN_WIDTH`

The width of the game screen. By default this is set to 800

#### `SCREEN_HEIGHT`

The height of the game screen. By default this is set to 600

#### `SCORE`

This variable is provided to track a players score and is initially set to 0.

#### `LIVES`

This variable is provided to track a players lives and is initially set to 3.

#### `window_name`

The text that is stored in this variable will be displayed on the game window.

#### `levels`

This is an array that hold the names of all the levels in the game, in the order that a player progresses through them. The names in this array, must match with files that are in the `Rooms` folder.

An example could be

``` python
Levels = ['StartScreen', 'MazeLevel', 'PlatformLevel', 'EndScreen']
```

#### `start_level`

The level index from the levels array, that will be launched when the game starts, this is usually 0 (the first item)

#### `end_game_level`

The level index from the levels array, that will be run when the game ends (usually an end screen or high score screen)

## `GameFrame/DataBaseController.py`

The `DataBaseController` is a class which connects the provided SQL database file.

If you wish to use a database in your game you will need to use this Class and write methods for the class in this file.

## Rooms/Levels

In a game made with GameFrame, a room is the area in which a game is played. To have a game, there must be at least one room, but there can be many rooms, with the game progressing through different rooms.

A room is defined and kept in the `Rooms` folder, and it is a type of GameFrame `Level`. As a room is a type of Level, every room has the attributes and methods of a Level, plus any defined for that room.

To access the `Level` code, you need to import the file as follows:

``` python
from GameFrame import Level
```

### Defining and Initialising a Room/Level:

``` python
class LevelName(Level): 
    def __init__(self, screen, joysticks): 
        Level.__init__(self, screen, joysticks)
```

### Rooms/Levels Variables

#### `screen`

Passed to the Room/Level when started, the screen variable is a hook to the display area of the room.

#### `running`

Level is active when True, level stops running due to being successfully complete when set to False

#### `quitting`

Level stops running and has not been successfully completed.

### Rooms/Levels Methods

#### `set_background_image(image_file)`

This function is called to set the background image of the level, where image_file is replaced by the name of an image in the Images folder.

Example:

``` python
self.set_background_image('background.jpg')
```

#### `set_background_scroll(speed)`

GameFrame provides this simple function call to set a scrolling background, such as those used for scrolling shooter games like 1942. The variable speed is the number of pixels moved every frame (Frames are set by default to 30 per second)

Example:

``` python
self.set_background_scroll(5)
```

#### `add_room_object(room_object)

Add a RoomObject to the level.

Example:

``` python
self.add_room_object(player)
```

#### `load_sound(sound_file)`

Read a sound file from the Sounds folder. Once read into a variable it can be played anytime by calling play() on the variable

Example:

``` python
self.explosion_sound = self.load_sound('explosion.wav') 

self.explosion_sound.play()
```

##### PyGame sound methods

The variable is storing a PyGame sound object, which means that you can use any PyGame mixer method.

For example:

- `.play(loop=1)` will loop the sound
- `.play(fade_ms=500)` will fade the sound in over half a 500ms
- `.stop()` will stop the sound
- `.fadeout(500)` will fade the sound out over 500ms
- `.set_volume(0.5)` will set the volume to half (range `0.0` to `1.0`)

Other methods can be found on the [PyGame mixer docs](https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.play)

#### `delete_object(obj_name)`

Removes an object from the room.

Example:

``` python
self.room.delete_object('enemy_plane_1')
```

#### `set_timer(ticks, function_call)`

When you want to set a timed event, you call the set_timer function providing the number of ticks (frames ticked over) and a function to call when the number of ticks is reached.

For example, if I wanted to generate a new enemy character every 10 seconds, and the Frames per second is at the default setting of 30, I could write the call

``` python
set_timer(300, create_new_enemy)
```

Within the function `create_new_enemy`, I could have that same line to repeatedly call itself every 10 seconds

#### `count_object(obj_name)`

Counts the number of instances  of the provided object within the room. The `obj_name` is a string giving the name of the object.

For example, if I wanted to know how many enemy planes are win the room, I could write the call:

``` python
self.room.count_object('enemy_plane')
```

## RoomObject

Everything that placed inside a Room, must be a `GameFrame` `RoomObject` (A `TextObject` is also a type of `RoomObject`). You define room objects in the “Objects” folder, and each object is a type of `GameFrame` `RoomObject`.

As each file in the Objects folder is a type of `RoomObject`, each has the attributes and methods of a `RoomObject`, plus any defined for that file.

To access the `RoomObject'` code, you need to import the file as follows:

``` python
from GameFrame import RoomObject
```

### Defining and Initialising a Room Object

``` python
class Name_of_Object(RoomObject): 
    def __init__(self, room, x, y): 
        RoomObject.__init__(self, room, x, y)
```

### RoomObject Variables

#### `room`

The room that the object is in.

#### `depth`

The layer the object is situated in. When two objects occupy the same space, the object with the higher depth value will be shown, the object with the lower depth value will be covered.

#### `x`

The current horizontal position of the object, taken at the top left hand corner of the image

#### `y`

The current vertical position of the object, taken at the top left hand corner of the image

#### `rect`

The bounding rectangle. That is, a rectangle that encompasses the image. Used for collision detection.

#### `prev_x`

The previous horizontal position of the object, taken at the top left hand corner of the image

#### `prev_y`

The previous vertical position of the object, taken at the top left hand corner of the image

#### `width`

The width in pixels, of the object image

#### `height`

The height in pixels, of the object image

#### `image`

The current image of the object

#### `x_speed`

The number of pixels the object is moving in the horizontal direction every frame. Positive numbers indicate a move to the right, negative numbers indicate a move to the left. Default value is `0`.

#### `y_speed`

The number of pixels the object is moving in the vertical direction every frame. Positive numbers indicate a move down, negative numbers indicate a move up. Default value is `0`.

#### `gravity`

The gravity is a number that is used to determine the amount of gravity exerted on an object. The higher the number, the greater effect of falling the object has.

#### `handle_key_events`

Set to `False` by default, this variable determines whether an object is notified of keyboard presses. To listen for key events, set this variable to `True`

#### `handle_mouse_events`

Set to `False` by default, this variable determines whether an object is notified of mouse presses and movement. To listen for mouse events, set this variable to `True`

### RoomObject Methods

#### `load_image(file_name)`

Retrieve and image from file.

#### `set_image(image, width, height)`

Set the objects image by providing the image itself as well as its width and height in pixels.

#### `delete_object(obj)`

Remove an object from the room.

Example:

``` python
self.room.delete_object('enemy_plane_1')
```

#### `register_collision_object(collision_object)`

For an object to be notified of collisions with other objects, it must register to listen for collisions with a given object type. You can register for multiple object types.

Example:

``` python
self.register_collision_object('enemy') 
```

#### `handle_collision(self, other, other_type)`

When a collision is registered, the object will be notified of any such event by calling its `handle_collision` function.  

To write the code that needs to run in a collision event, the object needs to implement the function.

Example:

``` python
def handle_collision(self,other,other_type): 
    self.bounce(other) 
```

#### `key_pressed(self, key)`

If the variable `handle_key_events` is set to `True`, the object will be notified of any key presses by calling its `key_pressed` function. To write the code that needs to run in a key press event, the object needs to implement the function. The key identity will be supplied as the variable `key`.  [PyGame key identities can be found here.](http://www.pygame.org/docs/ref/key.html)

Example:

``` python
def key_pressed(self, key): 
    if key[pygame.K_LEFT]:
        self.x -= 4 
    elif key[pygame.K_RIGHT]: 
        self.x += 4 
    elif key[pygame.K_UP]: 
        self.y -= 4 
    elif key[pygame.K_DOWN]: 
        self.y += 4 
```

#### `clicked(self, button_number)`

If the variable `handle_mouse_events` is set to `True`, the object will be notified of any mouse key presses by calling its clicked function. To write the code that needs to run in a mouse key press event, the object needs to implement the function. The mouse button identity will be supplied as the variable `button_number`

Example:

``` python
def clicked(self, button_number): 
    # - Check for a left mouse button click - # 
    if button_number == 1: 
        self.delete_object(self) 
```

#### `mouse_event(self,mouse_x,mouse_y,button_left,button_middle,button_right)`

If the variable `handle_mouse_events` is set to `True`, the object will be notified of any mouse event by calling its mouse_event function. To write the code that needs to run in a mouse event, the object needs to implement the function. The mouse `x` and `y` position will be supplied as well as the buttons information

Example:

``` python
def mouse_event(self, mouse_x, mouse_y, button_left, button_middle, button_right): 
    self.x = mouse_x 
    self.y = mouse_y
```

#### `bounce(other)`

A convenience function that makes the current object bounce off of another object. The other object is provided as the variable `other`

#### `blocked(other)`

A convenience function that makes the current object blocked by another object. The other object is provided as the variable `other`

#### `prestep()`

Use this method to run code for the object each tick of the game clock, but before the code in the `step()` method.

#### `step()`

Use this method to run code for the object on each tick of the game clock.

#### `set_dircetion(angle,speed)`

Sets the direction and speed of the object. `angle` is in degrees where:

- 0&deg; - right &rarr;
- 90&deg; - up &uarr;
- 180&deg; - left &larr;
- 270&deg; - down &darr;

#### `get_direction_coordinates(angle, speed)`

Calculates the next tick coordinates for a object travelling at `angle` and `speed`. Returns coordinates as a tuple `(x,y)`

#### `rotate(angle)`

Rotates the object so that it's direction is pointed towards `angle`.

#### `rotate_to_coordinate(x, y)`

Rotates the object so that it's direction is pointed at the coordinates of `x` and `y`.

## Text Object

The `TextObject` is a type of `RoomObject`. It has all the same attributes of a `RoomObject`, but specialises in displaying text. The text can be set to various sizes and colours as well as specifying a given font type. To access the `TextObject`' code, you need to import the file as follows:

``` python
from GameFrame import TextObject
```

### Defining and Initialising a Text Object

``` python
class NameofTextObject(TextObject): 
    def __init__(self, room, x, y, 
                 text='Not Set', 
                 size=60,
                 font='Comic Sans MS', 
                 colour=(0, 0, 0), 
                 bold=False): 
        RoomObject.__init__(self, room, x, y) 
```

### Text Object Variables

#### `text`

The text that will be used for the `TextObject` when the function `update_text()` is called.

#### `size`

The font size of the text when rendered

#### `font`

The font type for the text when rendered. ie. 'Sans Serif', 'Comic Sans MS'

#### `colour`

The colour of the text when rendered

#### `bold`

Set to `False` by default, this will set the text to bold if `True`.

### Text Object Methods

#### `update_text()`

This function must be called for any changes to the object variable to take effect.