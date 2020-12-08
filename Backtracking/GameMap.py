from random import randint


## @class Creates the game map.
#  @brief Includes the non-destroyable blocks within
#         the map ensuring that players can access other players within the map.
class GameMap:

    ## Constructor of the class.
    #  Initialize the players number in zero, the players list and the grid of the game.
    def __init__(self):
        self.players = 0
        self.players_list = []
        self.grid = []

    ## Is a getter that returns the position in the grid of a spacific player.
    #  @param player Is an int that characterize each player.
    #  @return a tuple with the position i j of the player in the map.
    def getPlayerPosition(self, player):
        return self.players_list[player]

    ## Sets the non-destroyable blocks in the matrix or grid of the map.
    #  @param matrix Is the matrix where the blocks must be placed.
    #  @param items Is an int that indicates how much blocks must be placed in the matrix.
    def setNonDestructibleItems(self, matrix, items):
        for x in range(items):
            i, j = randint(0, len(matrix) - 1), randint(0, len(matrix[0]) - 1)
            if matrix[i][j] == "0":
                matrix[i][j] = "1"
        if not self.checkPaths(matrix):
            for i in matrix:
                for j in range(len(i)):
                    if i[j] is "1":
                        i[j] = "0"
            self.setNonDestructibleItems(matrix, items)

    ## Obtains the neighboring blocks of a specific block of the matrix and inserts it into a list.
    #  @param current Is the block of a player where starts the searc
    def getNeighbours(self, current, destiny, matrix, visited):
        i, j = current[0], current[1]
        matrix_i, matrix_j = len(matrix) - 1, len(matrix[0]) - 1
        # print(visited)
        result = []
        if not j + 1 > matrix_j:
            temp = [i, j + 1]
            if temp not in visited and (
                    matrix[temp[0]][temp[1]] == "0" or matrix[temp[0]][temp[1]] == "P" + destiny.__str__()):
                result.append(temp)
        if not i + 1 > matrix_i:
            temp = [i + 1, j]
            if temp not in visited and (
                    matrix[temp[0]][temp[1]] == "0" or matrix[temp[0]][temp[1]] == "P" + destiny.__str__()):
                result.append(temp)
        if not j - 1 < 0:
            temp = [i, j - 1]
            if temp not in visited and (
                    matrix[temp[0]][temp[1]] == "0" or matrix[temp[0]][temp[1]] == "P" + destiny.__str__()):
                result.append(temp)
        if not i - 1 < 0:
            temp = [i - 1, j]
            if temp not in visited and (
                    matrix[temp[0]][temp[1]] == "0" or matrix[temp[0]][temp[1]] == "P" + destiny.__str__()):
                result.append(temp)
        return result

    def DFS(self, current, destiny, matrix, visited):
        stack = [current]
        while stack:
            s = stack.pop()
            if s == self.getPlayerPosition(destiny):
                return True
            if matrix[s[0]][s[1]] == destiny:
                return True
            if s not in visited:
                visited.append(s)
            neighbours = self.getNeighbours(s, destiny, matrix, visited)
            stack += neighbours
        return False

    def checkPaths(self, matrix):
        for i in range(self.players):
            for j in range(self.players):
                if i == j:
                    continue
                if not self.DFS(self.getPlayerPosition(i), j, matrix, []):
                    print(False)
                    return False
        return True

    def setPlayer(self, i, j, matrix):
        self.players_list.append([i, j])
        if matrix[i][j] == "0":
            matrix[i][j] = "P" + self.players.__str__()
            # matrix[i][j] = players
            self.players += 1

    def create_grid(self):
        # grid = []
        size_rows = 18
        size_columns = 42
        size = 40
        print("jjsbfd")
        for i in range(size_rows):
            temp = []
            for j in range(size_columns):
                temp.append("0")
            self.grid.append(temp)
        self.setPlayer(2, 3, self.grid)
        self.setPlayer(10, 23, self.grid)
        self.setPlayer(7, 14, self.grid)
        self.setPlayer(16, 6, self.grid)
        self.setNonDestructibleItems(self.grid, round((30 ** 2) / 2))
        self.print_grid()
        return self.grid

    def print_grid(self):
        for i in self.grid:
            temp = ""
            for j in i:
                temp += str(j) + "  "
            print(temp)


if __name__ == '__main__':
    my_map = GameMap()
    my_map.create_grid()
