import pygame as pg
from Map.GameMap import GameMap
from Game.Screens import StatsScreen
from Game.Sprites import Player

class GameLoop:
    """
    This class represents the game loop
    """
    def __init__(self, screen, displayWidth, displayHeight):
        """
        Constructor for the GameLoop class
        :param screen: the pygame surface where objects will be drawn
        :param displayWidth: width of the screen
        :param displayHeight: height of the screen
        """
        self.screen = screen
        self.firstBuild = False
        self.gameMap = GameMap()
        self.statsScreen = StatsScreen(self.screen)
        self.background = pg.image.load("Resources/Grass.png").convert()

        self.allCharacters = pg.sprite.Group()  # TODO: add enemies to this sprite group
        self.allEnemies = pg.sprite.Group() # TODO: add enemies to this sprite group
        self.allBombs = pg.sprite.Group()
        self.allPowerUps = pg.sprite.Group()

        self.player = Player(displayWidth, displayHeight)
        # TODO: create enemies

        self.allCharacters.add(self.player)
        self.allBombs.add(self.player.bomb)

    def run(self):
        if not self.firstBuild:  # Initializes the map and draws it
            self.gameMap.run(self.screen)
            self.firstBuild = True

        self.screen.blit(self.background, (0,0))

        keys = pg.key.get_pressed()
        self.player.update(keys, self.gameMap.walls, self.gameMap.fakeWalls, self.allPowerUps)
        #TODO: self.allEnemies.update(self.gameMap.walls, self.gameMap.fakeWalls, self.allPowerUps)
        self.allCharacters.draw(self.screen)

        for character in self.allCharacters.sprites():
            pickedUp = pg.sprite.spritecollide(character, self.allPowerUps, True)  # Picking up power-ups
            for powerUp in pickedUp:
                powerUp.assignPowerUp(character)
            if character.placedBomb:
                if character.bomb.time > 0:
                    character.bomb.update()
                    character.bomb.draw(self.screen)
                if character.bomb.time == 0:
                    character.placedBomb = False
                    character.bomb.explode(self.gameMap.fakeWalls, self.allCharacters, self.gameMap.backMatrix, self.allPowerUps)
                    character.bomb.resetTime()

        self.gameMap.drawMap(self.screen)
        self.statsScreen.draw(self.player.lives, self.player.shield)
        self.allPowerUps.draw(self.screen)

        if self.player.lives == 0:
            return 1
        else:
            return 0
