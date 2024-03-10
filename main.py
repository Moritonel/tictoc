import pygame as pg
import sys
import time
from pygame.locals import *


class Game:
    def __init__(self):
        # setting up needed values
        self.XO = "x"
        self.winner = None
        self.draw = None

        # setting up game window width, height, 
        # background color and color of the lines dviding board
        self.width = 400
        self.height = 400
        self.white = (255, 255, 255)
        self.line_color = (0, 0, 0)

        #setting up a 3 * 3 board in canvas
        self.board = [[None]*3, [None]*3, [None]*3]

