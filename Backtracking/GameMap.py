from random import randint

class GameMap:
    def __init__(self):
        self.players = 0
        self.players_list = []
        self.grid= []

    def getPlayerPosition(self, player):
        return self.players_list[player]

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
        #grid = []
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
    map = GameMap()
    map.create_grid()
