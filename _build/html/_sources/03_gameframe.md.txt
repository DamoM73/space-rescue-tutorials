# Get to know GameFrame

The GameFrame framework is driven by the **Objects**. You will create objects that contain all the game logic. These objects are then placed in **Rooms**.

```{admonition} Game Logic
:class: note
Game Logic is the all the algorithms that make a game work. They govern such things as what happens when a player presses certain keys, or what happens when sepecific object collide with each other, or when the score changes etc.
```

The image below is a screen shot of the game we will be creating.

![Game Play](assets/img/game_play.png)

Everything that you see in the screen is an Object:

- player's spaceship on the left
- enemy spaceship (called Zork) on the right
- asteroids
- astronauts
- score
- player's lives
- the sub-goal tally

They are all inside a Room called **GamePlay**.

Let's look a little deeper.

The player's ship object called **Ship** contains:

- the associated sprite (image)
- the logic that deals with the played pressing keys
- the logic to prevent the ship from moving outside the upper and lower bounds of the room
- the logic that shoot lasers

Other objects have different game logic. For example:

- the Zork object determines when asteroids and astronauts spawn
- the Asteroid object reduces the players health when it collides with the ship
- the Astronaut object increases the score when it collides with the ship
- the Laser object destroys asteroids and astronauts when it collides with them.

Therefore, when creating a game in GameFrame we need to think about the object involved and how the interact with each other and the player.

## File Structure

Another important aspect of GameFrame to understand is it file structure and some of the important files within it. Below is an image of the file structure.

![File Structure](assets/img/file_structure.png)

First is the yellow **SPACE RESCUE** folder. This is called the **root** folder and it contains everything.

The next folder is the green **.venv** folder. This folder contains the files for your virtual environment. Visual Studio Code created this when you made your virtual environment.

All the rest of the files and folders are part of our GameFrame 