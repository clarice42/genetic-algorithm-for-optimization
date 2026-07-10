import bisect
import random

# Implementation of roulette wheel selection, where individuals with
# higher fitness are selected with higher probability
def select(number_of_individuals, population, fn_fitness):
    fitnesses = map(fn_fitness, population)
    sampler = fitness_sampler(population, fitnesses)
    return [sampler() for i in range(number_of_individuals)]

# Implementation of a function that whenever called returns a single sample from the population
# The probability of a sample being returned is proportional to its fitness value
def fitness_sampler(population, fitness_values):
    totals_fitness = []
    for fitness in fitness_values:
        totals_fitness.append(fitness + totals_fitness[-1] if totals_fitness else fitness)
    return lambda: population[bisect.bisect(totals_fitness, random.uniform(0, totals_fitness[-1]))]

# Implementation of single-point crossover, where the resulting individuals carry
# a portion from parent 1 and a portion from parent 2, with c selected at random
def crossover(parent_1, parent_2):
    parent_1_size = len(parent_1)
    crossover_point = random.randrange(0, parent_1_size)
    individual_1 = parent_1[:crossover_point] + parent_2[crossover_point:]
    individual_2 = parent_2[:crossover_point] + parent_1[crossover_point:]
    return individual_1, individual_2

# Implementation of mutation, where a single element of the individual
# is selected at random and its value is changed by a randomly chosen value
def mutate(individual, possible_values, mut_probability):

    # if random >= mut_probability, then no mutation is performed
    # and the original individual is returned
    if random.uniform(0, 1) >= mut_probability:
        return individual

    gene_to_be_mutated = random.randrange(0, len(individual))
    new_gene_value = random.randrange(0, len(possible_values))
    new_gene = possible_values[new_gene_value]
    return individual[:gene_to_be_mutated] + [new_gene] + individual[gene_to_be_mutated+1:]

# Implementation of elitism, where the fitness of each individual 
# is used to reorder the population by best fitness; the population_size
# defines how many individuals will be returned
def elitism(population, fn_fitness, population_size):
  population_fitness_mapping = []
  for individual in population:
    fitness = fn_fitness(individual)
    population_fitness_mapping.append({"individual": individual, "fitness": fitness})

  # Sort by fitness in descending order
  population_fitness_mapping.sort(key=lambda solution: solution["fitness"], reverse=True)
  population_desc = [solution["individual"] for solution in population_fitness_mapping]
  return population_desc[:population_size]