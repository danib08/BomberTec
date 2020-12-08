from Game.Interface import *

class Menu:
    """
    Represents the menu screen
    """
    def __init__(self, surface):
        """
        Constructor of the Menu class
        :param surface: The pygame surface where objects will be drawn
        """
        self.surface = surface
        self.clicked = False  # Boolean that states if the button on the menu screen was clicked or not


    def draw(self):
        """
        Draws text and a button on the screen
        :return: null
        """
        title = Text(self.surface, "BomberTEC", 630, 250, (68, 0, 204), 100)
        title.drawText()

        button = Button(self.surface, "Start game", 540, 350, 200, 45, (255, 51, 85), (255, 102, 128))
        button.drawButton()

        if button.drawButton() == 1:
            self.clicked = True