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
        self.nFrames = 10000
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

            # Enemies are created
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

        # Sprites are updated
        keys = pg.key.get_pressed()
        self.player.update(keys, self.gameMap.walls, self.gameMap.fakeWalls)
        self.allEnemies.update(self.gameMap.allWalls)
        self.allCharacters.draw(self.screen)

        for character in self.allCharacters.sprites():
            pickedUp = pg.sprite.spritecollide(character, self.allPowerUps, True)  # Picking up power-ups
            for powerUp in pickedUp:
                powerUp.assignPowerUp(character)
            if character.placedBomb:    # Managing bombs
                if character.bomb.time > 500:
                    character.bomb.update()
                    character.bomb.draw(self.screen)
                if 0 <= character.bomb.time <= 500:
                    character.placedBomb = False
                    character.bomb.explode(self.gameMap.fakeWalls, self.allCharacters, self.gameMap.mapMatrix,
                                           self.allPowerUps, self.gameMap.allWalls)
                    character.bomb.drawFlames(self.screen, character.cross)
                    character.bomb.resetTime()

        self.allPowerUps.draw(self.screen)  # Power ups are drawn
        self.statsScreen.draw(self.player.lives, self.player.shield) # Stats are updated

        if self.counter % self.mFrames == 0 or (self.firstBuild and self.counter == 5):
            for enemy in self.allEnemies:
                enemy.doAction(self.gameMap.allWalls, self.allPowerUps, self.gameMap.mapMatrix) # Enemies do their actions

        elif self.counter == self.nFrames:  # Starts new genetic generation
            for i in range(0, len(self.allEnemies.sprites())):
                self.genetic.characteres[i].blockRecord = self.allEnemies.sprites()[i].blockRecord
                self.genetic.characteres[i].enemiesRecord = self.allEnemies.sprites()[i].enemiesRecord

            self.genetic.fitness()
            self.genetic.selection()
            self.genetic.crossOver(4)
            self.genetic.mutation(40)

            for i in range(0, len(self.allEnemies.sprites())):
                self.allEnemies.sprites()[i] = self.genetic.characteres[i]
                self.allEnemies.sprites()[i].setProb()

            self.counter = 0

        self.counter += 1

        if self.player.lives == 0:
            return 1
        elif self.player.lives > 0 and len(self.allEnemies.sprites()) == 0:
            return 2
        else:
            return 0
