# Main File

import pygame as pg
import sys
from pygame.locals import QUIT
from Game.Menu import Menu
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
firstBuild = False

## Loop that controls the game
while running:
    # Instances of the screens are created
    menu = Menu(window)
    gameMap = GameMap()

    if menuFlag:   # Draws everything on the menu screen
        menu.draw()
        if menu.clicked:
            menuFlag = False
            gameFlag = True

    elif gameFlag:
        if not firstBuild:  # Initializes the map and draws it
            window.fill((0,153,77))
            gameMap.test(window)
            firstBuild = True

    for event in pg.event.get():
        if event.type == pg.locals.QUIT:
            running = False
            pg.quit()
            sys.exit()

        pg.display.update()
