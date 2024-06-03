import numpy as np
import pandas as pd
from openpyxl import load_workbook
import os
import random
from scipy.stats import pearsonr

def generate_correlated_numbers(dataset_num, target_corr, size=1000, tolerance=0.01, noise_bias=17):
    np.random.seed(42)  # For reproducibility
    n = len(dataset_num)

    # Generate random numbers with standard normal distribution
    random_numbers = np.random.normal(0, 1, n)

    # Create a covariance matrix based on the target correlation
    covariance_matrix = np.array([[1, target_corr], [target_corr, 1]])
    
    # Perform Cholesky decomposition to create a transformation matrix
    L = np.linalg.cholesky(covariance_matrix)
    
    # Create a new matrix of the initial random numbers
    z = np.vstack([dataset_num, random_numbers])
    
    # Apply the linear transformation
    transformed_data = np.dot(L, z)
    
    # Normalize the new correlated data to have the same mean and std as the given numbers
    correlated_numbers = transformed_data[1, :]
    correlated_numbers = correlated_numbers * (dataset_num.std() / np.std(correlated_numbers))
    correlated_numbers = correlated_numbers + (dataset_num.mean() - np.mean(correlated_numbers))

    # Ensure numbers are within the required range 11-98
    correlated_numbers = np.clip(correlated_numbers, 11, 98)

    # Iteratively adjust the correlated numbers until the correlation is close enough to the target
    while abs(np.corrcoef(dataset_num, correlated_numbers)[0, 1] - target_corr) > tolerance:
        noise = np.random.normal(scale=noise_bias, size=n)
        correlated_numbers += noise
        correlated_numbers = correlated_numbers * (dataset_num.std() / np.std(correlated_numbers))
        correlated_numbers = correlated_numbers + (dataset_num.mean() - np.mean(correlated_numbers))
        correlated_numbers = np.clip(correlated_numbers, 11, 98)

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

def adjust_correlation(original_data, target_corr):
    # Generate random numbers
    new_data = np.random.normal(size=len(original_data))

    # Calculate the current correlation
    current_corr, _ = pearsonr(original_data, new_data)

    # Adjust the new data until the correlation is close to the target
    while not np.isclose(current_corr, target_corr, atol=0.01):
        # If the current correlation is less than the target, increase the new data
        if current_corr < target_corr:
            new_data += 0.01
        # If the current correlation is greater than the target, decrease the new data
        else:
            new_data -= 0.01

        # Recalculate the correlation
        current_corr, _ = pearsonr(original_data, new_data)

    return new_data

def main():
    num_of_columns = 5
    output_file = 'correlated_values.xlsx'
    target_corrs= [0.9, 0.5, 0.4, 0.3, 0.2]
    
    
    # Remove existing file if it exists (for clean run)
    if os.path.exists(output_file):
        os.remove(output_file)

    # Generate for all datasets (1-->16)
    for ds_num in range(1, 17):
        dataset_num = dataSet(ds_num)

        if len(dataset_num) == 0:
            print(f"Invalid dataset number: {ds_num}.")
            continue

        # makes a list of 4 lists of correlated numbers
        # Generate four columns of correlated numbers
        correlated_data = []
        i =0
        for _ in range(num_of_columns):
            target_corr = target_corrs[i]
            correlated_numbers = generate_correlated_numbers(dataset_num, target_corr)

            correlated_numbers = np.round(correlated_numbers).astype(int)
            correlated_data.append(correlated_numbers)
            # Calculate the actual correlation
            actual_corr, _ = pearsonr(dataset_num, correlated_numbers)
            print(f'Actual correlation for set {i+1}: {actual_corr}')
            i+=1

        # Transpose data for dataframe
        correlated_data = np.array(correlated_data).T

        # Output to Excel
        df = pd.DataFrame(correlated_data, columns=[f'Correlated Values {i+1}' for i in range(num_of_columns)])
        # Add a row with the actual correlations
        df.loc['Actual Correlation'] = [pearsonr(df[col], dataset_num)[0] for col in df.columns]
        sheet_name = f'Sheet{ds_num}'
        
        # Save the data to Excel, creating a new file if it doesn't exist, or appending if it does
        if os.path.isfile(output_file):
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"Dataset {ds_num} processed and saved to {sheet_name}.")

if __name__ == "__main__":
    main()
