# Main File

import pygame, sys
import pygame.locals
from Map.GameMap import GameMap

pygame.init()

## Main class that initializes the map
class Main:
    displayWeight = 1280
    displayHeight = 720
    window = pygame.display.set_mode((displayWeight, displayHeight))
    pygame.display.set_caption("BomberTec")
    window.fill((0, 0, 0))

    clock = pygame.time.Clock()
    gameMap = GameMap()

    ## Method that initializes the map construction and drawing
    def start(self):
        self.gameMap.test(self.window)
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.start()
