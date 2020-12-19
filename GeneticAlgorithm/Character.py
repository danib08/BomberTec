
class Character(object):

    #Constructor
    def __init__(self, new_id):
        self.id = new_id
        self.DNA = [0, 0, 0, 0]
        self.bombsRecord = []
        self.enemiesRecord = []
        self.blockRecord = []
        self.fitness = 0

    def setDNA(self, nDNA):
        self.DNA = nDNA

    def setFitness(self, fitness):
        self.fitness = fitness




