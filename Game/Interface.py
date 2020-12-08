import pygame as pg

class Text:
    """
    Class that represents a text object
    """
    def __init__(self, surface, text, x, y, color, size):
        """
        Constructor of the Text class
        :param surface: The pygame surface where the text will be displayed
        :param text: The text shown on screen
        :param x: The x coordinate of the text center
        :param y: The y coordinate of the text center
        :param color: The text color in rgb notation
        :param size: The text size
        """
        self.winSurface = surface
        self.x = x
        self.y = y
        self.font = pg.font.Font('freesansbold.ttf', size)
        self.textSurface = self.font.render(text, True, color)
        self.textRect = self.textSurface.get_rect()

    def drawText(self):
        """
        Draws the text on scren
        :return: null
        """
        self.textRect.center = (self.x, self.y)
        self.winSurface.blit(self.textSurface, self.textRect)

class Button:
    """
    Class that represents a button
    """
    def __init__(self, surface, text, x, y, w, h, color, colorHover):
        """
        Constructor for the Button class
        :param surface: The pygame surface where the text will be displayed
        :param text: The text shown on screen
        :param x: The x coordinate of the button
        :param y: The y coordinate of the button
        :param w: The weight of the button
        :param h: The height of the button
        :param color: The color of the button
        :param colorHover: The color of the button when the mouse hovers over it
        """
        self.winSurface = surface
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.colorHover = colorHover

    def drawButton(self):
        """
        Draws the button on-screen
        :return: 1 if the button is clicked
        """
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