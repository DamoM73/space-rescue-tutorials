# Goals and Rewards

!!! learn "In this lesson we will learn"
    - how to give the player a clear goal and show their progress
    - how to reward the player for reaching the goal
    - how to make the game harder as the player gets closer to the goal
    - how to use an f-string to build text from variables

!!! terms "Terminology"
    - **f-string** – a Python string with an `f` before the quotes that puts the values of variables inside `{ }` into the text.
    - **robust** – describes code that still works correctly when something unexpected happens.

In [Game Design](game_design.md) we found that Space Rescue has no goal: the player just collects astronauts forever. That means there's no what-if effect and no reason to keep trying. Let's fix that.

## Planning

Here's what we decided in Game Design:

| The problem | The solution |
| --- | --- |
| The player doesn't have a goal | set a goal for the number of astronauts rescued |
| The player doesn't know what the goal is | show the number of astronauts to rescue |
| The player doesn't know how close they are | show the number of astronauts rescued |
| The player might reach the goal too quickly | spawn astronauts less often as more are rescued |
| No reward for reaching the goal | give big bonus points for reaching the goal |

So we need:

1. two new variables in ***Globals.py***: the goal (`rescue_goal`) and the number rescued so far (`rescued`)
2. a new HUD item that shows `Rescued: 3 / 10`
3. code in the Astronaut's ship collision that adds to `rescued`, updates the HUD, and checks if the goal is reached
4. a reward when the goal is reached: 500 bonus points and a sound, then the game ends
5. Zork's astronaut timer gets longer as more astronauts are rescued

| Input | Process | Output |
| --- | --- | --- |
| the ship rescues an astronaut | add 1 to `rescued` and update the HUD; if `rescued` has reached `rescue_goal`, add 500 points, play the bonus sound and end the game | the HUD shows the new count; the player wins when they reach the goal |

---

## Add the goal

Open ***GameFrame/Globals.py***, add the highlighted code below at the bottom and save it.

```python linenums="45" hl_lines="6-8" title="GameFrame/Globals.py"
--8<-- "examples/design/goals_rewards/step01/GameFrame/Globals.py:45:52"
```

??? note "Code explanation"
    - **line 51** → sets the goal: rescue 10 astronauts.
    - **line 52** → counts the astronauts rescued so far, starting at `0`.

---

## Show the progress

We'll add a `Rescued` class to the HUD. It's a TextObject, like the `Score`. Open ***Objects/Hud.py***, add the highlighted code below to the bottom and save it.

```python linenums="51" hl_lines="3-11 13-17 19-24" title="Objects/Hud.py"
--8<-- "examples/design/goals_rewards/step02/Objects/Hud.py:51:74"
```

??? note "Code explanation"
    - **line 53** → defines the `Rescued` class as a subclass of `TextObject`.
    - **lines 54–56** → a docstring that explains what the class is for.
    - **line 57** → defines the `__init__` method. Unlike `Score`, it doesn't take any text, because it builds its own.
    - **lines 58–60** → a docstring that explains what the method does.
    - **line 61** → runs `TextObject`'s `__init__` method.
    - **lines 64–66** → set the font size, font and colour.
    - **line 67** → calls `update_rescued` to draw the text for the first time.
    - **line 69** → defines the `update_rescued` method.
    - **lines 70–72** → a docstring that explains what the method does.
    - **line 73** → builds the text with an **f-string**, which puts the values of `Globals.rescued` and `Globals.rescue_goal` inside the `{ }`, for example `Rescued: 3 / 10`.
    - **line 74** → redraws the text on the screen.

Open ***Objects/\_\_init\_\_.py***, change the highlighted code below and save it.

```python linenums="1" hl_lines="7" title="Objects/__init__.py"
--8<-- "examples/design/goals_rewards/step03/Objects/__init__.py"
```

??? note "Code explanation"
    - **line 7** → imports the `Rescued` class as well as `Score` and `Lives`.

Open ***Rooms/GamePlay.py***, add the highlighted code below and save it.

```python linenums="1" hl_lines="4 24-25 33" title="Rooms/GamePlay.py"
--8<-- "examples/design/goals_rewards/step04/Rooms/GamePlay.py"
```

??? note "Code explanation"
    - **line 4** → imports the `Rescued` class.
    - **line 24** → creates a Rescued counter in the bottom-left corner of the screen, and stores it in `self.rescued` so the astronauts can update it.
    - **line 25** → adds the counter to the Room.
    - **line 33** → loads the bonus sound for reaching the goal.

---

## Count rescues and reward the goal

Open ***Objects/Astronaut.py***, add the highlighted code below and save it.

```python linenums="1" hl_lines="1 41-46" title="Objects/Astronaut.py"
--8<-- "examples/design/goals_rewards/step05/Objects/Astronaut.py:1:47"
```

??? note "Code explanation"
    - **line 1** → imports `Globals`, so the astronaut can update the rescued count.
    - **line 41** → adds 1 to the number of astronauts rescued.
    - **line 42** → updates the counter on the screen.
    - **line 43** → checks if the player has reached the goal…
    - **line 44** → …plays the bonus sound…
    - **line 45** → …adds 500 bonus points…
    - **line 46** → …and ends the GamePlay Room, so the game goes back to the welcome screen.

!!! tip "Why >= and not ==?"
    `Globals.rescued` should never jump past the goal, so `==` would work too. But using `>=` means the game still ends if something unexpected pushes the count past the goal. It's a small habit that makes code more **robust**.

The rescued count needs to start at `0` in every new game, just like the score and lives. Open ***Objects/Title.py***, add the highlighted code below and save it.

```python linenums="18" hl_lines="10" title="Objects/Title.py"
--8<-- "examples/design/goals_rewards/step06/Objects/Title.py:18:28"
```

??? note "Code explanation"
    - **line 27** → resets the rescued count to `0` when a new game starts.

!!! primm "PRIMM"
    1. **Predict** what will happen when you rescue the tenth astronaut.
    2. **Run** ***MainController.py*** and rescue ten astronauts.
    3. **Investigate**: change `rescue_goal` to `3` to test it faster. Change it back when you're done.

---

## Make the goal harder to reach

To make the what-if effect stronger, astronauts should appear less often as the player gets closer to the goal. We'll add 20 ticks to Zork's astronaut timer for every astronaut rescued. Open ***Objects/Zork.py***, change the highlighted code below and save it.

```python linenums="1" hl_lines="28-29 65-66" title="Objects/Zork.py"
--8<-- "examples/design/goals_rewards/step07/Objects/Zork.py"
```

??? note "Code explanation"
    - **line 29** → adds `Globals.rescued * 20` ticks to the first astronaut's timer. At the start of a game `rescued` is `0`, so nothing changes.
    - **line 66** → adds the same extra time when choosing when the next astronaut appears. After 9 rescues, astronauts take up to 180 ticks (6 seconds) longer to appear.

!!! primm "PRIMM"
    1. **Predict** how the game will feel near the end now.
    2. **Run** ***MainController.py*** and play a whole game.
    3. **Modify**: is 20 ticks too much or too little? Change it until the end of the game feels tense but fair.

---

## Commit and push

1. In GitHub Desktop, type **Added rescue goal** in the **Summary** box.
2. Click **Commit to main**.
3. Click **Push origin**.
