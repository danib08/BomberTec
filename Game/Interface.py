import pygame as pg

class Text:
    def __init__(self, surface, text, x, y, color, size):
        self.winSurface = surface
        self.x = x
        self.y = y
        self.font = pg.font.Font('freesansbold.ttf', size)
        self.textSurface = self.font.render(text, True, color)
        self.textRect = self.textSurface.get_rect()

    def drawText(self):
        self.textRect.center = (self.x, self.y)
        self.winSurface.blit(self.textSurface, self.textRect)
