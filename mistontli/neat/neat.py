import time
import MultiNEAT as NEAT

from parameters import params


class NEATGame:
    def training(self, epochs, num_generations):
        generations = []

        for run in range(epochs):
            generation = self.get_best_genome(run, num_generations)
            generations.append(generation)

            print('Run: {} generations to solve: {}'.format(run, generation))

        average_generations = sum(generations) / len(generations)

        print('All:', generations)
        print('Average:', average_generations)

    def get_best_genome(self, run, num_generations):
        genome_prototype = NEAT.Genome(0, 10, 0, 9, False,
                                       NEAT.ActivationFunction.UNSIGNED_SIGMOID,
                                       NEAT.ActivationFunction.UNSIGNED_SIGMOID,
                                       0, params)

        seed = int(time.clock() * 100)
        population = NEAT.Population(genome_prototype, params, True, 1.0, seed)

        # for num_generations
        # evaluate each member of the population
        # after num_generations, get the fittest genome and save it
        return best_genome

    def evaluate(self, genome):
        network = NEAT.NeuralNetwork()
        genome.BuildPhenotype(network)

        fitness = 0

        # for n games
        # get the winning or lose state
        # get winning or lose rate

        return fitness
