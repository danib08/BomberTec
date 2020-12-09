from random import randint

class CreateMap:
    """
    Creates the game map.
    Includes the non-destroyable blocks within the map ensuring that players can access other players within the map.
    """

    def __init__(self):
        """
        Constructor of the class.
        Initialize the players number in zero, the players list and the grid of the game.
        """
        self.players = 0
        self.players_list = []
        self.grid = []

    def getPlayerPosition(self, player):
        """
        Is a getter that returns the position in the grid of a spacific player.
        :param player: Is an int that characterize each player.
        :return: tuple with the position i j of the player in the map.
        """
        return self.players_list[player]

    def setNonDestructibleItems(self, matrix, items):
        """
        Sets the non-destroyable blocks in the matrix or grid of the map.
        :param matrix: Is the matrix where the blocks must be placed.
        :param items: Is an int that indicates how much blocks must be placed in the matrix.
        """
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
        """
        Obtains the neighboring blocks of a specific block of the matrix and inserts it into a list.
        :param current: Is the block of a player where starts the search.
        :param destiny: Is the block destiny where ends the search for the path.
        :param matrix: Is the matrix or grid of the map.
        :param visited: Is a list that contanis all the nodes or blocks that are visited.
        :return result: A list of all current neighboring blocks that can be visited.
        """
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
        """
        Makes the search for a path between two points by means of stacked recursion.
        :param current: Is the start block for the searching.
        :param destiny: Is the end block for the searching.
        :param matrix: Is the matrix for the search of the path.
        :param visited: is a list that saves the nodes or blocks that are visited in the searching.
        :return: True or False depending on whether there is a path between the current and the destiny.
        """
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
        """
        Check if there are paths available between two blocks.
        :param matrix: is the matrix for the search of the path.
        :return: True or False on whether there is a path between all players.
        """
        for i in range(self.players):
            for j in range(self.players):
                if i == j:
                    continue
                if not self.DFS(self.getPlayerPosition(i), j, matrix, []):
                    print(False)
                    return False
        return True

    def setPlayer(self, i, j, matrix):
        """
        Creates a new player on the map at a position in the matrix.
        :param i: Is the row position.
        :param j: Is the column position.
        :param matrix: Is the matrix where the player should be placed.
        """
        self.players_list.append([i, j])
        if matrix[i][j] == "0":
            matrix[i][j] = "P" + self.players.__str__()
            # matrix[i][j] = players
            self.players += 1

    def create_grid(self):
        """
        Creates The map of the game. It calls all other functions of the class that generate all the game map.
        :return: The game map created in a matrix.
        """
        size_rows = 18
        size_columns = 32
        size = 40
        for i in range(size_rows):
            temp = []
            for j in range(size_columns):
                temp.append("0")
            self.grid.append(temp)

        # Set the required players on the map
        self.setPlayer(0, 0, self.grid)
        self.setPlayer(17, 0, self.grid)
        self.setPlayer(0, 31, self.grid)
        self.setPlayer(17, 31, self.grid)
        self.setNonDestructibleItems(self.grid, round((20 ** 2) / 2))
        #self.print_grid()
        return self.grid

    def print_grid(self):
        """
        Prints the game matrix on console.
        """
        for i in self.grid:
            temp = ""
            for j in i:
                temp += str(j) + "  "
            print(temp)
