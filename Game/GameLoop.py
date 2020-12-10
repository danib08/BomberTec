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
        self.player = Player(displayWidth, displayHeight)
        # TODO: create enemies

        self.allCharacters = pg.sprite.Group()  # TODO: add enemies to this sprite group
        self.allBombs = pg.sprite.Group()

        self.allCharacters.add(self.player)
        self.allBombs.add(self.player.bomb)

    def run(self):
        if not self.firstBuild:  # Initializes the map and draws it
            self.gameMap.test(self.screen)
            self.firstBuild = True

        self.screen.fill((0, 153, 77))

        keys = pg.key.get_pressed()
        self.player.update(keys, self.gameMap.walls, self.gameMap.fakeWalls)
        self.allCharacters.draw(self.screen)

        for character in self.allCharacters.sprites():
            if character.placedBomb:
                if character.bomb.time > 0:
                    character.bomb.update()
                    character.bomb.draw(self.screen)
                if character.bomb.time == 0:
                    character.placedBomb = False
                    character.bomb.explode(self.gameMap.fakeWalls, self.allCharacters, self.gameMap.mapMatrix)
                    character.bomb.resetTime()

        self.gameMap.drawMap(self.screen)
        self.statsScreen.draw(self.player.lives)

        if self.player.lives == 0:
            return 1
        else:
            return 0
