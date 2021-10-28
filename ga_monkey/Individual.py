# Genetic algorithm: Monkey typing a phrase
import random
class Individual:
    def __init__(self, num):
        self.fitness = -1
        self.genes = []
        self.genSize = num
        for i in range(0, num):
            self.genes.append(chr(random.randint(32, 128)))


    def getPhrase(self):
        return "".join(str(x) for x in self.genes)

    def getFitness(self):
        return self.fitness

    def computeFitness(self, target):
        score = 0.0
        for i in range(0, len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1

            self.fitness = score / len(target)
                