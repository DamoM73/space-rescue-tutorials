# Subgoals

!!! learn "In this lesson we will learn"
    - how subgoals give players short-term and optional challenges
    - how to track a streak and reset it when something goes wrong
    - how to use `count_object` to limit how many objects are in a Room
    - how to write a method that returns a value
    - how to make a mistake cost the player progress

In [Game Design](game_design.md) we planned two **subgoals** for Space Rescue:

| Subgoal | How it works |
| --- | --- |
| Shoot asteroids without taking damage | - count the asteroids shot in a row (the **streak**)<br>- reset the streak when the ship loses a life<br>- limit the number of lasers on the screen by the streak |
| Try not to shoot the astronauts | each astronaut we shoot takes one off our rescued count |

## Planning

### The streak

The **streak** is the number of asteroids shot in a row without losing a life. To make the streak worth chasing, it also controls how many lasers can be on the screen at once:

| Streak | Lasers on screen |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 or more | 5 |

So the rule is: lasers = 1 + streak, but never more than 5.

| Event | Input | Process | Output |
| --- | --- | --- | --- |
| Shoot an asteroid | a laser hits an asteroid | add 1 to the streak, play a sound if the laser limit went up | the HUD shows the new streak and laser limit |
| Lose a life | an asteroid hits the unshielded ship | reset the streak to `0` | the HUD shows a streak of 0 and 1 laser |
| Shoot | the player presses space | count the lasers in the Room; only fire if there are fewer than the limit | a laser fires, or nothing happens |

GameFrame's [`count_object`](../reference/gameframe_api.md#count_objectobj_name) method counts how many objects of a class are in the Room, so `self.room.count_object("Laser")` tells us how many lasers are on the screen.

### Shooting astronauts

Shooting an astronaut already costs 10 points. Now it will also take one off the rescued count, which pushes the player further from the goal. The count can't go below `0`.

---

## Track the streak

Open ***GameFrame/Globals.py***, add the highlighted code below at the bottom and save it.

```python linenums="50" hl_lines="5-6" title="GameFrame/Globals.py"
--8<-- "examples/design/subgoals/step01/GameFrame/Globals.py:50:55"
```

??? note "Code explanation"
    - **line 55** → creates the `streak` counter, starting at `0`.

Now we'll add a `Streak` HUD item that shows the streak and the laser limit. Open ***Objects/Hud.py***, add the highlighted code below at the bottom and save it.

```python linenums="75" hl_lines="3-11 13-17 19-23 25-30" title="Objects/Hud.py"
--8<-- "examples/design/subgoals/step02/Objects/Hud.py:75:104"
```

??? note "Code explanation"
    - **line 77** → defines the `Streak` class as a subclass of `TextObject`.
    - **lines 78–80** → a docstring that explains what the class is for.
    - **line 81** → defines the `__init__` method.
    - **lines 82–84** → a docstring that explains what the method does.
    - **line 85** → runs `TextObject`'s `__init__` method.
    - **lines 88–90** → set the font size, font and colour.
    - **line 91** → draws the text for the first time.
    - **line 93** → defines the `max_lasers` method.
    - **lines 94–96** → a docstring that explains what the method does.
    - **line 97** → **returns** the laser limit: `1 + Globals.streak`, but `min` picks the smaller of that and `5`, so it never goes above 5.
    - **line 99** → defines the `update_streak` method.
    - **lines 100–102** → a docstring that explains what the method does.
    - **line 103** → builds the text with an f-string, calling `max_lasers` to get the laser limit.
    - **line 104** → redraws the text on the screen.

!!! tip "Methods that return a value"
    Most of our methods **do** something, like moving or deleting an object. `max_lasers` **returns** a value instead, so other code can ask for it: `self.room.streak.max_lasers()`. Keeping the rule in one method means the HUD and the Ship always agree about the limit.

Open ***Objects/\_\_init\_\_.py***, change the highlighted code below and save it.

```python linenums="1" hl_lines="7" title="Objects/__init__.py"
--8<-- "examples/design/subgoals/step03/Objects/__init__.py"
```

??? note "Code explanation"
    - **line 7** → imports the `Streak` class as well.

Open ***Rooms/GamePlay.py***, add the highlighted code below and save it.

```python linenums="1" hl_lines="4 26-27 38" title="Rooms/GamePlay.py"
--8<-- "examples/design/subgoals/step04/Rooms/GamePlay.py"
```

??? note "Code explanation"
    - **line 4** → imports the `Streak` class.
    - **line 26** → creates a Streak counter in the bottom-right corner, and stores it in `self.streak` so other objects can use it.
    - **line 27** → adds the counter to the Room.
    - **line 38** → loads the sound for the laser limit going up.

---

## Use the streak

### Limit the lasers

Open ***Objects/Ship.py***, change the highlighted code below in `shoot_laser` and save it.

```python linenums="56" hl_lines="5-6" title="Objects/Ship.py"
--8<-- "examples/design/subgoals/step05/Objects/Ship.py:56:68"
```

??? note "Code explanation"
    - **line 60** → asks the Streak counter for the current laser limit.
    - **line 61** → only fires if the ship can shoot **and** there are fewer lasers in the Room than the limit.

### Build the streak

Open ***Objects/Laser.py***, add the highlighted code below and save it.

```python linenums="39" hl_lines="10-13" title="Objects/Laser.py"
--8<-- "examples/design/subgoals/step06/Objects/Laser.py:39:56"
```

??? note "Code explanation"
    - **line 48** → adds 1 to the streak when a laser hits an asteroid.
    - **line 49** → updates the Streak counter on the screen.
    - **line 50** → checks if the streak is 4 or less, which means the laser limit just went up…
    - **line 51** → …and plays a sound to tell the player.

### Lose the streak

Open ***Objects/Asteroid.py***, add the highlighted code below and save it.

```python linenums="58" hl_lines="8-9" title="Objects/Asteroid.py"
--8<-- "examples/design/subgoals/step07/Objects/Asteroid.py:58:70"
```

??? note "Code explanation"
    - **line 65** → resets the streak to `0` when the ship loses a life.
    - **line 66** → updates the Streak counter on the screen.

!!! primm "PRIMM"
    1. **Predict** how many lasers you can fire at the start of a game, and after shooting three asteroids.
    2. **Run** ***MainController.py*** and test it. Then let an asteroid hit you.
    3. **Investigate**: what happens to the streak when an asteroid hits you while you're shielded? Why?

---

## Don't shoot the astronauts

Go back to ***Objects/Laser.py***, add the highlighted code below and save it.

```python linenums="52" hl_lines="5-7" title="Objects/Laser.py"
--8<-- "examples/design/subgoals/step08/Objects/Laser.py:52:59"
```

??? note "Code explanation"
    - **line 56** → checks that at least one astronaut has been rescued, so the count can't go below `0`…
    - **line 57** → …takes one off the rescued count…
    - **line 58** → …and updates the Rescued counter on the screen.

Finally, the streak needs to start at `0` in each new game. Open ***Objects/Title.py***, add the highlighted code below and save it.

```python linenums="22" hl_lines="7" title="Objects/Title.py"
--8<-- "examples/design/subgoals/step09/Objects/Title.py:22:29"
```

??? note "Code explanation"
    - **line 28** → resets the streak when a new game starts.

!!! primm "PRIMM"
    1. **Predict** what will happen to the Rescued counter when you shoot an astronaut.
    2. **Run** ***MainController.py*** and test both subgoals with a testing table.
    3. **Modify**: is a maximum of 5 lasers right? Try changing the rule in `max_lasers`.

---

## Commit and push

1. In GitHub Desktop, type **Added subgoals** in the **Summary** box.
2. Click **Commit to main**.
3. Click **Push origin**.
