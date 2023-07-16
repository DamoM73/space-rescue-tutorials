# Get to know GameFrame

```{topic} In this lesson you will:
- Learn the file structure of the GameFrame framework
- Learn about the important files in the GameFrame framework
```

## How GameFrame works

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

## Documentation

We will cover many of the features on GameFrame through this tutorial. If you want to dig deeper, or use GameFrame for other purposes, then the full documentation can be found on the [GameFrame API](./documentation.md) page.

## File Structure

Another important aspect of GameFrame to understand is it file structure and some of the important files within it. Below is an image of the file structure.

```{figure} assets/img/file_structure.png
---
align: left
---
```

First is the yellow **SPACE RESCUE** folder. This is called the **root** folder and it contains everything.

The next folder is the green **.venv** folder. This folder contains the files for your virtual environment. Visual Studio Code created this when you made your virtual environment.

The rest of the files and folders are part of our GameFrame framework. All the GameFrame folders (root, GameFrame, Images, Objects, Rooms and Sounds) have a **`notes.md`** file. These file contain the documentation relevant for that specific folder. The entire documentation can be found on the [GameFrame API](./documentation.md) page.

Next is the red **GameFrame** folder. This folder is the engine behind GameFrame. It has many files which hold most of the code. The only file you need to be concerned about is the **`Globals.py`** file. This file contain the variables that are applicable to the entire program.

The blue **Images** and **Sounds** folders contain all the images and sounds that your game uses. They have pre-populated with the assets we need for Space Rescue, but if you want to add more, or if you are using GameFrame for other projects, then this is where the files should go.

The purple **Objects** and **Rooms** folders are where you will write most of your code. Your object and room classes will go into these folders in new files. For example, we will be creating a `Ship.py` file that contains our `Ship` class in the **Objects** folder.

Notice that both of the purple folder have a **`__init__.py`** file. This is very important. Since our GameFrame files are spread across various folders, we need to link them all together. This is done using the `__init__.py` files. This means that when you create a new file and class you need to link it to the rest of GameFrame using the `__init__.py` files. Going back to our previous ship example, we would need to add the following line to the `__init__.py` in the **Objects** folder:

``` python
from Objects.Ship import Ship
```

The last file of note is the **MainController.py** in the root folder. This is the file that you run to start the program.
