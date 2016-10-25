import Population

keyword = 'goal'
populationcap = 200
mutationrate = .01

pop = Population.Population(populationcap, keyword, mutationrate)

count = 0
pop.population = pop.reproduce()
while pop.donecheck():
    count += 1
    pop.reproduce()
    print('Best match: ' + pop.showbest()[0] + ' Fitness: ' + str(pop.showbest()[1]) + ' Generation: ' + str(count))
