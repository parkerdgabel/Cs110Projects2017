from drawingpanel import *
from random import randint
PANEL_WIDTH = 500
PANEL_HEIGHT = 300


def oval(panel):
    """Backgroud oval."""
    panel.fill_oval(50, 60, 20, 30, "magenta")


def rectangle(panel):
    """Backgroud Rectangle."""
    panel.fill_rect(100, 150, 70, 100, "purple2")


def triangle(panel):
    """Backgroud Triangle."""
    panel.fill_polygon(300, 150, 250, 200, 350, 275, "peru")


def transform_x_left(x, i):
    """Function to tranform the green lines diagonally left."""
    return (x + i) - 10


def transform_x_right(x, i):
    """Function to tranform the green lines diagonally right."""
    return (x + i) + 10


def transform_x(x, i):
    """Function to tranform the green lines up."""
    return x + i


def draw_green_lines(panel, x, y, x_transform_func):
    """Function to draw a generic green line."""
    for i in range(5):
        panel.draw_line(x + i, y, x_transform_func(x, i), y - 10, "green4")


def draw_leaves_left(panel, x, y):
    """Wrapper to transform lines diagonally left."""
    draw_green_lines(panel, x, y, transform_x_left)


def draw_leaves_right(panel, x, y):
    """Wrapper to transform lines diagonally right."""
    draw_green_lines(panel, x, y, transform_x_right)


def draw_stalk(panel, x, y):
    """Wrapper to transform lines up."""
    draw_green_lines(panel, x, y, transform_x)


def draw_outer_pedals(panel, x, y):
    """Draws the outer pedals of the flower."""
    panel.fill_oval(x - 23, y - 50, 50, 50, "red1")


def draw_inner_pedals(panel, x, y):
    """Draws the inner pedals of the flower."""
    panel.fill_oval(x - 3, y - 29, 10, 10, "yellow3")


def pedals(panel, x, y):
    """Draws both pedals of the flower."""
    draw_outer_pedals(panel, x, y)
    draw_inner_pedals(panel, x, y)


def leaves(panel, x, y):
    draw_stalk(panel, x, y)
    draw_leaves_left(panel, x, y - 10)
    draw_stalk(panel, x, y - 10)
    draw_leaves_right(panel, x, y - 20)


def flower_complete(panel, x, y):
    for i in range(5):
        leaves(panel, x, y)
        y = y - 20
    draw_stalk(panel, x, y)
    y = y - 10
    draw_stalk(panel, x, y)
    y = y - 10
    draw_stalk(panel, x, y)
    pedals(panel, x, y)


def flower(panel, steps):
    x = randint(50, PANEL_WIDTH - 50)
    y = PANEL_HEIGHT
    for i in range(steps // 5000):
        flower_complete(panel, x, y)
        x = randint(50, PANEL_WIDTH - 50)
    for i in range((steps % 5000) // 1000):
        leaves(panel, x, y)
        y = y - 20
    draw_stalk(panel, x, y)
    y = y - 10
    draw_stalk(panel, x, y)
    y = y - 10
    draw_stalk(panel, x, y)
    pedals(panel, x, y)


def main():
    steps = int(input("How many steps have you walked? "))
    panel = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT, "CadetBlue")
    oval(panel)
    rectangle(panel)
    triangle(panel)
    flower(panel, steps)


main()
