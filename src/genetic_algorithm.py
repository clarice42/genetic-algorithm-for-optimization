from tqdm import tqdm

from genetic_operators import select, crossover, mutate, elitism

# check if best individual achieved a fitness higher than the specified threshold
def fitness_threshold(best_fitness_value, fn_thres):
    if not fn_thres:
        return False

    if best_fitness_value >= fn_thres:
        return True

    return False

def genetic_algorithm(population, fn_fitness, possible_values, 
                      population_size, fn_thres=None, ngen=1000, pmut=0.1):

    global_best_solution = None
    global_best_fitness = 0
    history = {'best': [], 'average': []}

    # for each generation
    for i in tqdm(range(ngen)):

        # evaluate fitness of current population
        fitnesses = [fn_fitness(individual) for individual in population]

        # track the best solution in the current generation
        best_fitness = max(fitnesses)
        best_solution = population[fitnesses.index(best_fitness)]

        # record convergence history
        history['best'].append(best_fitness)
        history['average'].append(sum(fitnesses) / len(fitnesses))

        # stores the best solution if it's better than the current global solution
        if best_fitness > global_best_fitness:
            global_best_fitness = best_fitness
            global_best_solution = best_solution

        # check if the best individual achieved a fitness of fn_thres; if so, stop search
        if fitness_threshold(best_fitness, fn_thres):
            return best_solution, best_fitness

        # create a new population
        new_population = []

        # repeat for all individuals from the population
        for i in range(len(population)):

            # select the parents
            parent_1, parent_2 = select(2, population, fn_fitness)

            # recombine the parents, thus producing the child
            child_1, child_2 = crossover(parent_1, parent_2)

            # mutate the children
            child_1 = mutate(child_1, possible_values, pmut)
            child_2 = mutate(child_2, possible_values, pmut)

            # add the children to the new population
            new_population.append(child_1)
            new_population.append(child_2)

        # Apply elitism to select the best individuals and restore the 
        # population length to population_size
        new_population = elitism(new_population, fn_fitness, population_size)
        # move to the new population
        population = new_population

    # return the individual with highest fitness
    return global_best_solution, global_best_fitness, history
