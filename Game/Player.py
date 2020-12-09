import pygame as pg

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
        self.image = pg.Surface((40,40))  # Player's surface dimensions
        self.image.fill((25,217,255))
        self.rect = self.image.get_rect()  # Fetch the rectangle object that has the dimensions of the image

        # self.bomb = Bomb(screenHeight, screenHeight)

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
        # if keys[pg.K_SPACE]:
        #     # Place bomb
        #     self.bomb.draw()

        # Keep player on-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screenW:
            self.rect.right = self.screenW
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screenH:
            self.rect.bottom = self.screenH

# class Bomb(pg.sprite.Sprite):
#     """
#     Class that represents a bomb.
#     Extends from the pygame Sprite class.
#     """
#     def __init__(self, screenWidth, screenHeight):
#         """
#         Constructor for the player.
#         :param screenWidth: The screen width that will be the bomb's x coordinate limit
#         :param screenHeight: The screen height that will be the bomb's y coordinate limit
#         """
#         super().__init__()
#         self.screenW = screenWidth
#         self.screenH = screenHeight
#         self.image = pg.Surface((25, 25))
#         self.image.fill((255,25,25))
#         self.rect = self.image.get_rect()
#
#     def update(self):
#         if self.rect.left < 0:
#             self.rect.left = 0
#         if self.rect.right > self.screenW:
#             self.rect.right = self.screenW
#         if self.rect.top <= 0:
#             self.rect.top = 0
#         if self.rect.bottom >= self.screenH:
#             self.rect.bottom = self.screenH