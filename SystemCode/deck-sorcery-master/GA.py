from DataProvider import *
from KDD import predict
import random
from deap import base
from deap import creator
from deap import tools
import time

class GeneticAlgorithm:
    def __init__(self, heroClass, initialSelection, useLibrary):
        self.heroClass = heroClass
        self.cardPool = getAvailableCardIdsForConstruction(heroClass) if not useLibrary else getLibraryCardIdsForConstruction(heroClass)
        self.initialSelection = initialSelection
        self.toolbox = base.Toolbox()

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)
        self.toolbox.register("attr_gen", random.randint, 0, len(self.cardPool) - 1)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_gen, 30 - len(self.initialSelection))
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        #----------
        # Operator registration
        #----------
        # register the goal / fitness function
        self.toolbox.register("evaluate", self.evalFct)
        self.toolbox.decorate("evaluate", tools.DeltaPenalty(self.feasible, -100))

        # register the crossover operator
        self.toolbox.register("mate", tools.cxTwoPoint)

        # register a mutation operator with a probability to
        # flip each attribute/gene of 0.05
        self.toolbox.register("mutate", tools.mutUniformInt, low=0, up=len(self.cardPool) - 1)

        # operator for selecting individuals for breeding the next
        # generation: each individual of the current generation
        # is replaced by the 'fittest' (best) of three individuals
        # drawn randomly from the current generation.
        self.toolbox.register("select", tools.selTournament)

    def evalFct(self, individual):
        deck = set()
        for i in self.initialSelection:
            deck.add(i)
        for index in individual:
            deck.add(self.cardPool[index])
        return predict(self.heroClass, deck),    
    def feasible(self, individual):
        deck = {}
        for i in self.initialSelection:
            if i in deck:
                deck[i] += 1
            else:
                deck[i] = 1
        for index in individual:
            card = self.cardPool[index]
            if card in deck:
                deck[card] += 1
            else:
                deck[card] = 1
        for card in deck.keys():
            cardRarity = getRarity(card)
            if cardRarity == "LEGENDARY" and deck[card] > 1 or deck[card] > 2:
                return False
        return True

    def run(self, popSize=300, noOfGen=1000, cxRate=lambda gen: 0.5,mutRate=lambda gen: 0.2):
        start = time.time()
        best_ind = None
        random.seed()
        pop = self.toolbox.population(n=popSize)
        print("Start of evolution")

        fitnesses = list(map(self.toolbox.evaluate, pop))
        for ind, fit in zip(pop, fitnesses):
            ind.fitness.values = fit

        print("  Evaluated %i individuals" % len(pop))  
        # Extracting all the fitnesses of 
        fits = [ind.fitness.values[0] for ind in pop]

        # Variable keeping track of the number of generations
        g = 0
        
        # Begin the evolution
        while g < noOfGen:
            # A new generation
            g = g + 1
            print("-- Generation %i --" % g)
            
            # Select the next generation individuals
            offspring = self.toolbox.select(pop, len(pop),tournsize=3)
            # Clone the selected individuals
            offspring = list(map(self.toolbox.clone, offspring))
            print("offspring length: {0}".format(len(offspring)))
        
            # Apply crossover and mutation on the offspring
            for child1, child2 in zip(offspring[::2], offspring[1::2]):

                # cross two individuals with probability CXPB
                if random.random() < cxRate(g):
                    self.toolbox.mate(child1, child2)

                    # fitness values of the children
                    # must be recalculated later
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:

                # mutate an individual with probability MUTPB
                if random.random() < mutRate(g):
                    self.toolbox.mutate(mutant, indpb=0.15)
                    del mutant.fitness.values
        
            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(self.toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit
            
            print("  Evaluated %i individuals" % len(invalid_ind))
            
            # The population is entirely replaced by the offspring
            pop[:] = offspring
            
            # Gather all the fitnesses in one list and print the stats
            fits = [ind.fitness.values[0] for ind in pop]
            
            length = len(pop)
            mean = sum(fits) / length
            sum2 = sum(x*x for x in fits)
            std = abs(sum2 / length - mean**2)**0.5
            
            print("  Min %s" % min(fits))
            print("  Max %s" % max(fits))
            print("  Avg %s" % mean)
            print("  Std %s" % std)

            b = tools.selBest(pop,1)[0]
            if not best_ind or b.fitness.values > best_ind.fitness.values:
                best_ind = b
        print("-- End of (successful) evolution --")
        end = time.time()
        print("time taken: {0}".format(end-start))
        
        #best_ind = tools.selBest(pop, 1)[0]
        #print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

        al = [(self.cardPool[index], getCardName(self.cardPool[index]), getCardCost(self.cardPool[index])) for index in best_ind]
        al = sorted(al, key = lambda x: (x[2], x[1]))
        al = [x[0] for x in al]
        self.result = al
        self.fitness = best_ind.fitness.values
        return al



# initialSelection is a list of cards id preselected by the user. can by empty
# this method return the result after the genetic algorithm run.
def generateDeck(heroClass, initialSelection, useLibrary=False):
    ga = GeneticAlgorithm(heroClass, initialSelection, useLibrary)
    res = ga.run()
    return res
