from GameFrame import Level
from Objects.Block import Block
from Objects.Explorer import Explorer
from Objects.Exit import Exit

class Maze(Level):
    """
    A top-down maze demo
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # the maze: # is a wall, P is the player, E is the exit
        layout = [
            "##############################",
            "#P.......#...........#.......#",
            "#.######.#.#########.#.#####.#",
            "#.#......#.#.......#...#...#.#",
            "#.#.######.#.#####.#####.#.#.#",
            "#.#........#.#...#.......#...#",
            "#.##########.#.#.#########.###",
            "#............#.#...........#.#",
            "############.#.###########.#.#",
            "#............#...........#...#",
            "#.######################.###.#",
            "#.#....................#.....#",
            "#.#.##################.#######",
            "#...#................#.......#",
            "#####.##############.#######.#",
            "#.....#............#.......#.#",
            "#.#####.##########.#######.#.#",
            "#.................#.........E#",
            "##############################",
        ]
        
        # turn each character into an object
        for row, line in enumerate(layout):
            for col, cell in enumerate(line):
                x = col * 42
                y = row * 42
                if cell == "#":
                    self.add_room_object(Block(self, x, y))
                elif cell == "E":
                    self.add_room_object(Exit(self, x, y))
                elif cell == "P":
                    self.add_room_object(Explorer(self, x + 3, y + 3))
