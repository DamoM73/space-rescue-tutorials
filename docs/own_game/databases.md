# Saving Data with a Database

!!! learn "On this page we will learn"
    - why games use databases to keep data between games
    - how to create a table, add rows and query them with SQL
    - how GameFrame's `DataBaseController` connects to an SQLite database
    - how to let the player type text with an `EntryTextObject`
    - how to create TextObjects without writing a new class

!!! terms "Terminology"
    - **database** – an organised store of data that is saved permanently, so it is kept after the program closes.
    - **table** – the part of a database that stores data in rows and columns, a bit like a spreadsheet.
    - **row** – one record in a database table.
    - **column** – one piece of information that is stored for every row in a database table.
    - **SQL** – short for Structured Query Language, the language used to create, add to and get data from a database.
    - **query** – an SQL statement that asks a database for data.
    - **SQLite** – a type of database that stores a whole database in a single file, which Python can use with its built-in library.
    - **cursor** – the object that runs SQL statements on a database.
    - **override** – to replace a method inherited from the parent class with a new version in the subclass.
    - **unpack** – to split the values in a tuple into separate variables in one step.

Everything in our game so far disappears when we close it. The score, the lives and the rescued count are all stored in variables, and variables only last while the program runs. To keep data between games, we need to save it somewhere permanent, like a **database**.

In this extension, we'll add a **high score table** to Space Rescue. When a game ends, the player types their initials, their score is saved in a database, and the top five scores are shown.

!!! tip "Before you start"
    This page continues from the end of [Ship Choice](../design/ship_choice.md). If you skipped some of the Game Design pages, you can start from the Ship Choice checkpoint in the [tutorial files](../index.md#tutorial-files).

## Planning

### Databases and SQL

A **database** stores data in **tables**, a bit like a spreadsheet. Each **row** is one record, and each **column** is one piece of information about it. Our table will be called `Scores`:

| name | score |
| --- | --- |
| ZAK | 1250 |
| MIA | 980 |
| SAM | 615 |

We talk to a database with **SQL** (Structured Query Language). We'll need three SQL statements:

| SQL | What it does |
| --- | --- |
| `CREATE TABLE IF NOT EXISTS` | creates the `Scores` table the first time the game saves a score |
| `INSERT INTO` | adds a row with the player's initials and score |
| `SELECT … ORDER BY score DESC LIMIT 5` | gets the five highest scores, highest first |

Python has a built-in library for **SQLite** databases, which store a whole database in one file. GameFrame's `DataBaseController` class (in ***GameFrame/DataBaseController.py***) already connects to an SQLite file. We just need to add a method for each SQL statement.

### A new Room

We'll add a **HighScores** Room after GamePlay. When GamePlay ends, GameFrame moves on to HighScores, and when HighScores ends, it goes back to the WelcomeScreen (the first Room in `levels`).

| Event | Input | Process | Output |
| --- | --- | --- | --- |
| Game ends | GamePlay ends | start the HighScores Room | the player's score and an entry box are shown |
| Type initials | the player types letters | add them to the entry box (up to 3) | the initials appear on the screen |
| Save | the player presses ++enter++ | save the initials and score in the database, then get the top five | the top five scores are shown |
| Finish | 5 seconds after saving | end the Room | the welcome screen is shown |

---

## Add the database methods

Open ***GameFrame/DataBaseController.py***. Replace the example query at the bottom (the lines inside `'''` that define `get_lesson`) with the highlighted code below, and save it.

```python linenums="1" hl_lines="14-26 28-39 41-54" title="GameFrame/DataBaseController.py"
--8<-- "examples/own_game/databases/step01/GameFrame/DataBaseController.py"
```

??? note "Code explanation"
    - **line 14** → defines the `create_scores_table` method.
    - **lines 15–17** → a docstring that explains what the method does.
    - **line 18** → runs an SQL statement on the database, using the **cursor** GameFrame created on line 9.
    - **lines 19–24** → the SQL statement, in a multi-line string. It creates a table called `Scores` with a text column for the name and a whole-number column for the score. `IF NOT EXISTS` means it only creates the table the first time.
    - **line 25** → closes the `execute` brackets.
    - **line 26** → **commits** (saves) the change to the database file.
    - **line 28** → defines the `add_score` method, which takes the initials and the score.
    - **lines 29–31** → a docstring that explains what the method does.
    - **line 32** → runs an SQL statement…
    - **lines 33–36** → …that inserts a new row. `:name` and `:score` are **placeholders**…
    - **line 37** → …and this dictionary fills them in. Using placeholders (rather than joining strings together) keeps the data safe, whatever the player types.
    - **line 38** → closes the `execute` brackets.
    - **line 39** → commits the new row to the database file.
    - **line 41** → defines the `get_top_scores` method, which takes how many scores to get.
    - **lines 42–44** → a docstring that explains what the method does.
    - **line 45** → runs an SQL statement…
    - **lines 46–51** → …that selects the name and score from every row, sorts them from highest to lowest score (`DESC`), and keeps only the first `:count` rows…
    - **line 52** → …filling in `:count`.
    - **line 53** → closes the `execute` brackets.
    - **line 54** → **returns** the rows as a list of tuples, for example `[('ZAK', 1250), ('MIA', 980)]`.

!!! tip "Learning SQL"
    SQL is used in almost every app and website that stores data. Try changing `LIMIT :count` to `LIMIT 10`, or adding a `WHERE score > 0` line, and see what changes in the table.

Open ***GameFrame/Globals.py***, change the highlighted code below and save it.

```python linenums="18" hl_lines="2" title="GameFrame/Globals.py"
--8<-- "examples/own_game/databases/step02/GameFrame/Globals.py:18:19"
```

??? note "Code explanation"
    - **line 19** → adds `"HighScores"` to the end of the list of Rooms, so it comes straight after GamePlay.

---

## Type the initials

GameFrame has an `EntryTextObject` class: a TextObject that the player can type into. It adds letters as they're pressed, removes them with ++backspace++, and stops at a maximum length. We'll make a subclass of it that also saves the score when ++enter++ is pressed.

Create a new file in the ***Objects*** folder, add the code below and save it as ***HighScoreEntry.py***.

```python linenums="1" hl_lines="1-2 4-12 14-19 21-26 28-30 32-42" title="Objects/HighScoreEntry.py"
--8<-- "examples/own_game/databases/step03/Objects/HighScoreEntry.py"
```

??? note "Code explanation"
    - **line 1** → imports `EntryTextObject`, `Globals` and `DataBaseController` from GameFrame.
    - **line 2** → imports Pygame for the ++enter++ key name.
    - **line 4** → defines the `HighScoreEntry` class as a subclass of `EntryTextObject`.
    - **lines 5–7** → a docstring that explains what the class is for.
    - **line 8** → defines the `__init__` method.
    - **lines 9–11** → a docstring that explains what the method does.
    - **line 12** → runs `EntryTextObject`'s `__init__` method, with a maximum of 3 characters.
    - **lines 15–17** → set the font size, font and colour (yellow).
    - **line 18** → redraws the text with these settings.
    - **line 19** → creates a `saved` flag, so the score is only saved once.
    - **line 21** → defines `key_pressed`. This **overrides** (replaces) the `key_pressed` method from `EntryTextObject`.
    - **lines 22–24** → a docstring that explains what the method does.
    - **lines 25–26** → leave the method straight away if the score has already been saved.
    - **line 28** → runs `EntryTextObject`'s own `key_pressed` method, so the typing still works.
    - **line 29** → checks if ++enter++ is pressed **and** at least one letter has been typed…
    - **line 30** → …and saves the score.
    - **line 32** → defines the `save_score` method.
    - **lines 33–35** → a docstring that explains what the method does.
    - **line 36** → sets the `saved` flag.
    - **line 37** → connects to the database file ***scores.db***. If it doesn't exist yet, SQLite creates it in the ***GameFrame*** folder.
    - **line 38** → creates the `Scores` table if it isn't there yet.
    - **line 39** → saves the initials and the score.
    - **line 40** → gets the top five scores.
    - **line 41** → closes the connection to the database.
    - **line 42** → asks the Room to show the top scores.

!!! tip "Overriding and calling the parent method"
    Line 28 is a pattern we've used in every `__init__` method: run the **parent** class's version of the method, then add our own code. Here we do it with `key_pressed`, so we keep all of `EntryTextObject`'s typing and add the ++enter++ key.

Open ***Objects/\_\_init\_\_.py***, add the highlighted code below and save it.

```python linenums="1" hl_lines="11" title="Objects/__init__.py"
--8<-- "examples/own_game/databases/step04/Objects/__init__.py"
```

??? note "Code explanation"
    - **line 11** → imports the `HighScoreEntry` class.

---

## Create the HighScores Room

Create a new file in the ***Rooms*** folder, add the code below and save it as ***HighScores.py***.

```python linenums="1" hl_lines="1-2 4-9 11-12 14-18 20-21 23-28 30-35 37-38 40-44" title="Rooms/HighScores.py"
--8<-- "examples/own_game/databases/step05/Rooms/HighScores.py"
```

??? note "Code explanation"
    - **line 1** → imports `Level`, `Globals` and `TextObject`.
    - **line 2** → imports the `HighScoreEntry` class.
    - **line 4** → defines the `HighScores` class as a subclass of `Level`.
    - **lines 5–7** → a docstring that explains what the class is for.
    - **lines 8–9** → define `__init__` and run `Level`'s `__init__` method.
    - **line 12** → sets the background image.
    - **line 15** → creates a TextObject showing the player's score. We don't need a new class for text that just sits on the screen: we give `TextObject` the Room, position, text, size, font and colour directly.
    - **line 16** → adds it to the Room.
    - **line 17** → creates a TextObject with instructions, and stores it so we can change it later.
    - **line 18** → adds it to the Room.
    - **line 21** → adds the HighScoreEntry box under the instructions.
    - **line 23** → defines the `show_scores` method, which takes the list of top scores.
    - **lines 24–26** → a docstring that explains what the method does.
    - **line 27** → changes the instructions to a heading…
    - **line 28** → …and redraws it.
    - **line 31** → sets the `y` position of the first score.
    - **line 32** → loops through the top scores. Each one is a tuple, so we can **unpack** it into `name` and `score`.
    - **line 33** → creates a TextObject for this score…
    - **line 34** → …adds it to the Room…
    - **line 35** → …and moves 50 pixels down for the next one.
    - **line 38** → starts a 5-second timer that calls `finish`.
    - **line 40** → defines the `finish` method.
    - **lines 41–43** → a docstring that explains what the method does.
    - **line 44** → ends the Room. It's the last Room in `levels`, so the game goes back to the WelcomeScreen.

Open ***Rooms/\_\_init\_\_.py***, add the highlighted code below and save it.

```python linenums="1" hl_lines="5" title="Rooms/__init__.py"
--8<-- "examples/own_game/databases/step06/Rooms/__init__.py"
```

??? note "Code explanation"
    - **line 5** → imports the `HighScores` class.

!!! primm "PRIMM"
    1. **Predict** what you'll see when a game ends.
    2. **Run** ***MainController.py***, play two games and save a score each time.
    3. **Investigate**: close the game and run it again. Are your scores still there? Why?

!!! warning "Don't commit the database"
    ***scores.db*** is your own data, not code. If you don't want it in your GitHub repo, add a line `*.db` to your ***.gitignore*** file before you commit.

---

## Commit and push

1. In GitHub Desktop, type **Added high score table** in the **Summary** box.
2. Click **Commit to main**.
3. Click **Push origin**.
