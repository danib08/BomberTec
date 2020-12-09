import pygame as pg

class Player(pg.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, screenWidth, screenHeight):
        super().__init__()
        self.screenW = screenWidth
        self.screenH = screenHeight
        self.image = pg.Surface((25,25))
        self.image.fill((25,217,255))

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self, keys):
        if keys[pg.K_w] and self.rect.x :
            self.rect.move_ip(0,-5)
        if keys[pg.K_a]:
            self.rect.move_ip(-5, 0)
        if keys[pg.K_s]:
            self.rect.move_ip(0, 5)
        if keys[pg.K_d]:
            self.rect.move_ip(5,0)
        if keys[pg.K_SPACE]:
            # Place bomb
            pass

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.screenW:
            self.rect.right = self.screenW

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= self.screenH:
            self.rect.bottom = self.screenH

