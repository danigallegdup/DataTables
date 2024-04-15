import numpy as np

# Given set of numbers
given_numbers = [47, 68, 62, 43, 43, 47, 65, 42, 28, 71, 36, 24, 16, 53, 42, 70, 59, 15, 24, 37, 27, 40, 56, 41, 21, 32, 25, 21, 23]

# Generate correlated random numbers
def generate_correlated_numbers(given_numbers, target_corr, size=1000):
    # Generate uncorrelated random numbers
    random_numbers = np.random.rand(size)
    
    # Calculate mean and standard deviation
    given_mean = np.mean(given_numbers)
    given_std = np.std(given_numbers)
    random_mean = np.mean(random_numbers)
    random_std = np.std(random_numbers)
    
    # Standardize the given numbers and random numbers
    standardized_given = [(x - given_mean) / given_std for x in given_numbers]
    standardized_random = [(x - random_mean) / random_std for x in random_numbers]
    
    # Calculate covariance
    covariance = np.cov(standardized_given, standardized_random)[0][1]
    
    # Calculate the multiplier for the random numbers
    multiplier = covariance / np.var(standardized_given)
    
    # Generate correlated numbers
    correlated_numbers = [multiplier * x + random_mean for x in standardized_given]
    
    return correlated_numbers

# Generate correlated numbers
correlated_numbers = generate_correlated_numbers(given_numbers, 0.97, len(given_numbers))

print("Correlated numbers:")
print(correlated_numbers)
