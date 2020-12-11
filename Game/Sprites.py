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
        self.bomb = Bomb(screenHeight, screenHeight)  # Creates a bomb sprite
        self.placedBomb = False


    def update(self, keys, blocks, fakeBlocks, powerUps):
        """
        Updates the player according to the keys pressed and detected collisions.
        :param keys: A list of all the keys pressed per frame
        :param blocks: A list of pygame Rects that represent walls
        :param fakeBlocks: A list of pygame Rects that represent fake walls
        :param powerUps: List of powerUps on the map
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
        self.speed = random.randint(4, 6)
        self.evade = random.randint(7,9)
        self.bomb = Bomb(screenHeight, screenHeight)  # Creates a bomb sprite
        self.placedBomb = False

        self.id = charId
        self.DNA = dna
        self.hideProb = self.DNA[0]
        self.powerProb = self.DNA[1]
        self.enemyProb = self.DNA[2]
        self.bombProb = self.DNA[3]
        self.inAction = False

        self.aStar = AStar()
        self.path = []  # Path the enemy is following


    def update(self, blocks, fakeBlocks, powerUps):
        # TODO: update enemy movement, right/left/up/down += self.speed
        if len(self.path) == 0:
            self.inAction = False
        # else:


        # Keep enemy on-screen
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

    #TODO: document
    def doAction(self, allWalls, mapMatrix):
        if not self.inAction:
            i = 0
            j = 0
            for rect in allWalls:
                if rect.colliderect(self.rect):
                    i = rect.i
                    j = rect.j
            action = random.choices(self.DNA, weights=(self.DNA[0], self.DNA[1], self.DNA[2], self.DNA[3]), k=1)
            if action[0] == self.hideProb:
                # print("hide")
                #TODO: A*
                pass
            elif action[0] == self.powerProb:
                # print("pow")
                #TODO: A*
                pass
            elif action[0] == self.enemyProb:
                # print("enemy")
                #TODO: A*
                pass
            elif action[0] == self.bombProb:
                self.placeBomb()
                self.runAway(i, j, mapMatrix)
                pass
            self.inAction = True

    #TODO: document
    def runAway(self, i, j, mapMatrix):
        onLeftBorder = False
        onTopBorder = False
        onRightBorder = False
        onBottomBorder = False
        moveFlag = True
        start = (i,j)
        end = (0,0)

        if i == 0:
            onTopBorder = True
        if j == 0:
            onLeftBorder = True
        if i == 17:
            onBottomBorder = True
        if j == 31:
            onRightBorder = True

        if onLeftBorder and onBottomBorder:
            end = (16,1)
        elif onLeftBorder and onTopBorder:
            end = (1,1)
        elif onRightBorder and onBottomBorder:
            end = (16,30)
        elif onRightBorder and onTopBorder:
            end = (1,30)
        elif onLeftBorder:
            if mapMatrix[i-1][j+1] == 0:
                end = (i-1,j+1)
            elif mapMatrix[i+1][j+1] == 0:
                end = (i+1,j+1)
            else:
                moveFlag = False
        elif onRightBorder:
            if mapMatrix[i-1][j-1] == 0:
                end = (i-1,j-1)
            elif mapMatrix[i+1][j-1] == 0:
                end = (i+1,j-1)
            else:
                moveFlag = False
        elif onTopBorder:
            if mapMatrix[i+1][j-1] == 0:
                end = (i+1,j-1)
            elif mapMatrix[i+1][j+1] == 0:
                end = (i+1,j+1)
            else:
                moveFlag = False
        elif onBottomBorder:
            if mapMatrix[i-1][j+1] == 0:
                end = (i-1,j+1)
            elif mapMatrix[i-1][j-1] == 0:
                end = (i-1,j-1)
            else:
                moveFlag = False
        else:
            if mapMatrix[i+1][j-1] == 0:
                end = (i+1,j-1)
            elif mapMatrix[i+1][j+1] == 0:
                end = (i+1,j+1)
            elif mapMatrix[i - 1][j + 1] == 0:
                end = (i - 1, j + 1)
            elif mapMatrix[i - 1][j - 1] == 0:
                end = (i - 1, j - 1)
            else:
                moveFlag = False

        if moveFlag:
            self.path = self.aStar.getPath(mapMatrix, start, end)
            print(self.path)
        else:
            self.inAction = False