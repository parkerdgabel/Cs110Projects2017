
# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #4, 09/13/17
#
# This program's behavior is to show various representations
# the Cafewall effect.
from drawingpanel import *
PANEL_WIDTH = 600
PANEL_HEIGHT = 400


def main():
    panel = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT, "DarkOrchid")
    animate_taxi(0, PANEL_HEIGHT, panel)


def taxi(x, y, panel):
    """Taxi draws a taxi on screen."""
    panel.fill_rect(x + 20, y - 70, 40, 25, "yellow")
    panel.fill_rect(x + 40, y - 68,  20, 20, "gray")
    panel.fill_rect(x, y - 40, 80, 25, "yellow")
    panel.fill_rect(x, y - 30, 80, 10, "black")
    panel.fill_rect(x, y - 20, 80, 10, "yellow")
    panel.fill_oval(x + 5, y - 20, 20, 20)
    panel.fill_oval(x + 55, y - 20, 20, 20)


def animate_taxi(x, y, panel):
    """animate_taxi animates the taxi"""
    for i in range(100):
        panel.clear()
        taxi(x, y, panel)
        x += 5
        panel.sleep(15)


main()
