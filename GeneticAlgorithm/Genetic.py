from GeneticAlgorithm.Character import Character
import random
import copy

class Genetic:

    def __init__(self, characteres, nPopulation):
        self.characteres = characteres #lista de individuos
        self.nPopulation = nPopulation #Cantidad de idividuos que quiero

    #Obtiene la lista de individuos
    def getCharacteres(self):
        return self.characteres

    #Setea la lista de individuos
    def setCharacteres(self, newCharacteres):
        self.characteres = newCharacteres

    #Verifica que la suma de las probabilidades sea 100
    def sumList(self, listElements):
        for j in range(len(listElements)):
            aux = sum(listElements)
            if aux != 100:
                n = 100 - aux
                listElements[random.randint(0, 3)] += n

    #Genera la poblacion inicial
    def generateFP(self):
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

    #Función Fitness

    #Calcula primer parametro para el fitness
    #Bombas mas cercanas a los idividuos
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

    #Calcula segundo y tercer parametro para el fitness
    #Bombas detonodas en enemigos
    #Bombas detonadas en bloques
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

    #Suma de todos los parametros para el fitness
    def fitness(self):
        for i in range (len(self.characteres)):
            fit = self.f1(self.characteres[i].bombsRecord)\
                  + self.f2(self.characteres[i].enemiesRecord)\
                  + self.f2(self.characteres[i].blockRecord)
            self.characteres[i].setFitness(fit)

    #Seleccion

    #Suma de todos los fitness
    def totalFit(self, listPopu):
        globalFitness = 0
        i = 0
        for i in range(len(listPopu)):
            globalFitness += listPopu[i].fitness
        return globalFitness

    #Selección de individuos para el crossover
    #Se utiliza el metodo de la ruleta
    def selection(self, selecSize):
        popu = self.characteres.copy()
        selectedPopu = []
        i = 0
        for i in range(selecSize):
            aux = random.randint(0, self.totalFit(popu))
            random.shuffle(popu)
            sumDec = 0
            for character in popu:
                sumDec += character.getFitness()
                if sumDec >= aux :
                    selectedPopu.append(character)
                    popu.remove(character)
                    break
        self.setCharacteres(selectedPopu)
        print(len(selectedPopu))

    #Crossover
    #Metodo de un solo puntu
    def crossover(self, reproduc):
        parents = copy.deepcopy(self.characteres)
        random.shuffle(parents)
        for i in range(reproduc):
            parent1 = parents[random.randint(0, len(parents))].getDNA()
            parent2 = parents[random.randint(0, len(parents))]
            son1 = Character(len(self.characteres) + 1)
            son2 = Character(len(self.characteres) + 1)
            point = random.randint(0, 2)
            if point == 1:
                son1.setDNA([parent1[0], parent2[1], parent2[2], parent2[3]])
                son2.setDNA([parent2[0], parent2[1], parent1[2], parent2[3]])
                self.characteres.append(son1, son2)
            if point == 2:
                son1.setDNA([parent1[0], parent1[1], parent2[2], parent2[3]])
                son2.setDNA([parent2[0], parent2[1], parent1[2], parent1[3]])
                self.characteres.append(son1, son2)
            else:
                son1.setDNA(parent1.getDNA())
                son2.setDNA(parent2.getDNA())
                self.characteres.append(son1, son2)

    #Mutation
    def mutation(self, probMuta):
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
