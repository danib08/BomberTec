from Character import Character
import random

class Genetic:

    def __init__(self, characteres, nPopulation):
        self.characteres = characteres
        self.nPopulation = nPopulation

    def getCharacteres(self):
        return self.characteres

    def setCharacteres(self):
        return self.characteres

    def sumList(self, listElements):
        for j in range(len(listElements)):
            aux = sum(listElements)
            if aux != 100:
                n = 100 - aux
                listElements[3] = listElements[3] + n

    def generateFP(self):
        i = 0
        for i in range(self.nPopulation):
            nCharacter = Character(i+1)
            j = 0
            prob = 100
            for j in range(len(nCharacter.DNA)):
                aux = random.randint(0, prob)
                nCharacter.DNA[j] = aux;
                prob = prob - aux
                if j == 3:
                    Genetic.sumList(self, nCharacter.DNA)
            random.shuffle(nCharacter.DNA)
            self.characteres.append(nCharacter)


    #Función Fitness
    def f1(self, bombsR):
        value = 0
        if len(bombsR) == 0:
            return value
        else:
            for i in range(len(bombsR)):
                value = value + bombsR[i]
            f = 1/(value/sum(bombsR))
            print(f)
            return f

    def f2(self, enemiesR):
        value = 0
        if len(enemiesR) == 0:
            return value
        else:
            for i in range(len(enemiesR)):
                value = value + enemiesR[i]
            f = value/len(enemiesR)
            print(f)
            return f

    def fitness(self):
        i = 0
        for i in range (len(self.characteres)):
            fit = self.f1(self.characteres[i].bombsRecord)\
                  + self.f2(self.characteres[i].enemiesRecord)\
                  + self.f2(self.characteres[i].blockRecord)
            self.characteres[i].setFitness(fit)

    #Selección
    def totalFit(self, listPopu):
        globalFitness = 0
        i = 0
        for i in range(len(listPopu)):
            globalFitness += listPopu[i].fitness
        return globalFitness

    def selection(self, selecSize):
        popu = self.characteres.copy();
        selectedPopu = []
        i = 0
        for i in range(selecSize):
            aux = random.randint(0, self.totalFit(popu))
            random.shuffle(popu)
            sumDec = 0
            cont = 0
            for character in popu:
                sumDec += character.getFitness()
                if sumDec == aux :
                    selectedPopu.append(character)
                    popu.remove(character)
                    break;
                cont += 1
        return selectedPopu


    def reproduction(self):
        print("Reproduction")

    def crossOver(self):
        print("crossover")

    def mutation(self):
        print("Mutacion")










