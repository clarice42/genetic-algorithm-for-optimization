import numpy as np
import random as random
import matplotlib.pyplot as plt

from evaluate_task_distribution import EvaluateTaskDistribution
from init_population import init_population
from genetic_algorithm import genetic_algorithm
from problem_instance import Tasks, VMs
from round_robin import round_robin_schedule

MUTATION_PROB = 0.1
NUMBER_OF_ITERATIONS = 100
POPULATION_SIZE = 10
WEIGHT = 0.2

seed = 38
random.seed(seed)
np.random.seed(seed)

possible_values = [0, 1, 2, 3]
problem_instance = [Tasks, VMs]

fn_fitness = EvaluateTaskDistribution(problem_instance, WEIGHT)

# individual length
individual_length = len(Tasks)

# initial population
population = init_population(POPULATION_SIZE, possible_values, individual_length)

# run the algoritm
solution, fitness, history = genetic_algorithm(population, fn_fitness, possible_values, POPULATION_SIZE, fn_thres=0.8, ngen=NUMBER_OF_ITERATIONS)

# print the results
print('Resulting solution: %s' % solution)
print('Value of resulting solution: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# Experiments - Number of generations

print("Experiments with different generation values: ")

# 100 generations
solution, fitness, history_100 = genetic_algorithm(population, fn_fitness, possible_values, 
                                      POPULATION_SIZE, fn_thres=0.8, ngen=100)

print('Resulting solution - 100 gen: %s' % solution)
print('Value of resulting solution - 100 gen: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# 500 generations
solution, fitness, history_500 = genetic_algorithm(population, fn_fitness, possible_values, 
                                      POPULATION_SIZE, fn_thres=0.8, ngen=500)

print('Resulting solution - 500 gen: %s' % solution)
print('Value of resulting solution - 500 gen: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# 1000 generations
solution, fitness, history_1000 = genetic_algorithm(population, fn_fitness, possible_values, 
                                      POPULATION_SIZE, fn_thres=0.8, ngen=1000)

print('Resulting solution - 1000 gen: %s' % solution)
print('Value of resulting solution - 1000 gen: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# Experiments - Threshold value

print("Experiments with different threshold values: ")

# Threshold of 0.5
solution, fitness = genetic_algorithm(population, fn_fitness, possible_values, 
                                      POPULATION_SIZE, fn_thres=0.5, ngen=NUMBER_OF_ITERATIONS)

print('Resulting solution - 0.5 threshold: %s' % solution)
print('Value of resulting solution - 0.5 threshold: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# Threshold of 0.7
solution, fitness = genetic_algorithm(population, fn_fitness, possible_values, 
                                      POPULATION_SIZE, fn_thres=0.7, ngen=NUMBER_OF_ITERATIONS)

print('Resulting solution - 0.7 threshold: %s' % solution)
print('Value of resulting solution - 0.7 threshold: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# Threshold of 0.8
solution, fitness, history_t08 = genetic_algorithm(population, fn_fitness, possible_values, 
                                      POPULATION_SIZE, fn_thres=0.8, ngen=NUMBER_OF_ITERATIONS)

print('Resulting solution - 0.8 threshold: %s' % solution)
print('Value of resulting solution - 0.8 threshold: %f' % fitness)

fit = fn_fitness(solution, should_print_values=True)

print("Fitness of solution: ", fit)
print("\n")

# Round Robin execution
rr_solution = round_robin_schedule(problem_instance)

print('Round-robin solution: %s' % rr_solution)
print('Round-robin fitness: %f' % fn_fitness(rr_solution))
print(fn_fitness(rr_solution, should_print_values=True))

plt.figure(figsize=(6,4))
plt.plot(history['best'], label='Melhor fitness')
plt.plot(history['average'], label='Fitness média')
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.legend()
plt.title('Convergência do algoritmo genético')
plt.show()