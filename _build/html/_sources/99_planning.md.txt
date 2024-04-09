# Creating your own game

```{topic} In this lesson you will:
- learn how to plan a new game for the GameFrame framework
- learn the important processes of creating a new game
```

## Planning the Game

Way back in our **[introduction to GameFrame](./03_gameframe.md)** we identified that a GameFram game consists of the RoomObjects inside a series of Rooms. We will use this concept to help plan new games.

### Step 1 - Determine the Rooms

The first step is to work out how many levels (Rooms) the new game will have. For example, the Space Rescue game that we just completed consisted of two Rooms &mdash; WelcomeScreen and GamePlay.

### Step 2 - Draw wireframes

Once the number of Rooms have been determined, you will need to draw a wireframe for each of the Rooms.

```{admonition} Wireframes
:class: note
A wireframe is like a blueprint or skeleton of a website or app. It's a simple, basic outline that shows where different elements, like buttons, images, and text, will go on the screen. It focuses on the layout and arrangement of elements rather than the colors or details. It's a helpful tool for visualizing and discussing ideas before creating the final design, just like making a rough sketch or draft of a drawing before adding all the details.
```

A Room's wireframe should contain a placeholder for every RoomObject that is going to appear in the Room. The placeholder can be as simple a box, but it should be approximately the right size.

Below is a wireframe for Space Rescue's GamePlay Room. For the sake of brevity, we will only show the wireframe for the GamePlay Room, but in your design you should have a wireframe for each sufficiently different Room.

![planning_wireframe](./assets/img/planning_wireframe.png)

### Step 3 - Annotate RoomObjects

Now that you have identified all the Rooms the game will use, as well as all the RoomObjects in each Room, it is time to start describing the game.

Remember that the a GameFrame game consists through the interactions between RoomObjects. Therefore you  describe the game through describing each of the RoomObjects.

Annotate each RoomObject explaining what RoomObject does.

Below is our Space Rescue GamePlay Room wireframe, with annotations.

![planning_wirefram_with_annotations](./assets/img/planning_wirefram_with_annotations.png)

### Step 4 - Create Class Diagrams

Now that you know what you want your RoomObjects to do, you need to fit that into the GameFrame framework. RoomObjects are classes, so use class diagrams to rewrite the RoomObject descriptions into classes. Remember we have been using class diagrams since **[Deepest Dungeon](https://damom73.github.io/python-oop-with-deepest-dungeon/stage_1.html#class-diagram)**.

You need to create a class diagram for each RoomObject, remember:

- attributes:
  - describe features of the object
  - refer to the variable that belong to the object
  - go above the line
- methods:
  - describe actions the object take
  - refer to the differnt functions that belong to the object
  - go under the line

Below is the Space Rescue GamePlay Room wireframe with the addition of the class diagram.

![planning _wireframe_with_class_diagrams](./assets/img/planning_wireframe_with_class_diagrams.png)

### Step 5 - Start Coding

Now you have sketched out the basic structure of the new game, it is time to start creating your code.

#### Setup programming environment

The blank copy of GameFrame can be found **[here on GitHub](https://github.com/DamoM73/GameFrame)**.

Follow the sames process we used in **[the Setup page](./02_setup.md)**.

## Processes

In this section, you will find flowcharts to remind you of the steps to complete some of the most common GameFrame processes.

### Create a Room

We created rooms in the following tutorials:

- **[Welcome screen](./04_welcome.md)**
- **[GamePlay Room](./05_gameplay.md)**

Below is the process followed.

![Create room](./assets/img/create_room.png)

### Create a RoomObject

In the tutorials we created RoomObjects in the following tutorials:

- **[Welcome screen](./04_welcome.md)**
- **[Spaceship Object](./06_spaceship.md)**
- **[Add Zork Object](./09_add_boss.md)**
- **[Add Asteroids](./10_add_asteroids.md)**
- **[Add Laser](./13_laser.md)**
- **[Add Astronaut](./15_astronaut.md)**
- **[Add Lives](./17_lives.md)**

Below is the process followed.

![Create room object](./assets/img/create_room_object.png)

### Create TextObject

In the tutorials we created TextObjects in the following tutorial:

- **[Add Scoring](./16_scoring.md)**

### Move Object using Keys

We made RoomObjects respond to keys in the following tutorials:

- **[Add Zork Object](./09_add_boss.md)**
- **[GamePlay Room](./05_gameplay.md)**
- **[Spaceship Object](./06_spaceship.md)**
- **[Add Laser](./13_laser.md)**

Below is the process followed.

![Move Object using keys](./assets/img/move_object_with_keys.png)

### Move RoomObject upon creation

We made RoomObjects move upon creation in the following tutorials:

- **[Move Asteroids](./11_animate_asteroids.md)**
- **[Add Laser](./13_laser.md)**
- **[Add Astronaut](./15_astronaut.md)**

### Handle Collisions

We handled collisions in the following tutorials:

- **[Ship and Asteroid Collision](./12_ship_astroid_collision.md)**
- **[Laser Asteroid Collision](./14_laser_asteroid_collision.md)**
- **[Add Astronaut](./15_astronaut.md)**
- **[Add Scoring](./16_scoring.md)**

![Handle collisions](./assets/img/handle_collisions.png)

### Spawn RoomObject

We spawned RoomObjects in the following tutorials:

- in response to timers:
  - **[Add Asteroids](./10_add_asteroids.md)**
  - **[Add Astronaut](./15_astronaut.md)**
- in response to key presses:
  - **[Add Laser](./13_laser.md)**

### Bounce RoomObject off Screen Edge

We made RoomObjects bounce of the edge of the screen in the following tutorials:

- **[Add Zork Object](./09_add_boss.md)**
- **[Move Asteroids](./11_animate_asteroids.md)**

### Keep RoomObject in Room

We restricted RoomObjects from leaving the Room in the following tutorial:

- **[Keeping Ship in the Room](./08_ship_in_bounds.md)**

### Despawn RoomObject when it leaves Room

We despawned RoomObjects when they left the Room in the following tutorials:

- **[Move Asteroids](./11_animate_asteroids.md)**
- **[Add Laser](./13_laser.md)**
- **[Add Astronaut](./15_astronaut.md)**

### Changing Rooms

We changed Rooms in the following tutorial:

- **[GamePlay Room](./05_gameplay.md)**

### Changed the Score

We changed the Score in the following tutorial:

- **[Add Scoring](./16_scoring.md)**

### Changed Lives

We changed lives in the following tutorial:

- **[Add Lives](./17_lives.md)**