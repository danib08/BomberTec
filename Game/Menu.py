import pygame as pg
from Game.Interface import *

pg.init()

class Menu:
    def __init__(self, width, height, surface):
        self.surf = pg.Surface((width, height))
        self.surf.fill((187,153,255))
        surface.blit(self.surf, (0, 0))
        title = Text(surface, "BomberTEC", 630, 250, (68,0,204), 100)
        title.drawText()

