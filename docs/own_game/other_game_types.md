# Other Game Types

!!! learn "On this page we will learn"
    - how GameFrame can make platform, top-down and scrolling games
    - how gravity and collisions make a player land on platforms
    - how to build a level from a list of strings
    - how to scroll the background to make the player feel like they're moving

!!! terms "Terminology"
    - **platform game** – a game where the player runs and jumps between platforms while gravity pulls them down.
    - **gravity** – a force in a game that pulls objects down, making them fall faster and faster.
    - **top-down game** – a game where we look down on the player from above as they move up, down, left and right.
    - **four-way movement** – movement where the player can only go up, down, left or right, and not diagonally.
    - **scrolling game** – a game where the background moves past the player to make it feel like they are travelling.

Space Rescue is a side-on shooter, but GameFrame can make lots of other kinds of games. This page has three small demo games to show how. Each one is a starting point for your own game, not a finished game.

## Setting up a demo

Each demo is in the [tutorial files](../index.md#tutorial-files), in the ***own_game*** folder. The demos use images from the Space Rescue resources, so the easiest way to try one is:

1. Make a copy of your Space Rescue folder, or clone the [Space Rescue Resources repo](https://github.com/DamoM73/space-rescue-resources) again into a new folder.
2. In the copy, delete the files in ***Objects*** and ***Rooms***, except ***\_\_init\_\_.py*** and ***notes.md***.
3. Copy the demo's ***Objects***, ***Rooms*** and ***GameFrame*** folders into the copy, and replace the files.
4. Run ***MainController.py***.

Each demo's ***Globals.py*** sets the window to 1280 × 800 and lists just one Room in `levels`, and each ***\_\_init\_\_.py*** imports the demo's classes.

All three demos use a `Block` class for walls and floors. It uses the repair kit image as a crate:

```python linenums="1" title="Objects/Block.py"
--8<-- "examples/own_game/platformer/step01/Objects/Block.py"
```

??? note "Code explanation"
    - **line 1** → imports the `RoomObject` class.
    - **line 3** → defines the `Block` class as a subclass of `RoomObject`.
    - **lines 4–6** → a docstring that explains what the class is for.
    - **lines 7–8** → define `__init__` and run `RoomObject`'s `__init__` method.
    - **lines 11–12** → give the block the crate image at 42 × 42 pixels. A Block has no other code: it just sits there for other objects to bump into.

---

## Platform game

In a **platform game**, the player runs and jumps between platforms, and gravity pulls them down. Think Super Mario Bros.

The key ideas are:

- **gravity**: every RoomObject has a `gravity` variable. GameFrame adds it to `y_speed` every frame, so the player falls faster and faster
- **landing**: when the player hits the top of a block, we put them on top of it and stop them falling
- **jumping**: the player can only jump when they're standing on something

### The player

```python linenums="1" title="Objects/Jumper.py"
--8<-- "examples/own_game/platformer/step01/Objects/Jumper.py"
```

??? note "Code explanation"
    - **lines 1–2** → import `RoomObject` and Pygame.
    - **line 4** → defines the `Jumper` class as a subclass of `RoomObject`.
    - **lines 5–7** → a docstring that explains what the class is for.
    - **lines 8–9** → define `__init__` and run `RoomObject`'s `__init__` method.
    - **lines 12–13** → give the Jumper the astronaut image.
    - **line 16** → sets `gravity` to `1`, so `y_speed` grows by 1 every frame and the Jumper falls faster and faster.
    - **line 17** → creates the `on_ground` flag. The Jumper starts in the air.
    - **line 20** → registers for key events.
    - **line 21** → registers collisions with `Block` objects.
    - **line 23** → defines the `key_pressed` event handler.
    - **lines 24–26** → a docstring that explains what the method does.
    - **lines 27–28** → move left while ++a++ is held.
    - **lines 29–30** → move right while ++d++ is held.
    - **lines 31–32** → stop moving sideways when neither key is held.
    - **line 34** → checks if ++w++ is pressed **and** the Jumper is on the ground…
    - **line 35** → …and jumps by giving it a big upwards speed. Gravity slows it down, stops it, then pulls it back down.
    - **line 37** → defines the `step` method.
    - **lines 38–40** → a docstring that explains what the method does.
    - **lines 41–42** → limit the falling speed to 20, so the Jumper can't fall so fast it skips straight through a 42-pixel block.
    - **line 43** → assumes the Jumper is in the air. If it's standing on a block, the collision below sets `on_ground` back to `True` before the next frame.
    - **line 45** → defines `handle_collision`.
    - **lines 46–48** → a docstring that explains what the method does.
    - **line 49** → checks if the Jumper hit a Block.
    - **line 50** → checks if the bottom of the Jumper was above the top of the block in the **last** frame (`prev_y`), which means it has just landed on it…
    - **lines 52–54** → …so it puts the Jumper on top of the block, stops it falling and sets `on_ground` to `True`.
    - **line 55** → otherwise, checks if the top of the Jumper was below the block last frame, which means it jumped into the block from underneath…
    - **lines 57–58** → …so it moves the Jumper below the block and stops it rising.
    - **line 59** → otherwise, it must have hit the side of the block…
    - **lines 61–62** → …so it moves the Jumper back to where it was and stops it moving sideways.

### The Room

```python linenums="1" title="Rooms/Platformer.py"
--8<-- "examples/own_game/platformer/step01/Rooms/Platformer.py"
```

??? note "Code explanation"
    - **lines 1–3** → import `Level`, `Block` and `Jumper`.
    - **line 5** → defines the `Platformer` class as a subclass of `Level`.
    - **lines 6–8** → a docstring that explains what the class is for.
    - **lines 9–10** → define `__init__` and run `Level`'s `__init__` method.
    - **line 13** → sets the background image.
    - **lines 16–17** → use a `for` loop to place a row of blocks every 42 pixels along the bottom of the screen, to make a floor.
    - **lines 20–21** → make a floating platform of five blocks.
    - **lines 22–23** → make a higher platform.
    - **line 26** → adds the Jumper above the floor. Gravity drops it onto the floor.

!!! primm "PRIMM"
    1. **Predict** what will happen if you change `gravity` to `2`.
    2. **Run** the demo and try it.
    3. **Modify**: add more platforms, and an object to collect at the top.

---

## Top-down game

In a **top-down game**, we look down on the player, who moves up, down, left and right. Think of the original Legend of Zelda or Pac-Man.

The key ideas are:

- **four-way movement**: the player only moves while a key is held, like the "in motion while a key is pressed" option in [Lesson 4](../lessons/04_advanced_movement.md)
- **walls**: GameFrame's `blocked` method moves an object back to where it was in the last frame, so it can't move into a wall
- **a level from a list**: instead of placing every wall by hand, we draw the maze as a list of strings and turn each character into an object

### The player

```python linenums="1" title="Objects/Explorer.py"
--8<-- "examples/own_game/top_down/step01/Objects/Explorer.py"
```

??? note "Code explanation"
    - **lines 1–2** → import `RoomObject` and Pygame.
    - **line 4** → defines the `Explorer` class as a subclass of `RoomObject`.
    - **lines 5–7** → a docstring that explains what the class is for.
    - **lines 8–9** → define `__init__` and run `RoomObject`'s `__init__` method.
    - **lines 12–13** → give the Explorer the astronaut image at 36 × 36 pixels, so it fits through the 42-pixel corridors.
    - **line 16** → registers for key events.
    - **lines 17–18** → register collisions with walls (`Block`) and the `Exit`.
    - **line 20** → defines the `key_pressed` event handler.
    - **lines 21–23** → a docstring that explains what the method does.
    - **lines 24–25** → stop the Explorer at the start of every frame, so it only moves while a key is held.
    - **lines 26–33** → move left, right, up or down depending on which arrow key is held. Using `elif` means only one direction at a time, so no diagonal moves.
    - **line 35** → defines `handle_collision`.
    - **lines 36–38** → a docstring that explains what the method does.
    - **line 39** → if the Explorer hit a wall…
    - **line 40** → …`blocked` moves it back to where it was last frame and stops it.
    - **line 41** → if the Explorer reached the exit…
    - **line 42** → …ends the Room.

The `Exit` class is just like `Block`, with the shield image.

### The Room

```python linenums="1" title="Rooms/Maze.py"
--8<-- "examples/own_game/top_down/step01/Rooms/Maze.py"
```

??? note "Code explanation"
    - **lines 1–4** → import `Level`, `Block`, `Explorer` and `Exit`.
    - **line 6** → defines the `Maze` class as a subclass of `Level`.
    - **lines 7–9** → a docstring that explains what the class is for.
    - **lines 10–11** → define `__init__` and run `Level`'s `__init__` method.
    - **line 14** → sets the background image.
    - **lines 17–37** → draw the maze as a list of 19 strings, each 30 characters long. Each character is a 42 × 42 square on the screen: `#` is a wall, `.` is empty, `P` is where the player starts and `E` is the exit.
    - **line 40** → loops through each string, with `enumerate` giving its row number…
    - **line 41** → …and loops through each character in the string, with its column number.
    - **lines 42–43** → work out the square's position on the screen from its column and row.
    - **lines 44–45** → if the character is `#`, add a wall.
    - **lines 46–47** → if it's `E`, add the exit.
    - **lines 48–49** → if it's `P`, add the Explorer, moved 3 pixels in so it sits in the middle of its square.

!!! primm "PRIMM"
    1. **Predict** what will happen if you change one of the `.` characters to `#`.
    2. **Run** the demo and find your way out of the maze.
    3. **Modify**: design your own maze. Keep every string the same length.

---

## Scrolling game

In a **scrolling game**, the background moves past the player to make it feel like they're travelling. Think of classic shooters like 1942 or Galaga.

The key ideas are:

- **a scrolling background**: GameFrame's `set_background_scroll` moves the background down the screen every frame, and wraps it around so it never runs out
- **objects coming towards the player**: rocks fall from the top of the screen, while the player moves left and right to dodge them
- **rotating an image**: our ship image faces right, so we turn it to face up

### The player

```python linenums="1" title="Objects/Fighter.py"
--8<-- "examples/own_game/scrolling/step01/Objects/Fighter.py"
```

??? note "Code explanation"
    - **lines 1–2** → import `RoomObject`, `Globals` and Pygame.
    - **line 4** → defines the `Fighter` class as a subclass of `RoomObject`.
    - **lines 5–7** → a docstring that explains what the class is for.
    - **lines 8–9** → define `__init__` and run `RoomObject`'s `__init__` method.
    - **lines 12–13** → give the Fighter the ship image at 80 × 80 pixels.
    - **line 14** → rotates the image 90° anticlockwise, so the ship points up the screen.
    - **line 17** → registers for key events.
    - **line 18** → registers collisions with `Rock` objects.
    - **line 20** → defines the `key_pressed` event handler.
    - **lines 21–23** → a docstring that explains what the method does.
    - **line 24** → if ++a++ is held **and** the ship isn't at the left edge…
    - **line 25** → …moves left.
    - **line 26** → if ++d++ is held **and** the ship isn't at the right edge…
    - **line 27** → …moves right.
    - **lines 28–29** → otherwise, stop. Checking the edges here means we don't need a `keep_in_room` method.
    - **line 31** → defines `handle_collision`.
    - **lines 32–34** → a docstring that explains what the method does.
    - **lines 35–36** → end the Room when a rock hits the ship. The demo only has one Room, so it starts again.

### The falling rocks

```python linenums="1" title="Objects/Rock.py"
--8<-- "examples/own_game/scrolling/step01/Objects/Rock.py"
```

??? note "Code explanation"
    - **line 1** → imports `RoomObject` and `Globals`.
    - **line 3** → defines the `Rock` class as a subclass of `RoomObject`.
    - **lines 4–6** → a docstring that explains what the class is for.
    - **lines 7–8** → define `__init__` and run `RoomObject`'s `__init__` method.
    - **lines 11–12** → give the rock the asteroid image.
    - **line 15** → starts the rock moving at `90°`, which in GameFrame is straight **down**.
    - **line 17** → defines the `step` method.
    - **lines 18–20** → a docstring that explains what the method does.
    - **lines 21–22** → delete the rock once it has gone past the bottom of the screen.

### The Room

```python linenums="1" title="Rooms/Scroller.py"
--8<-- "examples/own_game/scrolling/step01/Rooms/Scroller.py"
```

??? note "Code explanation"
    - **lines 1–4** → import `Level`, `Globals`, `Fighter`, `Rock` and `random`.
    - **line 6** → defines the `Scroller` class as a subclass of `Level`.
    - **lines 7–9** → a docstring that explains what the class is for.
    - **lines 10–11** → define `__init__` and run `Level`'s `__init__` method.
    - **line 14** → sets the background image.
    - **line 15** → scrolls the background down 4 pixels every frame.
    - **line 18** → adds the Fighter near the bottom of the screen.
    - **line 21** → starts a timer that drops the first rock after one second. Rooms have a `set_timer` method too.
    - **line 23** → defines the `drop_rock` method.
    - **lines 24–26** → a docstring that explains what the method does.
    - **line 27** → chooses a random `x` position across the screen.
    - **line 28** → adds a rock just above the top of the screen, so it slides into view.
    - **line 29** → starts the timer again with a random time, so rocks keep falling.

!!! primm "PRIMM"
    1. **Predict** what will happen if you change the scroll speed on line 15 to `10`.
    2. **Run** the demo and try it.
    3. **Modify**: add a score that goes up the longer the player survives.

!!! tip "Mix and match"
    These ideas combine. A platform game could scroll, and a top-down game could have enemies that move by themselves like Zork. Start from the demo closest to your idea, then add the features you need one at a time.
