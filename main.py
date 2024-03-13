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

        #setting up the fps
        self.fps = 30

    def game_window(self):
        #initializing the pygame window
        pg.init()

        # constant used to track the time
        CLOCK = pg.time.Clock()

        #build infrastructure of the display
        screen = pg.display.set_mode((self.width, self.height + 100), 0, 32)

        #nametag for the game window
        pg.display.set_caption("Try not to suck at Tic Tac Toe")

        #loading the images as obj
        initiating_window = pg.image.load("modified_cover.png")
        x_img = pg.image.load("X_modified.png")
        y_img = pg.image.load("o_modified.png")

        #resizing images
        initiating_window = pg.transform.scale(initiating_window, (self.width, self.height +100))
        x_img = pg.transform.scale(x_img, (80, 80))
        o_img = pg.transform.scale(o_img, (80, 80))



