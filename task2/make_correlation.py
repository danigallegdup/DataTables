import numpy as np
import pandas as pd
from openpyxl import load_workbook
import os
import random
from sklearn.metrics import mean_absolute_error 
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error


def generate_correlated_numbers(dataset_num, target_corr, target_mean_absolute_error, size=1000, tolerance=0.01):
    # Set a random seed for reproducibility
    np.random.seed(42)
    n = len(dataset_num)  # Get the number of elements in the dataset

    # Generate initial random numbers with a standard normal distribution
    random_numbers = np.random.normal(0, 1, n)

    # Create a covariance matrix based on the target correlation
    covariance_matrix = np.array([[1, target_corr], [target_corr, 1]])
    
    # Perform Cholesky decomposition to create a transformation matrix
    L = np.linalg.cholesky(covariance_matrix)
    
    # Stack the original dataset and the random numbers vertically
    z = np.vstack([dataset_num, random_numbers])
    
    # Apply the linear transformation to introduce the desired correlation
    transformed_data = np.dot(L, z)
    
    # Extract the correlated data
    correlated_numbers = transformed_data[1, :]
    # Normalize the correlated data to have the same mean and standard deviation as the original dataset
    correlated_numbers = correlated_numbers * (dataset_num.std() / np.std(correlated_numbers))
    correlated_numbers = correlated_numbers + (dataset_num.mean() - np.mean(correlated_numbers))

    # Apply min-max normalization to scale the numbers to the range [11, 98]
    min_val = 11
    max_val = 98
    correlated_numbers = (correlated_numbers - np.min(correlated_numbers)) * (max_val - min_val) / (np.max(correlated_numbers) - np.min(correlated_numbers)) + min_val
    
    # Convert the numbers to integers
    correlated_numbers = correlated_numbers.astype(int)

    # Calculate initial mean absolute error (MAE) and root mean squared error (RMSE)
    mae = mean_absolute_error(dataset_num, correlated_numbers)

    max_iterations = 1000  # Set a limit for the number of iterations
    iteration = 0
    
    # Adjust numbers until MAE and RMSE are close to target values or maximum iterations are reached
    while (abs(mae - target_mean_absolute_error) > tolerance) and iteration < max_iterations:
        # Add a small random noise to the correlated numbers
        noise = np.random.normal(0, 0.01, size=correlated_numbers.shape)
        correlated_numbers = correlated_numbers.astype(float)  # Convert to float before adding noise
        correlated_numbers += noise
    
        # Ensure the numbers are still within the desired range
        correlated_numbers = np.clip(correlated_numbers, min_val, max_val)
    
        # Recalculate MAE and RMSE
        mae = mean_absolute_error(dataset_num, correlated_numbers)
        rmse = np.sqrt(mean_squared_error(dataset_num, correlated_numbers))
    
        iteration += 1  # Increment the iteration count
    
    # Convert the numbers back to integers
    correlated_numbers = correlated_numbers.astype(int)
    return correlated_numbers
    

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


def answer(Current_DS):
        Current_Corr_Set = dataSet(Current_DS)

        target_corr = 0.70
        target_mean_absolute_error = 10
        target_Root_Mean_Squared_Error = 13

        # Generate correlated numbers
        correlated_numbers = generate_correlated_numbers(Current_Corr_Set, target_corr, target_mean_absolute_error)

        for i in correlated_numbers:
            print(i)

            # Calculate and print the actual MAE
        actual_mae = mean_absolute_error(Current_Corr_Set, correlated_numbers)
        print(f'Actual MAE: {actual_mae}')

        # Calculate and print the actual correlation
        actual_corr, _ = pearsonr(Current_Corr_Set, correlated_numbers)
        print(f'Actual correlation: {actual_corr}')

        return correlated_numbers


def main():
    correlated_colums = []

    for i in range(1, 17):
        a = answer(i)
        correlated_colums.append(a)


    # Convert the list of lists to a DataFrame
    df = pd.DataFrame(zip(*correlated_colums), columns=[f'Correlated Numbers {i+1}' for i in range(len(correlated_colums))])
    
    # Output the DataFrame to an Excel file
    df.to_excel('correlated_numbers.xlsx', index=False)

  
if __name__ == "__main__":
    main()
