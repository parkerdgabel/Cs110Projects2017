# CSC 110, Autumn 2017
# Provided main for Project 9 - Tiles

# Use this program to test your tile_manager code.
# You will need to place it in the same directory as
# DrawingPanel.py and tile_manager.py.

# DO NOT ALTER THIS FILE

from DrawingPanel import *
from tile_manager import *

def main():
    p.window.bind("<Button-1>", raises)
    p.window.bind("<Button-3>", lower)
    p.window.bind("<Button-2>", lower)
    p.window.bind("<Shift-Button-1>", delete)
    p.window.bind("<Shift-Button-3>", delete_all)
    p.window.bind("<Shift-Button-2>", delete_all)
    p.window.bind("<s>", shuffle)
    p.window.bind("<n>", add)
    add_all()
    draw_all()

main()
