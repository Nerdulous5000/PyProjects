import string
import random


class Population:
    pass

    def __init__(self, populationcap, keyword, mutationrate):
        self.keyword = keyword
        self.keylen = len(keyword)
        self.mutationrate = mutationrate
        self.populationcap = populationcap
        self.population = self.populate()

    def populate(self):
        poparray = [''] * self.populationcap
        temp = [''] * self.keylen

        for i in range(self.populationcap):
            for x in range(self.keylen):
                temp[x] = (str(unichr(random.randrange(94)+32)))
            poparray[i] = ''.join(temp)
        return poparray

    def mutate(self):
        for i in range(self.populationcap):
            for x in range(self.keylen):
                if self.mutationrate > random.random():
                    self.population[i] = string.replace(self.population[i], self.population[i][x], str(unichr(random.randrange(94)+32)))
        return self.population

    def crossover(self, var1, var2):
        midpoint = random.randrange(1, self.keylen-1)
        return var1[0:midpoint]+var2[midpoint:len(var2)]

    def scorefit(self, element):
        fitscore = 0
        for i in range(self.keylen):
            if element[i] == self.keyword[i]:
                fitscore += 1
        return (float(fitscore)/float(self.keylen)) ** 3

    def selection(self,):
        selecpopulation = [''] * self.populationcap
        for i in range(self.populationcap):
            n = 0
            while n == 0:
                x = random.randrange(self.populationcap)
                if random.random() - .01 <= self.scorefit(self.population[x]):
                    selecpopulation[i] = self.population[x]
                    n = 1
        return selecpopulation

    def donecheck(self):
        for i in range(self.populationcap):
            if self.scorefit(self.population[i]) >= 1:
                return 0
        return 1

    def showbest(self):
        fitmax = ['', -1]
        for i in range(self.populationcap):
            if self.scorefit(self.population[i]) > fitmax[1]:
                fitmax[0] = self.population[i]
                fitmax[1] = self.scorefit(self.population[i])
        return fitmax

    def reproduce(self):
        if self.keylen <= 2:
            self.population = self.populate()
            return self.population
        repopulation = [''] * self.populationcap
        poptemp = self.selection()
        self.population = poptemp
        repopulation[0] = self.crossover(self.population[self.populationcap-1], self.population[0])
        for i in range(1, self.populationcap):
            repopulation[i] = self.crossover(self.population[i-1], self.population[i])
        self.population = repopulation
        self.population = self.mutate()
        return self.population
