from Game.Interface import *

class Menu:
    """
    Represents the menu screen
    """
    def __init__(self, screen):
        """
        Constructor of the Menu class
        :param screen: The pygame surface where objects will be drawn
        """
        self.screen = screen
        self.clicked = False  # Boolean that states if the button on the menu screen was clicked or not


    def draw(self):
        """
        Draws text and a button on the screen
        :return: null
        """
        title = Text(self.screen, "BomberTEC", 730, 250, (68, 0, 204), 100)
        title.drawText()

        button = Button(self.screen, "Start game", 640, 350, 200, 45, (255, 51, 85), (255, 102, 128))
        button.drawButton()

        if button.drawButton() == 1:
            self.clicked = True

class StatsScreen:
    """
    Class that represents the stats screen
    """
    def __init__(self, screen):
        """
        Constructor for the StatsScreen class
        :param screen: pygame surface where the objects will be drawn
        """
        self.screen = screen
        self.surf = pg.Surface((200, 720))
        self.surf.fill((157, 105, 163))

    def draw(self, playerLives, shield):
        """
        Draws all of the objects of the stats screen
        :param playerLives: the number of lives the player has
        :param shield: boolean that states if the player has an active shield power-up
        :return: null
        """
        self.screen.blit(self.surf, (1280,0))
        livesText = Text(self.screen, "Lives: %s" % playerLives, 1370, 50, (0, 0, 0), 25)
        livesText.drawText()

        powerUpsText = Text(self.screen, "Power-Ups:", 1370, 200, (0, 0, 0), 25)
        powerUpsText.drawText()

        pinkRect = pg.Rect(1300, 250, 30, 30)
        blueRect = pg.Rect(1300, 300, 30, 30)
        orangeRect = pg.Rect(1300, 350, 30, 30)
        brownRect = pg.Rect(1300, 410, 30, 30)

        pg.draw.rect(self.screen, (255,102,229), pinkRect)
        pg.draw.rect(self.screen, (25,64,255), blueRect)
        pg.draw.rect(self.screen, (255,140,25), orangeRect)
        pg.draw.rect(self.screen, (102, 68, 0), brownRect)

        oneUpText = Text(self.screen, "Life +1", 1380, 267, (0, 0, 0), 25)
        oneUpText.drawText()

        if shield:
            shieldFill = "yes"
        else:
            shieldFill = "no"

        shieldText = Text(self.screen, "Shield: %s" % shieldFill, 1405, 316, (0, 0, 0), 25)
        shieldText.drawText()
        crossText = Text(self.screen, "Cross-Bomb:", 1400, 365, (0, 0, 0), 21)
        crossText.drawText()
        crossActiveText = Text(self.screen, "No", 1390, 390, (0, 0, 0), 25)
        crossActiveText.drawText()
        crossText = Text(self.screen, "Shoe: no", 1390, 428, (0, 0, 0), 25)
        crossText.drawText()

class GameOver:
    """
    Represents the game over screen
    """

    def __init__(self, screen):
        """
        Constructor of the GameOver class
        :param screen: The pygame surface where objects will be drawn
        """
        self.screen = screen
        self.clicked = False

    def draw(self):
        """
        Draws text and a button on the screen
        :return: null
        """
        self.screen.fill((187, 153, 255))

        title = Text(self.screen, "Game Over", 730, 250, (68, 0, 204), 100)
        title.drawText()

        button = Button(self.screen, "Play again", 640, 350, 200, 45, (255, 51, 85), (255, 102, 128))
        button.drawButton()

        if button.drawButton() == 1:
            self.clicked = True