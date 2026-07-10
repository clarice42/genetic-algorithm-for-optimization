import random

def init_population(population_size, possible_values, individual_size):
    max_value = len(possible_values)
    population = []

    for i in range(population_size):
        # each individual is represented as an array with size equivalent to the 
        # number of tasks; each position in the array contains a value from possible_values
        # (which represent the VMs indexes) selected at random
        new_individual = [possible_values[random.randrange(0, max_value)] for j in range(individual_size)]
        population.append(new_individual)

    return population