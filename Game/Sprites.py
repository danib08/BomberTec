import pygame as pg
import random
from Game.Bombs import Bomb

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


    def update(self, blocks, fakeBlocks):
        # TODO: update enemy movement, right/left/up/down += self.speed

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

    def doAction(self):
        if not self.inAction:
            action = random.choices(self.DNA, weights=(self.DNA[0], self.DNA[1], self.DNA[2], self.DNA[3]), k=1)
            if action[0] == self.hideProb:
                print("hide")
                #TODO: A*
                pass
            elif action[0] == self.powerProb:
                print("pow")
                #TODO: A*
                pass
            elif action[0] == self.enemyProb:
                print("enemy")
                #TODO: A*
                pass
            elif action[0] == self.bombProb:
                print("bomb")
                #TODO: self.placeBomb() and get away
                pass
            self.inAction = True
