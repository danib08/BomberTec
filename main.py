from Genetic import Genetic

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myGenetic = Genetic([], 500)
    myGenetic.generateFP()
    myGenetic.fitness()
    myGenetic.selection(200)

