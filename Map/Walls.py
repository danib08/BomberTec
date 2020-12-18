import pygame as pg

class Wall(pg.Rect):
    """
    Class that represents a wall
    Extends from the pygame Rect class.
    """
    def __init__(self, left, top, width, height, i, j):
        """
        Constructor for the wall
        :param left: left side coordinate
        :param top: top side coordinate
        :param width: rectangle width
        :param height: rectangle height
        :param i: map matrix i position
        :param j: map matrix j position
        """
        super().__init__(left, top, width, height)
        self.i = i
        self.j = j
        self.image = pg.image.load("Resources/ExplodableBlock.png").convert()
        self.image = pg.transform.scale(self.image, (40, 40))
