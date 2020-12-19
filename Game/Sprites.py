import pygame as pg
import random
from Game.Bombs import Bomb
from Map.AStarAlgorithm import AStar

class Player(pg.sprite.Sprite):
    """
    Class that represents a player.
    Extends from the pygame Sprite class.
    """
    def __init__(self, screenWidth, screenHeight):
        """
        Constructor for the player.
        :param screenWidth: The screen width that will be the player's x coordinate limit
        :param screenHeight: The screen height that will be the player's y coordinate limit
        """
        super().__init__()
        self.screenW = screenWidth   # Screen dimensions
        self.screenH = screenHeight
        self.image = pg.Surface((35,35))  # Player's surface dimensions
        self.image.fill((25,217,255))
        self.rect = self.image.get_rect()  # Fetch the rectangle object that has the dimensions of the image

        self.lives = 3
        self.shield = False
        self.cross = False
        self.id = 10
        self.bomb = Bomb(screenHeight, screenHeight, 10, self)  # Creates a bomb sprite
        self.placedBomb = False
        self.isPlayer = True

    def update(self, keys, blocks, fakeBlocks):
        """
        Updates the player according to the keys pressed and detected collisions.
        :param keys: A list of all the keys pressed per frame
        :param blocks: A list of pygame Rects that represent walls
        :param fakeBlocks: A list of pygame Rects that represent fake walls
        :return: null
        """
        if keys[pg.K_w]:
            self.rect.move_ip(0,-5)
            if self.rect.collidelist(blocks) != -1 or self.rect.collidelist(fakeBlocks) != -1: # Detects collision
                self.rect.move_ip(0,5) # Keeps the player from overlapping with walls
        if keys[pg.K_a]:
            self.rect.move_ip(-5, 0)
            if self.rect.collidelist(blocks) != -1 or self.rect.collidelist(fakeBlocks) != -1:
                self.rect.move_ip(5,0)
        if keys[pg.K_s]:
            self.rect.move_ip(0, 5)
            if self.rect.collidelist(blocks) != -1 or self.rect.collidelist(fakeBlocks) != -1:
                self.rect.move_ip(0, -5)
        if keys[pg.K_d]:
            self.rect.move_ip(5,0)
            if self.rect.collidelist(blocks) != -1 or self.rect.collidelist(fakeBlocks) != -1:
                self.rect.move_ip(-5,0)

        # Keep player on-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screenW:
            self.rect.right = self.screenW
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screenH:
            self.rect.bottom = self.screenH

    def placeBomb(self):
        """
        Places a bomb on the screen
        :return: null
        """
        self.bomb.setCoord(self.rect.centerx, self.rect.centery)
        self.bomb.resetTime()
        self.placedBomb = True

class Enemy(pg.sprite.Sprite):
    """
    Class that represents an enemy.
    Extends from the pygame Sprite class.
    """

    def __init__(self, screenWidth, screenHeight, charId, dna):
        """
        Constructor for the player.
        :param screenWidth: The screen width that will be the player's x coordinate limit
        :param screenHeight: The screen height that will be the player's y coordinate limit
        :param charId: an id to link the sprite to a genetic algorithm character
        :param dna: the genes of the character
        """
        super().__init__()
        self.screenW = screenWidth  # Screen dimensions
        self.screenH = screenHeight
        self.image = pg.Surface((35, 35))  # Player's surface dimensions
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()  # Fetch the rectangle object that has the dimensions of the image

        self.lives = random.randint(2, 4)
        self.shield = False
        self.cross = False
        self.speed = random.randint(0, 2)
        self.evade = random.randint(7,9)
        self.bomb = Bomb(screenHeight, screenHeight, charId, self)  # Creates a bomb sprite
        self.placedBomb = False

        self.id = charId
        self.DNA = dna
        self.hideProb = self.DNA[0]
        self.powerProb = self.DNA[1]
        self.enemyProb = self.DNA[2]
        self.bombProb = self.DNA[3]
        self.enemiesRecord = []
        self.blockRecord = []

        self.inAction = False
        self.aStar = AStar()
        self.path = []  # Path the enemy is following
        self.nextNode = (0,0)
        self.nextRect = None
        self.i = 0
        self.j = 0
        self.isPlayer = False

    def setProb(self):
        self.hideProb = self.DNA[0]
        self.powerProb = self.DNA[1]
        self.enemyProb = self.DNA[2]
        self.bombProb = self.DNA[3]

    def update(self, allWalls):
        """
        Moves the character
        :param allWalls: all of the walls on the game
        :return: null
        """
        pass
        if len(self.path) == 0:
            self.inAction = False
        else:
            if self.i < self.nextNode[0]:
                self.rect.centery += self.speed
            elif self.i > self.nextNode[0]:
                self.rect.centery -= self.speed
            if self.j < self.nextNode[1]:
                self.rect.centerx += self.speed
            elif self.j > self.nextNode[1]:
                self.rect.centerx -= self.speed

            if self.nextRect.centerx - 3 <= self.rect.centerx <= self.nextRect.centerx + 3 and \
                    self.nextRect.centery - 3 <= self.rect.centery <= self.nextRect.centery + 3:
                self.path.pop(0)
                if len(self.path) == 0:
                    self.inAction = False
                else:
                    self.nextNode = self.path[0]
                    for rect in allWalls:
                        if rect.i == self.nextNode[0] and rect.j == self.nextNode[1]:
                            self.nextRect = rect
                            break

        # Keep enemy on-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screenW:
            self.rect.right = self.screenW
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screenH:
            self.rect.bottom = self.screenH

    def doAction(self, allWalls, powerUps, mapMatrix, allCharacters):
        """
        Triggers an action of the enemy
        :param allWalls: list of all walls on the map
        :param powerUps: list of power up sprites
        :param mapMatrix: matrix that represents the game map
        :param allCharacters: list of all sprites of players in the game
        :return: null
        """
        if not self.inAction:
            for rect in allWalls:
                if rect.colliderect(self.rect):
                    self.i = rect.i
                    self.j = rect.j
                    break

            action = random.choices(self.DNA, weights=(self.DNA[0], self.DNA[1], self.DNA[2], self.DNA[3]), k=1)
            if action[0] == self.hideProb:
                pass
            elif action[0] == self.powerProb:
                self.searchPowerUp(powerUps, allWalls, mapMatrix)
                pass
            elif action[0] == self.enemyProb:
                self.searchEnemy(allCharacters, allWalls, mapMatrix)
                pass
            elif action[0] == self.bombProb:
                self.placeBomb()
            self.inAction = True

    def placeBomb(self):
        """
        Places a bomb on the screen
        :return: null
        """
        self.bomb.setCoord(self.rect.centerx, self.rect.centery)
        self.bomb.resetTime()
        self.placedBomb = True

    def searchPowerUp(self, powerUps, allWalls, mapMatrix):
        if len(powerUps) != 0:
            end = (0,0)
            powerUp = random.choice(powerUps.sprites())
            nextRect = None
            for wall in allWalls:
                if wall.colliderect(powerUp.rect):
                    end = (wall.i, wall.j)
                    nextRect = wall
                    break
            path = self.aStar.getPath(mapMatrix, (self.i,self.j), end)
            if path is not None:
                self.path = path
                self.nextRect = nextRect
                self.nextNode = path[0]
            else:
                self.inAction = True

        else:
            self.inAction = False

    def searchEnemy(self, allCharacters, allWalls, mapMatrix):
        pass
        # end = (0, 0)
        # enemy = random.choice(allCharacters.sprites())
        # while enemy == self:
        #     enemy = random.choice(allCharacters.sprites())
        # nextRect = None
        # for wall in allWalls:
        #     if wall.colliderect(enemy.rect):
        #         end = (wall.i, wall.j)
        #         nextRect = wall
        #         break
        # path = self.aStar.getPath(mapMatrix, (self.i, self.j), end)
        # if path is not None:
        #     self.path = path
        #     self.nextRect = nextRect
        #     self.nextNode = path[0]
        # else:
        #     self.inAction = True
