import pygame
from Map import AStarAlgorithm

pygame.init()

## This class represents the game map
class GameMap:
    mapMatrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param rectangle
    def drawWall(self, surface, rectangle):
        pygame.draw.rect(surface, (255, 255, 255), rectangle)

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param new_map
    def buildMap(self, new_map):
        walls = []
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == 1:
                    walls.append(pygame.Rect(x, y, 40, 40))

                x += 40
            x = 0
            y += 40

        return walls

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param new_map
    def buildFakeWall(self, new_map):
        walls2 = []
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == 2:
                    walls2.append(pygame.Rect(x, y, 40, 40))

                x += 40
            x = 0
            y += 40

        return walls2

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param rectangle
    def drawFakeWalls(self, surface, rectangle):
        pygame.draw.rect(surface, (255, 0, 0), rectangle)

    ## Draw the map on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param walls
    # @param num
    def drawMap(self, surface, walls, num):
        for wall in walls:
            if num == 1:
                self.drawWall(surface, wall)
            else:
                self.drawFakeWalls(surface, wall)

    ## Temporary method that generates a map
    #  @param surface
    def test(self, surface):
        start = (1, 1)
        end = (7, 14)
        path = AStarAlgorithm.AStar.astar(self.mapMatrix, start, end)
        print(path)
        walls = self.buildMap(self.mapMatrix)
        self.drawMap(surface, walls, 1)
        walls2 = self.buildFakeWall(self.mapMatrix)
        self.drawMap(surface, walls2, 2)


pygame.quit()
