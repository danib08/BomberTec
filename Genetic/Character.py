
class Character(object):

    #Constructor
    def __init__(self, id):
        self.id = id
        self.DNA = [0, 0, 0, 0]
        self.bombsRecord = [7, 8, 9, 2 ]
        self.enemiesRecord = [1, 0, 1, 1]
        self.blockRecord = [0, 1, 0, 0]
        self.fitness = 0

    #Getters
    def getId(self):
        return self.id

    def getDNA(self):
        return self.DNA

    def getEnemiesR(self):
        return self.enemiesRecord

    def getBombsR(self):
        return self.bombsRecord

    def getBlockR(self):
        return self.blockRecord

    def getFitness(self):
        return self.fitness

    #Setters
    def setId(self, nID):
        self.id = nID

    def setDNA(self, nDNA):
        self.DNA = nDNA

    def setFitness(self, fitness):
        self.fitness = fitness




