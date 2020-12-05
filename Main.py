# Main File
import pygame as pg
import sys
from pygame.locals import QUIT
from Game.Menu import *
from Map.GameMap import GameMap

pg.init()

## Main class that initializes the game

displayWidth = 1280
displayHeight = 720
window = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("BomberTec")
window.fill((255,77,196))

clock = pg.time.Clock()
running = True

#gameMap = GameMap()
#gameMap.test(window)

## Loop that controls the game
while running:
    clock.tick(60)
    menu = Menu(displayWidth, displayHeight, window)

    for event in pg.event.get():
        if event.type == pg.locals.QUIT:
            pg.quit()
            sys.exit()

        pg.display.update()
