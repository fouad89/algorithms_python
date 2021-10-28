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
            if random.random() < self.mutationRate:
                ind.genes[i] = chr(random.randint(32, 128))

    def GAStep(self):
        for ind in self.population:
            ind.computeFitness(self.target)

        matingPool = []
        for ind in self.population:
            elementsInPool = int(ind.getFitness()*100)
            for i in range(0, elementsInPool):
                matingPool.append(ind)
        print(matingPool)
        for ind_i in range(0, len(self.population)):
            indexPartnerA = random.randint(0, len(matingPool)-1)
            indexPartnerB = random.randint(0, len(matingPool)-1)

            partnerA = matingPool[indexPartnerA]
            partnerB = matingPool[indexPartnerB]

            child = self.crossover(partnerA, partnerB)
            self.mutate(child)
            child.computeFitness(self.target)
            self.population[ind_i] = child
            if child.getFitness() > self.best.getFitness():
                self.best = child

                print ("Best so far =============")
                print ("Iteration: "+str(self.iteration))
                print ("Fitness: "+str(self.best.getPhrase()))
                print ("Cost: "+str(self.best.getFitness()))
                print ("=========================")

            



        
    def search(self):
        self.iteration = 0
        while self.iteration < self.maxIterations and self.best.getFitness() < 1:
            self.GAStep()
            self.iteration += 1
        print ("i: "+str(self.iteration),  self.best.getPhrase(), self.best.getFitness(), sep="\t")


ga = GA(0.01, 1000, 5000, "Diarmuid O'Greachain is ainm dom")
ga.search()