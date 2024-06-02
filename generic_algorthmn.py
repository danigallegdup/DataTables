import numpy as np
import random
from deap import base, creator, tools, algorithms
import pandas as pd
import matplotlib.pyplot as plt

# Given dataset A
A = np.array([55, 49, 21, 21, 18, 46, 18, 20, 18, 42, 42, 52, 14, 25, 63, 64, 32, 13, 37, 38, 36, 22, 33, 38, 37, 61, 58, 24, 36])

# Length of dataset
n = len(A)

# Target correlation
target_correlation = 0.99250

# Define evaluation function
def evaluate(individual):
    B = A + np.array(individual)
    correlation = np.corrcoef(A, B)[0, 1]
    mae = np.mean(np.abs(np.array(individual)))
    fitness = (correlation - target_correlation) ** 2
    if not np.all(np.logical_and(11 <= B, B <= 98)) or abs(mae - 15) > 0.1:
        return 1e6,  # Penalize solutions not meeting constraints
    return fitness,

# Set up DEAP framework
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -20, 20)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=n)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm parameters
population = toolbox.population(n=300)
ngen = 50
cxpb = 0.5
mutpb = 0.2

# Run Genetic Algorithm
result, log = algorithms.eaSimple(population, toolbox, cxpb, mutpb, ngen, verbose=True)

# Extract best individual
best_individual = tools.selBest(result, k=1)[0]
epsilon_optimized_ga = np.array(best_individual)

# Construct set B with optimized epsilon
B_optimized_ga = A + epsilon_optimized_ga

# Calculate final correlation and MAE
final_correlation_ga = np.corrcoef(A, B_optimized_ga)[0, 1]
final_mae_ga = np.mean(np.abs(A - B_optimized_ga))



# Assuming A, B_optimized_ga, and epsilon_optimized_ga are defined
df = pd.DataFrame({"A": A, "B": B_optimized_ga, "Epsilon": epsilon_optimized_ga})

# Display the DataFrame
print(df)

# Plot the DataFrame
df.plot(kind='line')
plt.title("GA Optimized Data Set Comparison")
plt.show()

A, B_optimized_ga, final_correlation_ga, final_mae_ga
