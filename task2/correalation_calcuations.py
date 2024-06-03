import numpy as np
import pandas as pd
from openpyxl import load_workbook
import os
import random
from sklearn.metrics import mean_absolute_error 
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr

"""
Create a excel file that calculates the relationship between the numbers in the dataset and the correlation between them.

1) Read the excel file that contains the numbers.
2) First column should be correalates to dataset(1) and second column should be correled to dataset(2).... match all those columns together
3) create a dictionary for every column:
    - key: dataset number
    - value:list of tuples
        - correlation between the numbers in the dataset
        - difference in range
        - mean absolute error
        - root mean squared error
        - difference in standard deviation
        - difference in mean

4) calculate all 16 of them and save them in a excel file
5) print out the columns of the excel file as a python dictionary (to be u))


"""


def read_excel(file_path):
    df = pd.read_excel(file_path)
    # Convert each column to a list and store it in a dictionary
    data_dict = {int(col.split()[-1]): df[col].tolist() for col in df.columns}

    return data_dict



def dataSet(ds_num):
    datasets = {
        1: [55, 49, 21, 21, 18, 46, 18, 20, 18, 42, 42, 52, 14, 25, 63, 64, 32, 13, 37, 38, 36, 22, 33, 38, 37, 61, 58, 24, 36],
        2: [47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23],
        3: [65, 32, 42, 62, 68, 37, 21, 59, 71, 24, 28, 53, 15, 43, 43, 25, 27, 47, 23, 42, 36, 16, 47, 56, 70, 41, 24, 40, 21],
        4: [50, 18, 31, 27, 22, 46, 25, 40, 19, 14, 15, 21, 17, 32, 36, 11, 17, 32, 23, 25, 17, 54, 43, 46, 25, 47, 31, 33, 21],
        5: [17, 46, 54, 25, 25, 27, 40, 23, 31, 14, 32, 47, 11, 22, 46, 17, 32, 15, 25, 17, 36, 21, 43, 31, 50, 18, 33, 21, 19],
        6: [63, 21, 18, 24, 61, 32, 37, 55, 18, 38, 33, 38, 37, 22, 42, 49, 13, 36, 25, 64, 42, 20, 21, 36, 18, 52, 14, 46, 58],
        7: [25, 43, 19, 15, 54, 25, 17, 46, 14, 36, 21, 32, 27, 21, 46, 47, 31, 25, 23, 22, 50, 18, 32, 11, 40, 33, 17, 31, 17],
        8: [31, 21, 25, 40, 46, 19, 23, 27, 14, 11, 18, 17, 25, 47, 46, 33, 50, 21, 54, 25, 31, 17, 36, 22, 15, 32, 43, 17, 32],
        9: [21, 17, 25, 32, 54, 19, 17, 47, 31, 46, 27, 25, 11, 18, 46, 43, 25, 33, 15, 32, 22, 40, 50, 17, 21, 36, 31, 14, 23],
        10: [17, 43, 15, 32, 21, 27, 11, 25, 32, 40, 19, 33, 17, 22, 18, 54, 23, 25, 46, 25, 31, 36, 31, 50, 46, 17, 21, 14, 47],
        11: [17, 19, 54, 11, 31, 46, 25, 21, 21, 27, 40, 31, 22, 15, 46, 36, 33, 18, 17, 14, 23, 25, 32, 32, 47, 50, 25, 17, 43],
        12: [42, 25, 20, 36, 18, 55, 42, 24, 32, 37, 38, 46, 49, 58, 37, 18, 21, 14, 52, 22, 63, 38, 36, 18, 33, 64, 61, 13, 21],
        13: [22, 58, 38, 14, 21, 21, 24, 52, 55, 13, 42, 18, 46, 63, 61, 36, 25, 32, 64, 36, 49, 38, 18, 37, 33, 20, 37, 18, 42],
        14: [22, 36, 47, 14, 17, 32, 40, 32, 17, 33, 31, 43, 15, 18, 17, 54, 19, 50, 27, 23, 21, 46, 31, 25, 21, 25, 46, 25, 11],
        15: [31, 18, 11, 54, 25, 25, 17, 14, 17, 36, 46, 46, 17, 43, 40, 19, 27, 31, 25, 50, 21, 21, 33, 23, 22, 32, 15, 47, 32],
        16: [33, 14, 58, 63, 21, 38, 21, 61, 52, 36, 55, 36, 32, 24, 38, 64, 46, 18, 49, 18, 25, 37, 13, 42, 22, 18, 42, 20, 37],
    }
    return np.array(datasets.get(ds_num, []))


def calculate_metric(set1, set2):
    # Calculate the correlation coefficient
    correlation_matrix = np.corrcoef(set1, set2)

    # The correlation coefficient is the value at position [0, 1] in the matrix
    correlation_coefficient = correlation_matrix[0, 1]
    print(f'Correlation coefficient: {correlation_coefficient}')
    range_diff = (max(set1) - min(set1)) - (max(set2) - min(set2))
    mae = mean_absolute_error(set1, set2)
    rmse = np.sqrt(mean_squared_error(set1, set2))
    std_diff = np.std(set1) - np.std(set2)
    mean_diff = np.mean(set1) - np.mean(set2)
    # print(f'Correlation coefficient: {(correlation_coefficient, range_diff, mae, rmse, std_diff, mean_diff)}')
    return (correlation_coefficient, range_diff, mae, rmse, std_diff, mean_diff)



# Function to calculate correlation
def calculate_correlation(original, permuted):
    return pearsonr(original, permuted)[0]

# Function to find permutation for desired correlation
def find_permutation_for_correlation(numbers, desired_correlation, tolerance=0.01):
    print(numbers)
    numbers = np.array(numbers)
    found = False
    while not found:
        permutation = np.random.permutation(len(numbers))
        permuted_numbers = numbers[permutation]
        correlation = calculate_correlation(numbers, permuted_numbers)
        if np.abs(correlation - desired_correlation) < tolerance:
            found = True
    return permutation, correlation

def sort_by_indices(indices, numbers):
    # Convert indices and numbers to numpy arrays
    indices = np.array(indices)
    numbers = np.array(numbers)

    # Get the sorted indices
    sorted_indices = np.argsort(indices)

    # Sort the numbers using the sorted indices
    sorted_numbers = numbers[sorted_indices]

    return sorted_numbers.tolist()

def generate_permutations_and_save(numbers, filename):
    # Find permutations for the desired correlations
    desired_correlations = [0.5, 0.4, 0.3, 0.2]
    tolerance = 0.01
    permutations = {}

    for corr in desired_correlations:
        permutation, _ = find_permutation_for_correlation(numbers, corr, tolerance)
        permutations[f"Index_{corr}_Correlation"] = permutation + 1  # Converting to 1-based index
        #permutations[f"Numbers_{corr}_Correlation"] = sort_by_indices(permutation[f"Numbers_{corr}_Correlation"], numbers)


    # Create a DataFrame with all permutations
    df = pd.DataFrame(permutations)

    # Save to Excel
    df.to_excel(filename, index=False)

    return filename


def main():
    print('Reading the excel file...')
    file_path = "./correlated_numbers_currtently.xlsx"
    correlated_set = read_excel(file_path)
    metric_dict = {}

    for i in range(1, 17):
        metric_result = calculate_metric(correlated_set[i], dataSet(i))
        metric_dict[i] = metric_result
    
    for i in range(1, 17):

        generate_permutations_and_save(correlated_set[i],f"./dataset_{i}.xlsx")


    print(metric_dict[1])


   


  
if __name__ == "__main__":
    main()
