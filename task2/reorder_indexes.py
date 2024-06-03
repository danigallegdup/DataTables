import numpy as np
import pandas as pd
from scipy.stats import pearsonr

# Given set of numbers
numbers = np.array([75, 72, 25, 26, 17, 67, 20, 22, 17, 61, 59, 77, 11, 27, 93, 97, 41, 11, 49, 51, 52, 25, 44, 50, 50, 92, 85, 30, 49])

# Function to calculate correlation
def calculate_correlation(original, permuted):
    return pearsonr(original, permuted)[0]

# Function to find permutation for desired correlation
def find_permutation_for_correlation(numbers, desired_correlation, tolerance=0.01):
    found = False
    while not found:
        permutation = np.random.permutation(len(numbers))
        permuted_numbers = numbers[permutation]
        correlation = calculate_correlation(numbers, permuted_numbers)
        if np.abs(correlation - desired_correlation) < tolerance:
            found = True
    return permutation, correlation

# Find permutations for the desired correlations
desired_correlations = [0.5, 0.4, 0.3, 0.2]
tolerance = 0.01
permutations = {}

for corr in desired_correlations:
    permutation, _ = find_permutation_for_correlation(numbers, corr, tolerance)
    permutations[f"Index_{corr}_Correlation"] = permutation + 1  # Converting to 1-based index

# Create a DataFrame with all permutations
df = pd.DataFrame(permutations)

# Save to Excel
file_path = "./permutation_indices_multiple_correlations.xlsx"
df.to_excel(file_path, index=False)

file_path
