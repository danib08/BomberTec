from GeneticAlgorithm.Character import Character
import random
import copy

class Genetic:

    """
    This class represents the Genetic Algorithm
    """

    def __init__(self, characteres, nPopulation):
        """
        Constructor of the Genetic class
        :param characteres: character list
        :param nPopulation: population size
        """
        self.characteres = characteres #lista de individuos
        self.nPopulation = nPopulation #Cantidad de idividuos que quiero


    def getCharacteres(self):
        """
        Is a getter that returns the character list.
        :return: list with character type objects.
        """
        return self.characteres


    def setCharacteres(self, selectedPopu):
        """
        Sets the population with the new character list after crossover.
        :param selectedPopu: Is the new character list with the new members of the population.
        """
        self.characteres = selectedPopu


    def sumList(self, listElements):
        """
        Check that the sum of the probabilities is 100.
        :param listElements: Is the list with the genes.
        """
        for j in range(len(listElements)):
            aux = sum(listElements)
            if aux != 100:
                n = 100 - aux
                listElements[random.randint(0, 3)] += n


    def generateFP(self):
        """
        Generates the first population.
        :return: list with the first population.
        """
        for i in range(self.nPopulation):
            nCharacter = Character(i+1)
            prob = 100
            for j in range(len(nCharacter.DNA)):
                aux = random.randint(0, prob)
                nCharacter.DNA[j] = aux
                prob = prob - aux
                if j == 3:
                    Genetic.sumList(self, nCharacter.DNA)
            random.shuffle(nCharacter.DNA)
            self.characteres.append(nCharacter)


    def f1(self, bombsR):
        """
        First element of the fitness function.
        :param bombsR: Is the list with bombs Record.
        :return: result of bombs efficiency.
        """
        value = 0
        if len(bombsR) == 0:
            return value
        else:
            for i in range(len(bombsR)):
                value = value + bombsR[i]
            f = 1/(value/sum(bombsR))
            return f

    def f2(self, enemiesR):
        """
        Second and third elements of the fitness function.
        :param enemiesR: Is the list with Enemies Record.
        :param blocksR: Is the list with Blocks Record.
        :return: result of bombs efficiency with the detonation of the enemies and blocks.
        """
        value = 0
        if len(enemiesR) == 0:
            return value
        else:
            for i in range(len(enemiesR)):
                value = value + enemiesR[i]
            f = value/len(enemiesR)
            return f

    def fitness(self):
        """
        Fitness function, evaluate each member of the population and sets the fitness value.
        :return: Fitness Value of eache member.
        """
        for i in range (len(self.characteres)):
            fit = (self.f1(self.characteres[i].bombsRecord)
                  + self.f2(self.characteres[i].enemiesRecord)
                  + self.f2(self.characteres[i].blockRecord))*10
            self.characteres[i].setFitness(fit)

    def totalFit(self, listPopu):
        """
        Sums each fitness value member.
        :param listPopu: population list.
        :return: A total sum of the fitness value of each member.
        """
        globalFitness = 0
        i = 0
        for i in range(len(listPopu)):
            globalFitness += listPopu[i].fitness
        return round(globalFitness)

    def selection(self):
        """
        Select the best population members, with roulette methood.
        :return: Parents of the new population members.
        """
        popu = copy.deepcopy(self.characteres)
        selectedPopu = []
        i = 0
        for i in range(4):
            aux = random.randint(0, self.totalFit(popu))
            random.shuffle(popu)
            sumDec = 0
            cont = 0
            for character in popu:
                sumDec += character.fitness
                if sumDec >= aux :
                    cont += 1
                    selectedPopu.append(character)
                    popu.remove(character)
                    break
        self.setCharacteres(selectedPopu)
        print(len(selectedPopu))


    def crossOver(self, reproduc):
        """
        Create the new population members with the selected parents.
        :param reproduc: number of the new members.
        :return: A new population list with the new members.
        """
        parents = copy.deepcopy(self.characteres)
        random.shuffle(parents)
        for i in range(reproduc):
            parent1 = parents[random.randint(0, len(parents)-1)].DNA
            parent2 = parents[random.randint(0, len(parents)-1)].DNA
            son1 = Character(len(self.characteres)+1)
            son2 = Character(len(self.characteres)+1)
            point = random.randint(0, 2)
            if point == 1:
                son1.DNA = [parent1[0], parent2[1], parent2[2], parent2[3]]
                son2.DNA = [parent2[0], parent2[1], parent1[2], parent2[3]]
                self.characteres.append(son1)
                self.characteres.append(son2)
            if point == 2:
                son1.DNA = [parent1[0], parent2[1], parent2[2], parent2[3]]
                son2.DNA = [parent2[0], parent2[1], parent1[2], parent2[3]]
                self.characteres.append(son1)
                self.characteres.append(son2)
            else:
                son1.DNA = parent1
                son2.DNA = parent2
                self.characteres.append(son1)
                self.characteres.append(son2)


    def mutation(self, probMuta):
        """
        Mutates some population members, this depends of the probability mutation.
        :param probMuta: probability mutation.
        """
        for character in self.characteres:
            defMut = random.randint(0, 100)
            if defMut <= probMuta:
                incre = random.randint(0, 3)
                decre = random.randint(0, 3)
                if incre == decre:
                    while decre == incre:
                        incre = random.randint(0, 3)
                        decre = random.randint(0, 3)
                    cant = random.randint(0, character.DNA[decre])
                    character.DNA[decre] -= cant
                    character.DNA[incre] += cant
                else:
                    cant = random.randint(0, character.DNA[decre])
                    character.DNA[decre] -= cant
                    character.DNA[incre] += cant
