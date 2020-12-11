from GeneticAlgorithm.Genetic import Genetic

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myGenetic = Genetic([], 8)
    myGenetic.generateFP()
    myGenetic.fitness()
    myGenetic.selection()
    myGenetic.crossOver(4)
    myGenetic.mutation(40)
