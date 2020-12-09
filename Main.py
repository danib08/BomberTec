# Main File

import pygame as pg
import sys
from pygame.locals import QUIT
from Game.Menu import Menu
from Map.GameMap import GameMap
from Game.Player import Player

pg.init()

displayWidth = 1280
displayHeight = 720
screen = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("BomberTec")
screen.fill((187, 153, 255))

clock = pg.time.Clock()

# Flags
running = True
menuFlag = True
gameFlag = False
firstBuild = False

# Instances of the screens are created
menu = Menu(screen)
gameMap = GameMap()

all_sprites_list = pg.sprite.Group()
player = Player()
all_sprites_list.add(player)

## Loop that controls the game
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if menuFlag:   # Draws everything on the menu screen
        menu.draw()
        if menu.clicked:
            menuFlag = False
            gameFlag = True

    elif gameFlag:
        if not firstBuild:  # Initializes the map and draws it
            screen.fill((0, 153, 77))
            gameMap.test(screen)
            firstBuild = True

        keys = pg.key.get_pressed()
        all_sprites_list.update(keys)
        all_sprites_list.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()