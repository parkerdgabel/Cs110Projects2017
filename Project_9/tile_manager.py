# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #9, 11/06/17
# This program adds tiles to drawing panel.
import DrawingPanel
from random import randint

PANEL_HEIGHT = 600
PANEL_WIDTH = PANEL_HEIGHT * (1.75 / 1)
BEGINNING_TILES = 50
p = DrawingPanel.DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT)
tiles = []


def add_to_tiles():
    """add adds a tile of random width and height to the panel.
    Args: None
    Returns: None"""
    tile_width = randint(25, 61)
    tile_height = randint(25, 61)
    x = randint(0, PANEL_WIDTH - tile_width)
    y = randint(0, PANEL_HEIGHT - tile_height)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    tiles.append((x, y, tile_width, tile_height, color))


def add(event):
    add_to_tiles()
    draw(tiles[-1])


def add_all():
    """Adds tiles to tile list.
    Args: None
    Returns: None"""
    for _ in range(0, BEGINNING_TILES + 1):
        add_to_tiles()


def draw(tile):
    p.fill_rect(tile[0], tile[1], tile[2], tile[3], tile[4])


def draw_all():
    """Draws all tiles in tile list.
    Args: None
    Returns: None"""
    p.clear()
    for elem in tiles:
        draw(elem)


def raises(event):
    """Raises any tile touched by a left-click to the top of the list.
    Args: event
    Returns: None"""
    i = __find_tile_at_event(event)
    if i != -1:
        tiles.append(tiles[i])
        draw(tiles[-1])


def lower(event):
    """Raises any tile touched by a right-click to the bottom of the list.
    Args: event
    Returns: None"""
    i = __find_tile_at_event(event)
    if i != -1:
        tiles.insert(0, tiles.pop(i))
        draw(tiles[0])


def delete(event):
    """Deletes the topmost tile at an event
    Args: event
    Returns: None"""
    i = __find_tile_at_event(event)
    if i != -1:
        tiles.pop(i)
        draw_all()


def delete_all(event):
    done = False
    while not done:
        i = __find_tile_at_event(event)
        if i != -1:
            tiles.pop(i)
        else:
            done = True
    draw_all()


def shuffle(event):
    for i in range(0, len(tiles)):
        x = randint(0, PANEL_WIDTH - tiles[i][2])
        y = randint(0, PANEL_HEIGHT - tiles[i][3])
        elem = (x, y, tiles[i][2], tiles[i][3], tiles[i][4])
        tiles.pop(i)
        tiles.insert(i, elem)
    draw_all()


def __find_tile_at_event(event):
    """Helper function to find if a tile is at an Event
    Args: event
    Returns: i"""
    x_loc = event.x
    y_loc = event.y
    for i in range(len(tiles) - 1, -1, -1):
        if tiles[i][0] <= x_loc and x_loc <= tiles[i][0] + tiles[i][2]:
            if tiles[i][1] <= y_loc and y_loc <= tiles[i][1] + tiles[i][3]:
                return i
    return -1
