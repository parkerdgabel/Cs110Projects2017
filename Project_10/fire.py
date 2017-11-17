# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #10, 11/14/17
# This program simulates a fire spreading.
from DrawingPanel import *
from random import randint

PROPAGATION_PERCENTAGE = 75
PAUSE_LENGTH = 100


def main():
    name = prompt_file_name()
    infile = open(name)
    grid = init_grid(infile)
    panel = init_panel(grid)
    while on_fire(grid):
        update_panel(panel, grid)
        new_grid = grid
        simulate_fire(grid, new_grid)
        grid = new_grid
    update_panel(panel, grid)


def prompt_file_name():
    """Prompts the user for the input filename
    Args: None
    Returns: string representing the input file name"""
    return input("Enter the name of the input file: ")


def init_grid(infile):
    """Converts the input file into the grid used for the simulation.
    Args: infile file
    Returns: grid list(list)"""
    lines = infile.readlines()
    grid = []
    for line in lines:
        row = []
        line = line.strip().split()
        for elem in line:
            row.append(int(elem))
        grid.append(row)
    return grid


def init_panel(grid):
    """Initiates a drawing panel of proper size.
    Args: grid list(list)
    Returns: DrawingPanel"""
    return DrawingPanel(len(grid[0]) * 10, len(grid) * 10)


def update_panel(panel, grid):
    """Updates the drawing panel to reflect a new state
    Args:    panel DrawingPanel
             grid list(list)
    Returns: None"""
    x_loc = 0
    y_loc = 0
    panel.sleep(PAUSE_LENGTH)
    for r in range(len(grid)):
        x_loc = 0
        for c in range(len(grid[r])):
            if grid[r][c] == 0:
                panel.fill_rect(x_loc, y_loc, 10, 10, "yellow")
            elif grid[r][c] == 1:
                panel.fill_rect(x_loc, y_loc, 10, 10, "green")
            else:
                panel.fill_rect(x_loc, y_loc, 10, 10, "red")
            x_loc += 10
        y_loc += 10


def has_fire_neighbor(i, j, grid):
    """Checks if a tile has a neighbor on fire.
    Args:    i int
             j int
             grid list(list)
    Returns: bool"""
    if grid[i + 1][j] == 2 or grid[i - 1][j] == 2:
        return True
    elif grid[i][j + 1] == 2 or grid[i][j + 1] == 2:
        return True
    else:
        return False


def propagate_fire(i, j, new_grid):
    """Determines whether a fire spreads or not.
    Args:    i int
             j int
             new_grid list(list)
    Returns: None"""
    if randint(0, 101) < PROPAGATION_PERCENTAGE:
        new_grid[i][j] = 2


def on_fire(grid):
    """Checks to see if the grid has any active fire tiles.
    Args:    grid list(list)
    Returns: bool"""
    for row in grid:
        for elem in row:
            if elem == 2:
                return True
    return False


def simulate_fire(grid, new_grid):
    """Simulates the fire.
    Args:     grid list(list)
              new_grid list(list)
    Returns:  None"""
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1 and has_fire_neighbor(r, c, grid):
                propagate_fire(r, c, new_grid)
            elif grid[r][c] == 2:
                new_grid[r][c] = 0


main()
