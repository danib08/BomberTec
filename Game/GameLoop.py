import pygame as pg
from Map.GameMap import GameMap
from Game.Screens import StatsScreen
from Game.Sprites import Player
from Game.Sprites import Enemy
from GeneticAlgorithm.Genetic import Genetic

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
        self.width = displayWidth
        self.height = displayHeight
        self.firstBuild = False
        self.gameMap = GameMap()
        self.statsScreen = StatsScreen(self.screen)
        self.background = pg.image.load("Resources/Grass.jpg").convert()
        self.counter = 0  # counter for the genetic algorithm frames
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

        self.enemyPositions = [(17,0), (0,31), (17,31), (9,0), (0,16), (17,16), (9,17)]
        self.enemyCoordinates = []

    def run(self):
        if not self.firstBuild:  # Initializes the map and draws it
            self.gameMap.run(self.screen)

            count = 0
            for rect in self.gameMap.allWalls:
                for pos in self.enemyPositions:
                    if rect.i == pos[0] and rect.j == pos[1]:
                        enemy = Enemy(self.width, self.height, self.genetic.characteres[count].id,
                                      self.genetic.characteres[count].DNA)
                        enemy.rect.center = rect.center
                        self.allEnemies.add(enemy)
                        self.allCharacters.add(enemy)
                        count += 1
            self.firstBuild = True

        self.screen.blit(self.background, (0,0))
        self.gameMap.drawMap(self.screen)

        keys = pg.key.get_pressed()
        self.player.update(keys, self.gameMap.walls, self.gameMap.fakeWalls, self.allPowerUps)
        self.allEnemies.update(self.gameMap.walls, self.gameMap.fakeWalls, self.allPowerUps, self.gameMap.allWalls)
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
                                           self.allPowerUps, character)
                    character.bomb.drawFlames(self.screen, character.cross)
                    character.bomb.resetTime()

        self.statsScreen.draw(self.player.lives, self.player.shield)
        self.allPowerUps.draw(self.screen)

        if self.counter == self.mFrames or (self.firstBuild and self.counter == 5):
            for enemy in self.allEnemies:
                enemy.doAction(self.gameMap.allWalls, self.gameMap.mapMatrix)

        elif self.counter == self.nFrames:
            self.genetic.characteres[0].blockRecord = self.allEnemies.sprites()[0].blockRecord
            self.genetic.characteres[0].enemiesRecord = self.allEnemies.sprites()[0].enemiesRecord
            self.genetic.characteres[1].blockRecord = self.allEnemies.sprites()[1].blockRecord
            self.genetic.characteres[1].enemiesRecord = self.allEnemies.sprites()[1].enemiesRecord
            self.genetic.characteres[2].blockRecord = self.allEnemies.sprites()[2].blockRecord
            self.genetic.characteres[2].enemiesRecord = self.allEnemies.sprites()[2].enemiesRecord
            self.genetic.characteres[3].blockRecord = self.allEnemies.sprites()[3].blockRecord
            self.genetic.characteres[3].enemiesRecord = self.allEnemies.sprites()[3].enemiesRecord
            self.genetic.characteres[4].blockRecord = self.allEnemies.sprites()[4].blockRecord
            self.genetic.characteres[4].enemiesRecord = self.allEnemies.sprites()[4].enemiesRecord
            self.genetic.characteres[5].blockRecord = self.allEnemies.sprites()[5].blockRecord
            self.genetic.characteres[5].enemiesRecord = self.allEnemies.sprites()[5].enemiesRecord
            self.genetic.characteres[6].blockRecord = self.allEnemies.sprites()[6].blockRecord
            self.genetic.characteres[6].enemiesRecord = self.allEnemies.sprites()[6].enemiesRecord

            self.genetic.fitness()
            self.genetic.selection()
            self.genetic.crossOver(4)
            self.genetic.mutation(40)

            self.genetic.characteres[0].DNA = self.allEnemies.sprites()[0].DNA
            self.genetic.characteres[1].DNA = self.allEnemies.sprites()[1].DNA
            self.genetic.characteres[2].DNA = self.allEnemies.sprites()[2].DNA
            self.genetic.characteres[3].DNA = self.allEnemies.sprites()[3].DNA
            self.genetic.characteres[4].DNA = self.allEnemies.sprites()[4].DNA
            self.genetic.characteres[5].DNA = self.allEnemies.sprites()[5].DNA
            self.genetic.characteres[6].DNA = self.allEnemies.sprites()[6].DNA

            for enemy in self.allEnemies.sprites():
                enemy.setProb()

            self.counter = 0

        self.counter += 1

        if self.player.lives == 0:
            return 1
        elif self.player.lives > 0 and len(self.allEnemies) == 0:
            return 2
            #TODO: you win (change game over text)
        else:
            return 0
