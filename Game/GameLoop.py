import pygame as pg
from Map.GameMap import GameMap
from Game.Player import Player

class GameLoop:
    def __init__(self, screen, displayWidth, displayHeight):
        self.screen = screen
        self.firstBuild = False
        self.gameMap = GameMap()
        self.player = Player(displayWidth, displayHeight)

        self.allPlayers = pg.sprite.Group()
        self.allBombs = pg.sprite.Group()

        self.allPlayers.add(self.player)
        self.allBombs.add(self.player.bomb)

    def run(self):
        if not self.firstBuild:  # Initializes the map and draws it
            self.gameMap.test(self.screen)
            self.firstBuild = True

        self.screen.fill((0, 153, 77))

        # ---------------------------------------
        #TODO: separate this code
        statsSurf = pg.Surface((200,720))
        statsSurf.fill((0,85,255))
        self.screen.blit(statsSurf, (1280,0))
        # ---------------------------------------

        self.gameMap.drawMap(self.screen)
        keys = pg.key.get_pressed()
        self.player.update(keys, self.gameMap.walls, self.gameMap.fakeWalls)
        self.allPlayers.draw(self.screen)

        for player in self.allPlayers.sprites():
            if player.placeBomb:
                player.bomb.draw(self.screen)
