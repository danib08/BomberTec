# Main File
import pygame as pg
import sys
from pygame.locals import QUIT
from Game.Menu import *
from Map.GameMap import GameMap

pg.init()

displayWidth = 1280
displayHeight = 720
window = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("BomberTec")
window.fill((187,153,255))

clock = pg.time.Clock()
running = True
menuFlag = True
gameFlag = False

## Loop that controls the game
while running:
    #clock.tick(60)
    menu = Menu(window)
    gameMap = GameMap()

    if menuFlag:
        menu.draw()
        if menu.clicked:
            menuFlag = False
            gameFlag = True

    elif gameFlag:
        window.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.locals.QUIT:
            running = False
            pg.quit()
            sys.exit()

        pg.display.update()
