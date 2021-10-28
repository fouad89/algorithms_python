import random
from Individual import *
import math

import sys


random.seed(12345)

class GA:
    def __init__(self, _mutation, _totalPopulation, _maxIterations, _target):
        self.mutationRate = _mutation
        self.totalPopulation = _totalPopulation
        self.maxIterations = _maxIterations
        self.target = _target

        self.population = []
        self.matingPool = []
        self.best = None
        self.iteration = 0
        self.printPopulation = False
        self.genSize = len(self.target)

        # initial population
        for i in range(0, self.totalPopulation):
            self.population.append(Individual(self.genSize))

        self.best = self.population[0]

    def crossover(self, ind1, ind2):
        child = Individual(self.genSize)
        splitPoint = random.randint(0,self.genSize)
        child.genes[0:splitPoint] = ind1.genes[0:splitPoint]
        child.genes[splitPoint:self.genSize] = ind2.genes[splitPoint:self.genSize]
        return child

    def mutate(self, ind):
        for i in range(0, self.genSize):
            if random.randint() < self.mutationRate:
                ind.genes[i] = chr(random.randint(32, 128))

    def GAStep(self):
        for ind in self.population:
            ind.computeFitness(self.target)
            



        
    def search(self):
        self.iteration = 0
        while self.iteration < self.maxIterations and self.best.getFitness() < 1:
            self.GAStep()
            self.iteration += 1
        print ("i: "+str(self.iteration),  self.best.getPhrase(), self.best.getFitness(), sep="\t")