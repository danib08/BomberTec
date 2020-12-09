import pygame as pg

class Player(pg.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        super().__init__()
        self.image = pg.Surface((25,25))
        self.image.fill((25,217,255))

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self, keys):
        if keys[pg.K_d]:
            self.rect.move_ip(5,0)
