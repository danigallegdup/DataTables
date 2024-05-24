import os
import pandas as pd

def process_all_csv_files(input_directory, output_directory, subsets):
    # List all .csv files in the input directory
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]

    for csv_file in csv_files:
        # Construct the full paths for the input and output files
        input_file_path = os.path.join(input_directory, csv_file)
        output_file_name = f'output_{csv_file}'
        output_file_path = os.path.join(output_directory, output_file_name)

        # Extract and append each subset
        for start_column, end_column in subsets:
            extract_and_append_subset(input_file_path, output_file_path, start_column, end_column)

def extract_and_append_subset(input_file_path, output_file_path, start_column, end_column):
    # Read the input CSV file
    df = pd.read_csv(input_file_path)

    # Extract the subset of columns
    subset_df = df.loc[:, start_column:end_column]

    # Append the subset dataframe to the output file
    if not os.path.exists(output_file_path):
        subset_df.to_csv(output_file_path, index=False)  # Headers are included by default
    else:
        subset_df.to_csv(output_file_path, mode='a', header=False, index=False)  # No headers when appending
    

# Define directories
input_directory = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step2_groups_of_24/"
output_directory = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Divided_t2345"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define the column ranges for subsets
subsets = [
    ("1Header", "1Answer Column / Row"),
    ("2Header", " 2Answer Column / Row"),
    ("3Header", " 3Answer Column / Row"),
    (" 4Header", "4Answer Column / Row"),
    (" 5Header", "5Answer Column / Row")
]

# Process all CSV files in the input directory
process_all_csv_files(input_directory, output_directory, subsets)

print(f"Subsets extracted and saved to {output_directory}")
