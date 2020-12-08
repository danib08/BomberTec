import pygame as pg
from Game.Interface import *

pg.init()

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.clicked = False


    def draw(self):
        title = Text(self.surface, "BomberTEC", 630, 250, (68, 0, 204), 100)
        title.drawText()

        button = Button(self.surface, "Start game", 540, 350, 200, 45, (255, 51, 85), (255, 102, 128))
        button.drawButton()

        if button.drawButton() == 1:
            self.clicked = True