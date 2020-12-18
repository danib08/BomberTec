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
        self.surf.fill((102, 51, 0))

        # Setting the sprite sheet
        self.spriteSheet = pg.image.load("Resources/PowerUps.png").convert()

        # Life +1
        self.spriteSheet.set_clip(20, 80, 30, 29)
        self.lifeImage = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.lifeImage = pg.transform.scale(self.lifeImage, (30, 30))
        self.lifeImage.set_colorkey((0, 0, 0))

        # Shield
        self.spriteSheet.set_clip(115, 80, 29, 29)
        self.shieldImage = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.shieldImage = pg.transform.scale(self.shieldImage, (30, 30))
        self.shieldImage.set_colorkey((0, 0, 0))

        # Cross-Bomb
        self.spriteSheet.set_clip(212, 80, 29, 29)
        self.crossImage = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.crossImage = pg.transform.scale(self.crossImage, (30, 30))
        self.crossImage.set_colorkey((0, 0, 0))

        # Kick
        self.spriteSheet.set_clip(179, 80, 29, 29)
        self.kickImage = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.kickImage = pg.transform.scale(self.kickImage, (30, 30))
        self.kickImage.set_colorkey((0, 0, 0))


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

        self.screen.blit(self.lifeImage, (1300, 250))
        self.screen.blit(self.shieldImage, (1300, 300))
        self.screen.blit(self.crossImage, (1300, 350))
        self.screen.blit(self.kickImage, (1300, 410))

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
        crossText = Text(self.screen, "Kick: no", 1390, 428, (0, 0, 0), 25)
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
        self.text = ""

    def draw(self):
        """
        Draws text and a button on the screen
        :return: null
        """
        self.screen.fill((187, 153, 255))

        title = Text(self.screen, self.text, 730, 250, (68, 0, 204), 100)
        title.drawText()

        button = Button(self.screen, "Play again", 640, 350, 200, 45, (255, 51, 85), (255, 102, 128))
        button.drawButton()

        if button.drawButton() == 1:
            self.clicked = True