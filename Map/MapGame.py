import pygame
from Map import AStarAlgorithm

Weight = 1280
Height = 720


Black = (0, 0, 0)
Blue = (0, 0, 255)
Color = (45, 118, 98)

def drawWall(surface, rectangle):
    pygame.draw.rect(surface, Color, rectangle)

def buildMap(map):
    walls = []
    x = 0
    y = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                walls.append(pygame.Rect(x, y, 80, 80))
            x += 80
        x = 0
        y += 80


    return walls

def drawMap(surface, walls):
    for wall in walls:
        drawWall(surface, wall)


map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
       [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
def prueba():
    start = (1, 1)
    end = (7, 14)
    path = AStarAlgorithm.astar(map, start, end)
    print(path)
window = pygame.display.set_mode((Weight, Height))
clock = pygame.time.Clock()

walls = buildMap(map)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        a = 0
    window.fill(Black)
    drawMap(window, walls)
    prueba()
    pygame.display.update()
pygame.init()

pygame.quit()
