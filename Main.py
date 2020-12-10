# Main File

import pygame as pg
import sys
from Game.Screens import Menu
from Game.Screens import GameOver
from Game.GameLoop import GameLoop

pg.init()

displayWidth = 1480
displayHeight = 720
screen = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("BomberTec")
screen.fill((187, 153, 255))

clock = pg.time.Clock()

# Flags
running = True
menuFlag = True
gameFlag = False
overFlag = False

# Instances of the screens are created
menu = Menu(screen)
gameOver = GameOver(screen)
gameLoop = GameLoop(screen, displayWidth - 200, displayHeight)

# Loop that controls the game
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if gameFlag:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not gameLoop.player.placedBomb:   # Place bombs
                    gameLoop.player.placeBomb()

    if menuFlag:   # Draws everything on the menu screen
        menu.draw()
        if menu.clicked:
            menuFlag = False
            gameFlag = True

    elif gameFlag:
        game = gameLoop.run()
        if game == 1:
            gameFlag = False
            overFlag = True
            gameOver.clicked = False

    elif overFlag:
        gameOver.draw()
        if gameOver.clicked:
            gameLoop = GameLoop(screen, displayWidth - 200, displayHeight)
            overFlag = False
            gameFlag = True

    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()