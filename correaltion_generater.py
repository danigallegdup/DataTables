
import numpy as np

def generate_correlated_numbers(given_numbers, target_corr, size=1000, tolerance=0.01):
    np.random.seed(42)  # For reproducibility
    n = len(given_numbers)

    # Generate random numbers with standard normal distribution
    random_numbers = np.random.normal(0, 1, n)

    # Create a covariance matrix based on the target correlation
    covariance_matrix = np.array([[1, target_corr], [target_corr, 1]])
    
    # Perform Cholesky decomposition to create a transformation matrix
    L = np.linalg.cholesky(covariance_matrix)
    
    # Create a new matrix of the initial random numbers
    z = np.vstack([given_numbers, random_numbers])
    
    # Apply the linear transformation
    transformed_data = np.dot(L, z)
    
    # Normalize the new correlated data to have the same mean and std as the given numbers
    correlated_numbers = transformed_data[1, :]
    correlated_numbers = correlated_numbers * (given_numbers.std() / np.std(correlated_numbers))
    correlated_numbers = correlated_numbers + (given_numbers.mean() - np.mean(correlated_numbers))

    # Iteratively adjust the correlated numbers until the correlation is close enough to the target
    while abs(np.corrcoef(given_numbers, correlated_numbers)[0, 1] - target_corr) > tolerance:
        noise = np.random.normal(scale=0.1, size=n)
        correlated_numbers += noise
        correlated_numbers = correlated_numbers * (given_numbers.std() / np.std(correlated_numbers))
        correlated_numbers = correlated_numbers + (given_numbers.mean() - np.mean(correlated_numbers))

    return correlated_numbers

def dataSet(ds_num):
    if ds_num == 1:
        numbers = [55, 49, 21, 21, 18, 46, 18, 20, 18, 42, 42, 52, 14, 25, 63, 64, 32, 13, 37, 38, 36, 22, 33, 38, 37, 61, 58, 24, 36]
        return np.array(numbers)
    if ds_num == 2:
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 3:
        np.array([65, 32, 42, 62, 68, 37, 21, 59, 71, 24, 28, 53, 15, 43, 43, 25, 27, 47, 23, 42, 36, 16, 47, 56, 70, 41, 24, 40, 21])
    if ds_num == 4:
        numbers = [50, 18, 31, 27, 22, 46, 25, 40, 19, 14, 15, 21, 17, 32, 36, 11, 17, 32, 23, 25, 17, 54, 43, 46, 25, 47, 31, 33, 21]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 5:
        numbers = [17, 46, 54, 25, 25, 27, 40, 23, 31, 14, 32, 47, 11, 22, 46, 17, 32, 15, 25, 17, 36, 21, 43, 31, 50, 18, 33, 21, 19]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 6:
        numbers = [63, 21, 18, 24, 61, 32, 37, 55, 18, 38, 33, 38, 37, 22, 42, 49, 13, 36, 25, 64, 42, 20, 21, 36, 18, 52, 14, 46, 58]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 7:
        numbers = [25, 43, 19, 15, 54, 25, 17, 46, 14, 36, 21, 32, 27, 21, 46, 47, 31, 25, 23, 22, 50, 18, 32, 11, 40, 33, 17, 31, 17]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 8:
        numbers = [31, 21, 25, 40, 46, 19, 23, 27, 14, 11, 18, 17, 25, 47, 46, 33, 50, 21, 54, 25, 31, 17, 36, 22, 15, 32, 43, 17, 32]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 9:
        numbers = [21, 17, 25, 32, 54, 19, 17, 47, 31, 46, 27, 25, 11, 18, 46, 43, 25, 33, 15, 32, 22, 40, 50, 17, 21, 36, 31, 14, 23]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 10:
        numbers = [17, 43, 15, 32, 21, 27, 11, 25, 32, 40, 19, 33, 17, 22, 18, 54, 23, 25, 46, 25, 31, 36, 31, 50, 46, 17, 21, 14, 47]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 11:
        numbers = [17, 19, 54, 11, 31, 46, 25, 21, 21, 27, 40, 31, 22, 15, 46, 36, 33, 18, 17, 14, 23, 25, 32, 32, 47, 50, 25, 17, 43]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 12:
        numbers = [42, 25, 20, 36, 18, 55, 42, 24, 32, 37, 38, 46, 49, 58, 37, 18, 21, 14, 52, 22, 63, 38, 36, 18, 33, 64, 61, 13, 21]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 13:
        numbers = [22, 58, 38, 14, 21, 21, 24, 52, 55, 13, 42, 18, 46, 63, 61, 36, 25, 32, 64, 36, 49, 38, 18, 37, 33, 20, 37, 18, 42]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 14:
        numbers = [22, 36, 47, 14, 17, 32, 40, 32, 17, 33, 31, 43, 15, 18, 17, 54, 19, 50, 27, 23, 21, 46, 31, 25, 21, 25, 46, 25, 11]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 15:
        numbers = [31, 18, 11, 54, 25, 25, 17, 14, 17, 36, 46, 46, 17, 43, 40, 19, 27, 31, 25, 50, 21, 21, 33, 23, 22, 32, 15, 47, 32] 
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
    if ds_num == 16:
        numbers = [33, 14, 58, 63, 21, 38, 21, 61, 52, 36, 55, 36, 32, 24, 38, 64, 46, 18, 49, 18, 25, 37, 13, 42, 22, 18, 42, 20, 37]
        return np.array([47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23])
  


def main():
   # Given set of 

    # Ask the user to enter the dataset number
    ds_num = int(input("Enter the dataset number: "))
    given_numbers = dataSet(ds_num)

    # Ask the user to enter the target correlation
    target_corr = float(input("Enter the target correlation: "))

    correlated_numbers = generate_correlated_numbers(given_numbers, target_corr)

    # Ensure the numbers are integers
    correlated_numbers = np.round(correlated_numbers).astype(int)

    # Check the actual correlation achieved
    actual_corr = np.corrcoef(given_numbers, correlated_numbers)[0, 1]

    # Print results
    print("Desired Correlation Coefficient:", target_corr)
    print("Actual Correlation Coefficient:", actual_corr)
    print("Correlated numbers:")
    for i in range(len(correlated_numbers)):
        print(correlated_numbers[i])


if __name__ == "__main__":
    main()