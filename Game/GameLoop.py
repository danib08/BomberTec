import pygame as pg
from Map.GameMap import GameMap
from Game.Screens import StatsScreen
from Game.Sprites import Player
from Game.Sprites import Enemy
from GeneticAlgorithm.Genetic import Genetic
import random

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
        self.background = pg.image.load("Resources/Grass.jpg").convert()
        self.counter = 0
        self.nFrames = 700
        self.mFrames = 300

        self.allCharacters = pg.sprite.Group()
        self.allEnemies = pg.sprite.Group()
        self.allBombs = pg.sprite.Group()
        self.allPowerUps = pg.sprite.Group()

        self.player = Player(displayWidth, displayHeight)

        self.allCharacters.add(self.player)
        self.allBombs.add(self.player.bomb)

        self.genetic = Genetic([], 7)  # Genetic algorithm
        self.genetic.generateFP()

        for character in self.genetic.characteres:
            lives = random.randint(2, 4)
            speed = random.randint(4, 6)
            enemy = Enemy(displayWidth, displayHeight, lives, speed, character.id)  # TODO: add DNA probabilities
            self.allEnemies.add(enemy)
            self.allCharacters.add(enemy)

    def run(self):
        if not self.firstBuild:  # Initializes the map and draws it
            self.gameMap.run(self.screen)
            self.firstBuild = True

        self.screen.blit(self.background, (0,0))
        self.gameMap.drawMap(self.screen)

        keys = pg.key.get_pressed()
        self.player.update(keys, self.gameMap.walls, self.gameMap.fakeWalls, self.allPowerUps)
        #TODO: self.allEnemies.update(self.gameMap.walls, self.gameMap.fakeWalls, self.allPowerUps)
        self.allCharacters.draw(self.screen)

        for character in self.allCharacters.sprites():
            pickedUp = pg.sprite.spritecollide(character, self.allPowerUps, True)  # Picking up power-ups
            for powerUp in pickedUp:
                powerUp.assignPowerUp(character)
            if character.placedBomb:
                if character.bomb.time > 500:
                    character.bomb.update()
                    character.bomb.draw(self.screen)
                if 0 <= character.bomb.time <= 500:
                    character.placedBomb = False
                    character.bomb.explode(self.gameMap.fakeWalls, self.allCharacters, self.gameMap.backMatrix,
                                           self.allPowerUps, character.cross)
                    character.bomb.drawFlames(self.screen, character.cross)
                    character.bomb.resetTime()

        self.statsScreen.draw(self.player.lives, self.player.shield)
        self.allPowerUps.draw(self.screen)

        self.counter += 1

        if self.counter == self.mFrames:
            #TODO for enemy in allEnemies, .doAction()
            pass

        elif self.counter == self.nFrames:
            #TODO genetic again
            self.counter = 0
            pass

        if self.player.lives == 0:
            return 1
        else:
            return 0
