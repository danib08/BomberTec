import pygame
from Map import AStarAlgorithm

pygame.init()

## This class represents the game map
class GameMap:
    mapMatrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    ## Draws a wall on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param rectangle
    def drawWall(self, surface, rectangle):
        pygame.draw.rect(surface, (0, 0, 0), rectangle)

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
                    walls.append(pygame.Rect(x, y, 80, 80))
                x += 80
            x = 0
            y += 80

        return walls

    ## Draws the map on-screen
    #  @param self The object pointer
    #  @param surface
    #  @param walls
    def drawMap(self, surface, walls):
        for wall in walls:
            self.drawWall(surface, wall)

    ## Temporary method that generates a map
    #  @param surface
    def test(self, surface):
        start = (1, 1)
        end = (7, 14)
        path = AStarAlgorithm.astar(self.mapMatrix, start, end)
        print(path)
        walls = self.buildMap(self.mapMatrix)
        self.drawMap(surface, walls)

pygame.quit()
