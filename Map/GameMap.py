import random
import pygame
from Map import AStarAlgorithm
from Backtracking import CreateMap
from Map.Walls import Wall

## This class represents the game map
class GameMap:

    def __init__(self):
        self.walls = []
        self.fakeWalls = []
        self.mapMatrix = []

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param rectangle
    def drawWall(self, surface, rectangle):
        pygame.draw.rect(surface, (32,32,32), rectangle)

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param new_map
    def buildMap(self, new_map):
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == "1":
                    self.walls.append(pygame.Rect(x, y, 40, 40))

                x += 40
            x = 0
            y += 40

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param new_map
    def buildFakeWall(self, new_map):
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == "2":
                    self.fakeWalls.append(Wall(x, y, 40, 40, i, j))

                x += 40
            x = 0
            y += 40

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param rectangle
    def drawFakeWalls(self, surface, rectangle):
        pygame.draw.rect(surface, (104,104,104), rectangle)

    ## Draw the map on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param walls
    # @param num
    def drawMap(self, surface):
        for wall in self.walls:
            self.drawWall(surface, wall)
        for wall in self.fakeWalls:
                self.drawFakeWalls(surface, wall)

    def createFakeBlocks(self, map):
        for i in range(0, 17):
            for j in range(0, 31):
                flag = bool(random.getrandbits(1))
                if flag == 1 and map[i][j] == "0":
                    map[i][j] = "2"
        map[0][30] = "0"
        map[1][30] = "0"
        map[1][31] = "0"
        map[0][1] = "0"
        map[1][1] = "0"
        map[1][0] = "0"
        map[17][30] = "0"
        map[16][30] = "0"
        map[16][31] = "0"
        map[17][0] = "0"
        map[17][1] = "0"
        map[16][1] = "0"

        return map

    ## Temporary method that generates a map
    #  @param surface
    def test(self, surface):
        # start = (1, 1)
        # end = (7, 14)
        # path = AStarAlgorithm.AStar.astar(self.mapMatrix, start, end)
        # print(path)
        my_map = CreateMap.CreateMap()
        self.mapMatrix = my_map.create_grid()
        self.mapMatrix = self.createFakeBlocks(self.mapMatrix)
        self.buildMap(self.mapMatrix)
        self.buildFakeWall(self.mapMatrix)
        self.drawMap(surface)

pygame.quit()
