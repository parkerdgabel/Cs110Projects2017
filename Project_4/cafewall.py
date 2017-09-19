# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #4, 09/13/17
#
# This program's behavior is to show various representations
# the Cafewall effect.
from drawingpanel import *

PANEL_HEIGHT = 400
PANEL_WIDTH = 650
PANEL_COLOR = "gray"
MORTAR = 2


def main():
    panel = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT, PANEL_COLOR)
    upper_left(panel)
    mid_left(panel)
    lower_left(panel)
    lower_middle(panel)
    lower_right(panel)
    upper_right(panel)


def upper_left(panel):
    """Prints the upper left effect."""
    x, y, pairs, size = 0, 0, 4, 20
    draw_row(x, y, size, pairs, panel)


def mid_left(panel):
    """Prints the mid left panel."""
    x, y, size, pairs = 50, 70, 30, 5
    draw_row(x, y, size, pairs, panel)


def lower_left(panel):
    """Prints the lower left effect."""
    x, y, size, pairs, offset, cols = 10, 150, 25, 4, 0, 4
    draw_columns(x, y, size, pairs, offset, cols, panel)


def lower_middle(panel):
    """Prints the lower middle effect."""
    x, y, size, pairs, offset, cols = 250, 200, 25, 3, 10, 3
    draw_columns(x, y, size, pairs, offset, cols, panel)


def lower_right(panel):
    """Prints the lower right effect."""
    x, y, size, pairs, offset, cols = 425, 180, 20, 5, 10, 5
    draw_columns(x, y, size, pairs, offset, cols, panel)


def upper_right(panel):
    """Prints the upper right effect."""
    x, y, size, pairs, offset, cols = 400, 20, 35, 2, 35, 2
    draw_columns(x, y, size, pairs, offset, cols, panel)


def draw_black_square(x, y, size, panel):
    """Draws the black square.
        Parameters: x              int: x-location on drawing panel
                    y              int: y-location on drawing panel
                    size           int: size of squares
                    panel DrawingPanel: the panel."""
    panel.fill_rect(x, y, size, size, "black")
    panel.draw_line(x, y, x + size, y + size, "blue")
    panel.draw_line(x, y + size, x + size, y, "blue")


def draw_white_square(x, y, size, panel):
    """Draws the white square.
        Parameters: x              int: x-location on drawing panel
                    y              int: y-location on drawing panel
                    size           int: size of squares
                    panel DrawingPanel: the panel.
    """
    panel.fill_rect(x, y, size, size, "white")


def draw_pair_squares(x, y, size, panel):
    """Draws a pair of squares.
        Parameters: x              int: x-location on drawing panel
                    y              int: y-location on drawing panel
                    size           int: size of squares
                    panel DrawingPanel: the panel."""
    draw_black_square(x, y, size, panel)
    draw_white_square(x + size, y, size, panel)


def draw_row(x, y, size, pairs, panel):
    """Draws a row of pairs.
        Parameters: x              int: x-location on drawing panel
                    y              int: y-location on drawing panel
                    size           int: size of squares
                    pairs          int: number of pairs of squares.
                    panel DrawingPanel: the panel."""
    for i in range(pairs):
        draw_pair_squares(x, y, size, panel)
        x += (2 * size)


def draw_two_rows(x, y, size, pairs, offset, panel):
    """Draws two rows with an offset.
        Parameters: x              int: x-location on drawing panel
                    y              int: y-location on drawing panel
                    size           int: size of squares
                    pairs          int: number of pairs of squares.
                    offset         int: sets the offset for the rows
                    panel DrawingPanel: the panel."""
    draw_row(x, y, size, pairs, panel)
    draw_row(x + offset, y + size + MORTAR, size, pairs, panel)


def draw_columns(x, y, size, pairs, offset, cols, panel):
    """Draws colums of rows.
        Parameters: x              int: x-location on drawing panel
                    y              int: y-location on drawing panel
                    size           int: size of squares
                    pairs          int: number of pairs of squares.
                    offset         int: sets the offset for the rows
                    cols           int: sets the number of columns
                    panel DrawingPanel: the panel."""
    for i in range(cols):
        y_pos = y + (i * (size * 2))
        draw_two_rows(x, y_pos,
                      size, pairs, offset, panel)
        y += MORTAR * 2


main()
