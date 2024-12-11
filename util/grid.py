from enum import Enum

from util.tuple_arithmetics import tup_add


def get_surroundings(x, y, grid):
    """
    :param x: x index of position we are looking at
    :param y: y index of position we are looking at
    :param grid: array of arrays that form the grid
    :return: values of neighbors as a list, index corresponds to these positions:
        | 0 |  1  | 2 |
        | 3 | pos | 4 |
        | 5 |  6  | 7 |
      Value is None when neighbor does not exist.
    """
    return [get_grid_value(x - 1, y - 1, grid),
            get_grid_value(x, y - 1, grid),
            get_grid_value(x + 1, y - 1, grid),
            get_grid_value(x - 1, y, grid),
            get_grid_value(x + 1, y, grid),
            get_grid_value(x - 1, y + 1, grid),
            get_grid_value(x, y + 1, grid),
            get_grid_value(x + 1, y + 1, grid),
            ]


def get_grid_value(x, y, grid):
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid) - 1:
        return None
    return grid[y][x]


def get_neighbors(pos, grid):
    """
    returns the positions of direct neighbors, that is up, down, left, and right neighbors and no diagonals, if they are located on the grid
   
    :param pos: tuple (row, col) of the position whose neighbors we are after
    :param grid: the grid to plot the positions on
    :return: a list of tuples (row, col) the neighbors' positions
    """
    return [neighbor for direction in Direction if
            (neighbor := tup_add(pos, Direction.step_offset(direction))) and on_grid(neighbor, grid)]


def on_grid(pos, grid):
    """
    :param pos: tuple of form (row,col)
    :param grid: the grid
    :return: True if the position lies within the grid, False otherwise.
    """
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)


class Direction(Enum):
    UP = 1
    DOWN = 6
    LEFT = 3
    RIGHT = 4

    @staticmethod
    def step_offset(direction):
        if direction == Direction.UP:
            return 0, -1
        elif direction == Direction.DOWN:
            return 0, 1
        elif direction == Direction.LEFT:
            return -1, 0
        elif direction == Direction.RIGHT:
            return 1, 0
        else:
            raise ValueError('direction must be UP, RIGHT, DOWN, or LEFT')

    @staticmethod
    def turn_right(direction):
        if direction == Direction.UP:
            return Direction.RIGHT
        elif direction == Direction.DOWN:
            return Direction.LEFT
        elif direction == Direction.LEFT:
            return Direction.UP
        elif direction == Direction.RIGHT:
            return Direction.DOWN
        else:
            raise ValueError('direction must be UP, RIGHT, DOWN, or LEFT')
