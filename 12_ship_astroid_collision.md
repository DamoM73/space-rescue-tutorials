# Ship and Asteroid Collision

```{topic} In this lesson you will:
- learn about hitboxes and collisions
- learn how to detect collisions
- use the build-in GameFrame feature to detect and handle collisions
```

## Hitboxes

Collisions refer to the interactions between different game objects in a game when they overlap or come into contact with each other. GameFrame uses Rectangular Collisions which involve bounding rectangles that surround objects. This rectangles are often referred to as hitboxes.

We have already been using this this concept of hitboxes. For example, in our game asteroids look like this.

![asteroid](assets/img/asteroid.png)

But we have used the image below to represent asteroids.

![object boundaries](assets/img/object_boundaries.png)

We have been using hitboxes to represent all our objects. For example, when the **top boundary** of the Zork **hitbox** **collides** with the top of the screen, we reverse Zork's direction.

## Collisions

Collisions occur between two objects when their hitboxes touch or overlap. 

- obj_1's left boundary is less than obj_2's right boundary **and**
- obj_1's right boundary is greater than obj_2's left boundary **and**
- obj_1's top boundary is less than obj_2's bottom boundary **and**
- obj_1's bottom boundary is greater than obj_2's top boundary.

If we wanted to use the coordinates from this image:

![collision coordinates](assets/img/collision.png)

Then the code would be:

```{code-block} python
if (obj1.x < obj2.x + obj2.width and
    obj1.x + obj1.width > obj2.x and
    obj1.y < obj2.y + obj2.height and
    obj1.y + obj1.height > obj2.y):
```

That's a whole heap of code to understand and remember. Fortunately, this is all just for background. Since GameFrame is based on Pygame, there are is a built in process for detecting and handling collisions.

