# Introduction

In this course we will develop a 2D computer game using Python, Pygame and GameFrame. We will also explore some simple game design concepts.

Before we go any further, let's look at the technology we will be using.

## Python

To understand this course you will need a solid understanding of the basics of Python programming. You will need to understand:

- foundational syntax such as:
  - `for` and `while` loops
  - `if elif else` statements
  - creating and using functions
  - mathematical, conditional and Boolean operations
  - data types
- screen coordinates
- importing and using libraries
- object orientated programming
  - using objects
  - creating objects using `class`

If you are yet to develop this knowledge, then I would suggest completing the following courses before continuing here:

- [A Turtle Introduction to Python](https://damom73.github.io/turtle-introduction-to-python/) for foundational syntax.
- [Deepest Dungeon - Python OOP](https://damom73.github.io/python-oop-with-deepest-dungeon/) for object orientated programming.

## Pygame

Pygame is a popular open-source library for building 2D video games and multimedia applications in the Python . It provides developers with the necessary tools and functionality to create games, simulations, and interactive graphical applications.

Pygame uses abstraction to simplify many complicated programming tasks which computer game programming requires. For example, detecting when different sprites collide with each other. This makes developing games using Pygame much easier then if you were using Python alone.

Being at 2D game engine, Pygame is not used to AAA titles such as Call of Duty, but it can be used to create extensive computer games. There are many games available on Steam that have been created using Pygame.

If you are interested you can find more information on the [Pygame official website](https://www.pygame.org/news).

## GameFrame

In the words of it developer (Steven Tucker) 'GameFrame has been developed to take the excellent PyGame libraries and make them more accessible and easy to use for beginner to intermediate programmers.' Just as Pygame makes developing games with Python easier, GameFrame makes developing games using Pygame easier.

GameFrame is not a library like Pygame, but rather it is an event driven framework. It is made up of a directory structure and a range of different Python files containing classes. Programmers define Rooms and Room Objects, then write functions to handle certain events such as collisions, button clicks and so on. It has clear rules about where files should be saved as well as a range of commands that can be used to develop your program.

## The Stack

Below is an diagram showing the full stack of what we will be using for this course.

![GameFrame stack](assets/gf_stack.png)

Lets explore this:

- On top, the **programmer** interacts with **GameFrame**, using its file structure and the commands in its API.
- **GameFrame** interacts with **Pygame** using the commands available in its API.
- **Pygame** interacts with the **core Python libraries**.

```{admonition} Languages
:class: note
Your code, GameFrame, and Pygame are all written in Python, but this doesn't have to be the case. For example, Pygame uses a library called NumPy which is written in C or C++.
```

If you wish you can access the Pygame API directly. This means that you can use Pygame commands that aren't in the GameFrame API. You won't need to use them to complete this course, although you may wish to use them to add extra features. The [Pygame Documents](https://www.pygame.org/docs/) has all the details.