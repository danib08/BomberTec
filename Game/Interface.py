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

class Button:
    def __init__(self, surface, text, x, y, w, h, color, colorHover):
        self.winSurface = surface
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.colorHover = colorHover

    def drawButton(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.w and self.y < mouse[1] < self.y + self.h:
            pg.draw.rect(self.winSurface, self.colorHover, (self.x, self.y, self.w, self.h))
            if click[0] == 1:
                return 1
        else:
            pg.draw.rect(self.winSurface, self.color, (self.x, self.y, self.w, self.h))

        text = Text(self.winSurface, self.text, self.x + self.w / 2, self.y + self.h / 2, (0, 0, 0), 20)
        text.drawText()