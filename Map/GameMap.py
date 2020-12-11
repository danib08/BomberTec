import random
import pygame
from Map import AStarAlgorithm
from Backtracking import CreateMap
from Map.Walls import Wall

class GameMap:
    """
    Class GameMap that create and manage de map
    """
    def __init__(self):
        """
        Constructor method of GameMap class
        """
        self.walls = []
        self.fakeWalls = []
        self.allWalls = []
        self.backMatrix = []
        self.mapMatrix = []
        self.wallImage = pygame.image.load("Resources/SolidBlock.png").convert()
        self.wallImage = pygame.transform.scale(self.wallImage, (40, 40))

    def drawWall(self, surface, rectangle):
        """
        draw and add the wall on the screen
        :param surface: Window
        :param rectangle: py.rect (wall)
        """
        pygame.draw.rect(surface, (32, 32, 32), rectangle)
        surface.blit(self.wallImage, rectangle)

    def buildMap(self, new_map):
        """
        Method that create and add the py.rect into the walls list
        Also this method only works for the indestructible blocks
        :param new_map: matrix that is the template of the map
        :return: walls: list of indestructible blocks
        """
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == "1":
                    self.walls.append(pygame.Rect(x, y, 40, 40))

                x += 40
            x = 0
            y += 40

    def buildFakeWall(self, new_map):
        """
        Method that creates and adds the Walls into the fakeWalls list
        Also this method only works for the destructible blocks
        :param new_map: matrix that is the template of the map
        :return: null
        """
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == "2":
                    self.fakeWalls.append(Wall(x, y, 40, 40, i, j))

                x += 40
            x = 0
            y += 40


    def buildAllWalls(self, new_map):
        """
        Method that creates and add the Walls into the allWalls list
        This method adds all of the blocks on the map (including non-walls)
        :param new_map: matrix that is the template of the map
        :return: null
        """
        x = 0
        y = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                self.allWalls.append(Wall(x, y, 40, 40, i, j))
                x += 40
            x = 0
            y += 40

    def drawFakeWalls(self, surface, rectangle):
        """
        draw and add the wall on the screen
        :param surface: Window
        :param rectangle: py.rect (wall)
        """
        pygame.draw.rect(surface, (104, 104, 104), rectangle)
        surface.blit(rectangle.image, rectangle)

    def drawMap(self, surface):
        """
        This method scroll through the list and iterate through to create the walls
        :param surface: window
        :return:
        """
        for wall in self.walls:
            self.drawWall(surface, wall)
        for wall in self.fakeWalls:
            self.drawFakeWalls(surface, wall)

    def createFakeBlocks(self, map):
        """
        Method that edit the matrix template and add the fakewalls symbol into the matrix
        Also edit the free space for the players
        :param map: matrix that is the template of the map
        :return: map: matrix that is the new template of the map
        """
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
        map[8][0] = "0"
        map[8][1] = "0"
        map[10][0] = "0"
        map[10][1] = "0"
        map[9][1] = "0"
        map[9][30] = "0"
        map[8][31] = "0"
        map[10][31] = "0"
        map[10][30] = "0"
        map[8][30] = "0"
        map[0][17] = "0"
        map[0][15] = "0"
        map[1][15] = "0"
        map[1][17] = "0"
        map[1][16] = "0"
        map[17][17] = "0"
        map[17][15] = "0"
        map[16][15] = "0"
        map[16][17] = "0"
        map[16][16] = "0"
        return map

    def adaptiveMatrix(self, map):
        newMatrix = []
        row = []
        for i in range(0, 17):
            for j in range(0, 31):
                if map[i][j] == "0" or map[i][j] == "2":
                    row.append(0)
                elif map[i][j] == "1":
                    row.append(1)
                else:
                    row.append(0)
            newMatrix.append(row)
            row = []
        self.mapMatrix = newMatrix

    def run(self, surface):
        """
        Method that start the map on screen
        :param surface: window

        """
        my_map = CreateMap.CreateMap()
        self.backMatrix = my_map.create_grid()
        self.backMatrix = self.createFakeBlocks(self.backMatrix)
        self.buildMap(self.backMatrix)
        self.buildFakeWall(self.backMatrix)
        self.buildAllWalls(self.backMatrix)
        self.drawMap(surface)
        self.adaptiveMatrix(self.backMatrix)
