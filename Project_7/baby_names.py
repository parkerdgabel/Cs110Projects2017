# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #6, 10/17/17
# This program
from DrawingPanel import *

PANEL_WIDTH = 780
PANEL_HEIGHT = 560
STARTING_YEAR = 1890
DECADE_WIDTH = 60
BAR_WIDTH = DECADE_WIDTH / 2


def main():
    """Does all the things."""
    introduction()
    name = query_name()
    gender = query_gender()
    popularity = popularity_search(name, gender)
    if popularity == "":
        print(name, "not found.")
        return
    meaning = meaning_search(name, gender)
    print(popularity, end="")
    print(meaning)
    panel = panel_init()
    panel_draw_decades(popularity, panel)
    panel_draw_name_meaning(meaning, panel)
    panel_draw_bars(popularity, panel)


def introduction():
    """introduction presents the introduction to the program."""
    print("This program allows you to search through the")
    print("data from the Social Security Administration")
    print("to see how popular a particular name has been")
    print("since", STARTING_YEAR)
    print()


def panel_init():
    """initiates the panel"""
    panel = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT)
    panel.fill_rect(0, 0, PANEL_WIDTH, 30, "light gray")
    panel.draw_line(0, 30, PANEL_WIDTH, 30)
    panel.fill_rect(0, PANEL_HEIGHT - 30, PANEL_WIDTH, 30, "light gray")
    panel.draw_line(0, PANEL_HEIGHT - 30, PANEL_WIDTH, PANEL_HEIGHT - 30)
    return panel


def panel_draw_decades(popularity, panel):
    """Draws the decades at the bottom """
    popularity_split = popularity.split()
    year = STARTING_YEAR
    x = 0
    for i in range(len(popularity_split) - 2):
        panel.draw_string(year, x, PANEL_HEIGHT - 30)
        year += 10
        x += DECADE_WIDTH


def panel_draw_name_meaning(meaning, panel):
    """Simply draws the meaning at the top"""
    panel.draw_string(meaning, 0, 0)


def panel_draw_bars(popularity, panel):
    """Draws the bars on the panel."""
    bar_color = "yellow"
    x_start = 0
    popularity_split = popularity.split()
    if popularity_split[1] == 'm':
        bar_color = "green"
    for i in range(2, len(popularity_split)):
        elem = popularity_split[i]
        if int(elem) == 0:
            y = PANEL_HEIGHT - 30
            w = x_start + BAR_WIDTH
            h = PANEL_HEIGHT - 30
            panel.draw_line(x_start, y, w, h, bar_color)
            panel.draw_string(elem, x_start, PANEL_HEIGHT - 40)
        elif int(elem) == 1:
            y = 30
            panel.fill_rect(x_start, y, BAR_WIDTH,
                            (PANEL_HEIGHT - 30) - y, bar_color)
            panel.draw_string(elem, x_start, y - 10)

        else:
            num = int(elem)
            y = 30 + (num // 2)
            panel.fill_rect(x_start, y, BAR_WIDTH,
                            (PANEL_HEIGHT - 30) - y, bar_color)
            panel.draw_string(elem, x_start, y - 10)
        x_start += DECADE_WIDTH


def query_name():
    """Asks for a name from the user."""
    return input("Name: ")


def query_gender():
    """Asks the user for the gender."""
    return input("Gender: ")


def search(name, gender, file):
    """generic search function for the file."""
    if gender[0].lower() != 'm' and gender[0].lower() != 'f':
        return ""
    text = file.readlines()
    name_lower = name.lower()
    for line in text:
        line_split = line.lower().split()
        if line_split[0] == name_lower:
            if (line_split[0] == name_lower and line_split[1] == gender[0].lower()) or line_split[1] == 'mf':
                return line
    return ""


def popularity_search(name, gender):
    """searches popularity rankings"""
    return search(name, gender, open("names.txt"))


def meaning_search(name, gender):
    """searchs for meaning."""
    return search(name, gender, open("meanings.txt"))


main()
