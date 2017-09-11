from drawingpanel import *

PANEL_WIDTH = 500
PANEL_HEIGHT = 300


def oval(panel):
    panel.fill_oval(50, 60, 20, 30, "magenta")


def rectangle(panel):
    panel.fill_rect(100, 150, 70, 100, "purple2")


def triangle(panel):
    panel.fill_polygon(300, 150, 250, 200, 350, 275, "peru")


def transform_x_left(x, i):
    return (x + i) - 10


def transform_x_right(x, i):
    return (x + i) + 10


def transform_x(x, i):
    return x + i


def draw_green_lines(panel, x, y, x_transform_func):
    for i in range(5):
        panel.draw_line(x + i, y, x_transform_func(x, i), y - 10, "green4")


def draw_leaves_left(panel, x, y):
    draw_green_lines(panel, x, y, transform_x_left)


def draw_leaves_right(panel, x, y):
    draw_green_lines(panel, x, y, transform_x_right)


def draw_stalk(panel, x, y):
    draw_green_lines(panel, x, y, transform_x)


def draw_outer_pedals(panel, x, y):
    panel.fill_oval(x - 23, y - 50, 50, 50, "red1")


def draw_inner_pedals(panel, x, y):
    panel.fill_oval(x - 3, y - 29, 10, 10, "yellow3")


def pedals(panel, x, y):
    draw_outer_pedals(panel, x, y)
    draw_inner_pedals(panel, x, y)


def flower(panel, x):
    draw_stalk(panel, x, PANEL_HEIGHT)
    draw_leaves_left(panel, x, PANEL_HEIGHT - 10)
    draw_stalk(panel, x, PANEL_HEIGHT - 10)
    draw_leaves_right(panel, x, PANEL_HEIGHT - 20)
    draw_stalk(panel, x, PANEL_HEIGHT - 20)
    draw_leaves_left(panel, x, PANEL_HEIGHT - 30)
    draw_stalk(panel, x, PANEL_HEIGHT - 30)
    draw_stalk(panel, x, PANEL_HEIGHT - 40)
    draw_outer_pedals(panel, x, PANEL_HEIGHT - 50)
    draw_inner_pedals(panel, x, PANEL_HEIGHT - 50)


def main():
   # steps = int(input("How many steps have you walked? "))
    panel = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT, "CadetBlue")
    oval(panel)
    rectangle(panel)
    triangle(panel)
    flower(panel, 250)


main()
